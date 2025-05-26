from collections.abc import Callable, Sequence
from typing import Any, Optional

import click
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import BaseStyle, merge_styles
from pydantic import TypeAdapter
from questionary import utils
from questionary.constants import (
    DEFAULT_KBI_MESSAGE,
    DEFAULT_QUESTION_PREFIX,
    DEFAULT_SELECTED_POINTER,
    DEFAULT_STYLE,
)
from questionary.prompts import common
from questionary.prompts.common import Choice

from alltheutils.cli.base import ExtInquirerControl, ExtQuestion
from alltheutils.cli.dataclasses import CLIConfig
from alltheutils.config import read_conf_file
from alltheutils.instance_config import get_instance_config, has_instance_config
from alltheutils.utils import get_value_from_or_update_nested_dict, load_language_texts

PARAMETER_TYPES = ["arguments", "options"]


def select(  # noqa: C901
    message: str,
    choices: Sequence[str | Choice | dict[str, Any]] | dict[str, Any],
    default: Optional[Any] = None,
    instruction: Optional[str] = None,
    answer_text: Optional[str] = None,
    keyboard_interrupt_message: Optional[str] = None,
    qmark: Optional[str] = None,
    pointer: Optional[str] = None,
    style: Optional[BaseStyle] = None,
    show_selected: Optional[bool] = None,
    ret_err: Optional[bool] = None,
    **kwargs: dict[str, Any],
) -> tuple[bool, Any]:
    class _CEIQ(ExtInquirerControl):  # type: ignore[misc]
        pass

    class _CEQ(ExtQuestion):  # type: ignore[misc]
        pass

    if has_instance_config("language"):
        default_language = get_instance_config("language")
    else:
        default_language = "en"
    language_texts = load_language_texts(default_language)

    if instruction is None:
        instruction = get_value_from_or_update_nested_dict(language_texts, "cli.prompt.list_selector_instruction")  # type: ignore

    if answer_text is None:
        answer_text = get_value_from_or_update_nested_dict(language_texts, "cli.prompt.answer")  # type: ignore

    if keyboard_interrupt_message is None:
        keyboard_interrupt_message = get_value_from_or_update_nested_dict(language_texts, "cli.general.keyboard_interrupt")  # type: ignore

    if qmark is None:
        qmark = DEFAULT_QUESTION_PREFIX

    if pointer is None:
        pointer = DEFAULT_SELECTED_POINTER

    if show_selected is None:
        show_selected = False

    if ret_err is None:
        ret_err = False

    cd = False
    if type(choices).__mro__[-2] is dict:
        cd = True
        oc = choices.copy()  # type: ignore[union-attr]
        final_choices: Sequence[str | Choice | dict[str, Any]] = list(choices.keys())  # type: ignore[union-attr]
    else:
        final_choices = choices  # type: ignore[assignment]

    if style is not None:
        style = merge_styles([DEFAULT_STYLE, style])

    ic = _CEIQ(
        final_choices,
        default,
        pointer=pointer,
        use_indicator=False,
        use_shortcuts=False,
        show_selected=show_selected,
        use_arrow_keys=True,
        initial_choice=default,
    )

    def get_prompt_tokens() -> list[tuple[str, str]]:
        choice = ic.get_pointed_at().title

        _msg = message
        _instruction = instruction

        if cd:
            _val = oc[choice]  # type: ignore[index]

            if type(_val).__mro__[-2] is dict:
                _msg = _val.get("message", _msg)

                _CEQ.kbi = DEFAULT_KBI_MESSAGE

                _instruction = _val.get("instruction", _instruction)
                _CEIQ.answer_text = _val.get(
                    "answer",
                    answer_text if answer_text else _CEIQ.answer_text,
                )
                _CEQ.kbi = _val.get(
                    "keyboard_interrupt",
                    (
                        keyboard_interrupt_message
                        if keyboard_interrupt_message
                        else _CEQ.kbi
                    ),
                )

        tokens = [("class:qmark", qmark), ("class:question", f" {_msg} ")]

        if ic.is_answered:
            if isinstance(choice, list):
                tokens.append(
                    (
                        "class:answer",
                        "".join([token[1] for token in choice]),
                    ),
                )
            else:
                tokens.append(("class:answer", choice))  # type: ignore
        else:
            tokens.append(("class:instruction", f"({_instruction})"))

        return tokens  # type: ignore[return-value]

    layout = common.create_inquirer_layout(ic, get_prompt_tokens, **kwargs)

    bindings = KeyBindings()

    @bindings.add(Keys.ControlQ, eager=True)
    @bindings.add(Keys.ControlC, eager=True)
    def _(event: KeyPressEvent) -> None:
        event.app.exit(exception=KeyboardInterrupt, style="class:aborting")

    @bindings.add(Keys.Down, eager=True)
    def move_cursor_down(event: KeyPressEvent) -> None:
        ic.select_next()
        while not ic.is_selection_valid():
            ic.select_next()

    @bindings.add(Keys.Up, eager=True)
    def move_cursor_up(event: KeyPressEvent) -> None:
        ic.select_previous()
        while not ic.is_selection_valid():
            ic.select_previous()

    @bindings.add(Keys.ControlM, eager=True)
    def set_answer(event: KeyPressEvent) -> None:
        ic.is_answered = True
        event.app.exit(result=ic.get_pointed_at().value)

    @bindings.add(Keys.ControlS, eager=True)
    @bindings.add(Keys.Any)
    def other(event: KeyPressEvent) -> None:
        """Disallow inserting other text."""

    err, res = _CEQ(
        Application(
            layout=layout,
            key_bindings=bindings,
            style=style,
            **utils.used_kwargs(kwargs, Application.__init__),
        ),
    ).ask()

    if err and cd:
        res = oc[res]
        if type(res).__mro__[-2] is dict:
            res = res.get("value", res)
    return err, res


def str_to_type(str_type: str) -> Any:  # noqa: C901
    match str_type:
        case "int":
            return int
        case "float":
            return float
        case "bool":
            return bool
        case "str":
            return str
        case "tuple":
            return tuple
        case "Choice":
            return click.Choice
        case "DateTime":
            return click.DateTime
        case "UUIDParameter":
            return click.types.UUIDParameterType
        case "File":
            return click.File
        case "Path":
            return click.Path
        case _:
            return str


def command_type_str_to_type(
    commands: dict[str, Any],
) -> Any:
    for command_name, command_value in commands.items():
        for parameter_type in PARAMETER_TYPES:
            command_parameters = command_value.get(parameter_type, {})
            for (
                command_parameter_name,
                command_parameter_value,
            ) in command_parameters.items():
                command_parameter_kwargs = command_parameter_value.get("kwargs", {})
                command_parameter_type = command_parameter_kwargs.get("type")
                if isinstance(command_parameter_type, str):
                    commands[command_name][parameter_type][command_parameter_name][
                        "kwargs"
                    ]["type"] = str_to_type(command_parameter_type)


def parse_config_file_cli_config(
    file_path: str,
    filters_before_conversion: Optional[
        list[Callable[[dict[str, Any]], dict[str, Any]]]
    ] = None,
) -> CLIConfig:
    cli_config = read_conf_file(file_path)
    commands = cli_config.get("commands", {})

    command_type_str_to_type(commands=commands)

    if filters_before_conversion:
        for filter in filters_before_conversion:
            cli_config = filter(cli_config)

    ta = TypeAdapter(CLIConfig)  # type: ignore
    return ta.validate_python(cli_config)

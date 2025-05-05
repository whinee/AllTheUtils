from collections.abc import Sequence
from typing import Any, Optional

from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import BaseStyle, merge_styles
from pydantic_yaml import parse_yaml_file_as
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
from alltheutils.cli.dataclasses import CommandConfig
from alltheutils.instance_config import requires_instance_config


@requires_instance_config("language_constant")
def select(  # noqa: C901
    message: str,
    choices: Sequence[str | Choice | dict[str, Any]] | dict[str, Any],
    language_constant: dict[str, Any],
    default: Optional[Any] = None,
    instruction: Optional[str] = None,
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

    if language_constant.get("en"):
        language_constant = language_constant["en"]

    if instruction is None:
        instruction = language_constant["cli"]["prompt"]["list_instruction"]

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
                _CEIQ.answer_text = _val.get("answer", _CEIQ.answer_text)
                _CEQ.kbi = _val.get("kbi", _CEQ.kbi)

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


def parse_yaml_file_command_config(file_path: str) -> CommandConfig:
    return parse_yaml_file_as(CommandConfig, file_path)

"""
Parts of code in `alltheutils/cli/base.py` is derived from [click](https://github.com/pallets/click)

3-Clause BSD License

Copyright © 2014-2025 Pallets

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1.  Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

2.  Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

Hereunder resides functions for constructing CLI for this program.

> This module heavily documents my descent to madness.
>
> An unholy amalgamation of megalamonia, depression, God complex, and impostor syndrome filled my broken heart.
>
> This file is the digital manifestation of my mental woes.
>
> Masochistic tendencies fuelling my coding sessions.
>
> I wish upon this abyss to not touch this file ever again.

whi~nyaan! ― 2023

---

Update (April 23, 2025):

This still holds true to this day. Please, do not touch if you do not need to.

---

Update (May 4, 2025):

Bruh, why am I touching this?

"""  # noqa: D400, D415

from collections.abc import Callable
from textwrap import wrap
from typing import Any, Final, Optional

import click
from click.core import Group
from click.types import ParamType
from questionary.constants import (
    DEFAULT_KBI_MESSAGE,
    INDICATOR_SELECTED,
    INDICATOR_UNSELECTED,
)
from questionary.prompts.common import Choice, InquirerControl, Separator
from questionary.question import Question
from tabulate import tabulate

from alltheutils import TW, exceptions
from alltheutils.cli.dataclasses import CommandOptionsHelpSchema, CommandSchema

# Constants
CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR: Final[str] = "Ex.: "
DEFAULT_OPTIONS_KWARGS: Final[dict[str, Any]] = {"metavar": ""}
TERMINAL_CLEARANCE: Final[int] = 10

# Derived Constants
CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR_LEN: Final[int] = len(
    CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR,
)


class ExtInquirerControl(InquirerControl):  # type: ignore[misc]
    """Extended/Modified InquirerControl class."""

    answer_text = "Answer"

    def _get_choice_tokens(self) -> list[Any]:  # noqa: C901
        tokens: list[Any] = []

        def append(index: int, choice: Choice) -> None:  # noqa: C901
            # use value to check if option has been selected
            selected = choice.value in self.selected_options

            if index == self.pointed_at:
                if self.pointer is not None:
                    tokens.append(("class:pointer", " {} ".format(self.pointer)))
                else:
                    tokens.append(("class:text", " " * 3))

                tokens.append(("[SetCursorPosition]", ""))
            else:
                pointer_length = len(self.pointer) if self.pointer is not None else 1
                tokens.append(("class:text", " " * (2 + pointer_length)))

            if isinstance(choice, Separator):
                tokens.append(("class:separator", "{}".format(choice.title)))
            elif choice.disabled:  # disabled
                if isinstance(choice.title, list):
                    tokens.append(
                        ("class:selected" if selected else "class:disabled", "- "),
                    )
                    tokens.extend(choice.title)
                else:
                    tokens.append(
                        (
                            "class:selected" if selected else "class:disabled",
                            "- {}".format(choice.title),
                        ),
                    )

                tokens.append(
                    (
                        "class:selected" if selected else "class:disabled",
                        "{}".format(
                            (
                                ""
                                if isinstance(choice.disabled, bool)
                                else " ({})".format(choice.disabled)
                            ),
                        ),
                    ),
                )
            else:
                shortcut = choice.get_shortcut_title() if self.use_shortcuts else ""  # type: ignore[no-untyped-call]

                if selected:
                    if self.use_indicator:
                        indicator = INDICATOR_SELECTED + " "
                    else:
                        indicator = ""

                    tokens.append(("class:selected", "{}".format(indicator)))
                else:
                    if self.use_indicator:
                        indicator = INDICATOR_UNSELECTED + " "
                    else:
                        indicator = ""

                    tokens.append(("class:text", "{}".format(indicator)))

                if isinstance(choice.title, list):
                    tokens.extend(choice.title)
                elif selected:
                    tokens.append(
                        ("class:selected", "{}{}".format(shortcut, choice.title)),
                    )
                elif index == self.pointed_at:
                    tokens.append(
                        ("class:highlighted", "{}{}".format(shortcut, choice.title)),
                    )
                else:
                    tokens.append(("class:text", "{}{}".format(shortcut, choice.title)))

            tokens.append(("", "\n"))

        # prepare the select choices
        for i, c in enumerate(self.choices):
            append(i, c)

        if self.show_selected:
            current = self.get_pointed_at()

            answer = ""

            answer += (
                current.title if isinstance(current.title, str) else current.title[0][1]  # type: ignore[index]
            )

            tokens.append(("class:text", f"  {self.answer_text}: " + answer))
        else:
            tokens.pop()  # Remove last newline.
        return tokens


class ExtQuestion(Question):  # type: ignore[misc]
    """Extended/Modified Question class."""

    kbi = DEFAULT_KBI_MESSAGE

    def ask(self, patch_stdout: Optional[bool] = None, **kwargs: dict[str, Any]) -> tuple[bool, Any]:  # type: ignore[override]
        """
        Ask the question synchronously and return user response.

        Args:
        - patch_stdout (`bool`, optional): Ensure that the prompt renders correctly if other threads are printing to stdout. Defaults to `None`.

        Returns:
        `Any`: The answer from the question.

        """

        if patch_stdout is None:
            patch_stdout = False

        if self.should_skip_question:
            return True, self.default

        try:
            return True, self.unsafe_ask(patch_stdout)
        except KeyboardInterrupt:
            print("\n{}\n".format(self.kbi))
            return False, None


# Base CLI Logic
class CommandWrapper:
    """Returns wrappers for a click command evaluated from the given arguments."""

    def __init__(self, command_config: dict[str, CommandSchema], group: Group) -> None:  # type: ignore
        """
        Initialize object.

        Args:
        - command_config (`dict[str, CommandSchema]`): Command config for initialization of the command.
        - group (`Group`): Command group of the command to be under.

        """

        self.cfg: dict[str, Any] = {"required_options": []}

        self.command_config = command_config
        self.group: Group = group

    def command(  # noqa: C901
        self,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        The command wrapper.

        Returns:
        `Callable[[Callable[..., Any]], Callable[..., Any]]`

        """

        # Initialize Variables
        c_arg_help_ls: list[tuple[str, str, str]] = []

        # Primary Variables
        command_description_help_text = self.cmd.help.description
        command_overview_help_text = self.cmd.help.overview

        if not command_overview_help_text:
            command_overview_help_text = command_description_help_text

        if self.arguments_cfg:
            for arg_name, command_arguments_cfg in self.arguments_cfg.items():
                arg_help = command_arguments_cfg.help

                c_arg_type = command_arguments_cfg.kwargs.type
                c_arg_help = arg_help.help
                c_arg_example = arg_help.example

                c_arg_type_name = ""
                if c_arg_type:
                    if isinstance(c_arg_type, ParamType):
                        c_arg_type_name = c_arg_type.name
                    else:
                        c_arg_type_name = c_arg_type.__name__

                c_arg_example = f"\nEx.: {c_arg_example}" if c_arg_example else ""
                c_arg_help_ls.append(
                    (f"<{arg_name}>", c_arg_type_name, f"{c_arg_help}{c_arg_example}"),
                )

        click_kwargs: dict[str, dict[str, list[str]] | str] = dict(
            {
                "context_settings": {"help_option_names": ["-h", "--help"]},
                "short_help": command_overview_help_text,
                "help": f"\b\n{command_description_help_text}\n{tabulate(c_arg_help_ls, tablefmt='plain')}",
            },
            **self.cmd.kwargs.model_dump(),
        )

        def inner(
            func: Callable[..., Any],
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
            op: Callable[..., Any] = self.group.command(
                *self.cmd.args,
                **click_kwargs,
            )(func)
            return op

        return inner

    def arguments(self) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        The arguments wrapper.

        Returns:
        `Callable[[Callable[..., Any]], Callable[..., Any]]`

        """
        click_args: dict[str, Any] = {}
        click_kwargs: dict[str, Any] = {}

        if not self.arguments_cfg:
            return lambda x: x

        for arg_name, command_arguments_cfg in self.arguments_cfg.items():
            passed_kwargs = command_arguments_cfg.kwargs.model_dump()
            metavar = passed_kwargs.pop("metavar", None)
            kw: dict[str, str] = {
                "metavar": f"<{arg_name}>" if metavar is None else metavar,
            }
            click_args[arg_name] = [arg_name, *command_arguments_cfg.args]
            click_kwargs[arg_name] = dict(kw, **passed_kwargs)

        def inner(
            func: Callable[[Any], Any],
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
            for i in list(click_args.keys()):
                func = click.argument(*click_args[i], **click_kwargs[i])(func)
            return func

        return inner

    def options(  # noqa: C901
        self,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        The options wrapper.

        My God in heaven, I'm agnostic, but please save me from all evil. Amen.

        Returns:
        `Callable[[Callable[..., Any]], Callable[..., Any]]`

        """

        # Fetch Values
        opts = self.cmd.options

        options_kwargs = {}

        # Filter #1
        if not opts:
            return lambda x: x

        # Initialize Variables
        maxlen_option_string: int = 0
        maxlen_type_string: int = 0
        click_args: dict[str, Any] = {}
        click_kwargs: dict[str, Any] = {}

        # Check Longest Type and Help String
        # This is for checking how wide should the help string for each options should be rendered, and if the terminal could even handle it
        for opt_name, opt_cfg in opts.items():
            options_kwargs[opt_name] = kw = {
                **DEFAULT_OPTIONS_KWARGS,
                **opt_cfg.kwargs.model_dump(),
            }

            if opt_cfg.args:
                curlen_option_string = len(f"-{opt_name}, --{opt_cfg.args[0]}")
            else:
                curlen_option_string = len(f"--{opt_name}")
            maxlen_option_string = (
                curlen_option_string
                if curlen_option_string > maxlen_option_string
                else maxlen_option_string
            )

            c_opt_type = kw["type"]

            if kw.get("is_flag"):
                c_opt_type_name = "N/A (flag)"
            else:
                c_opt_type_name = ""

                if c_opt_type:
                    if isinstance(c_opt_type, ParamType):
                        c_opt_type_name = c_opt_type.name
                    else:
                        c_opt_type_name = c_opt_type.__name__
                elif c_opt_type_name and kw.get("multiple"):
                    c_opt_type_name = f"list[{c_opt_type_name}]"

            curlen_type_string = len(c_opt_type_name)
            maxlen_type_string = (
                curlen_type_string
                if curlen_type_string > maxlen_type_string
                else maxlen_type_string
            )

        maxlen_type_string += 2
        maxlen_option_string += 3
        min_width: int = maxlen_type_string + maxlen_option_string
        maxlen_opts_help: int = TW - 2 - min_width
        maxlen_opts_help_clearance: int = maxlen_opts_help - TERMINAL_CLEARANCE

        # Filter #2
        if maxlen_opts_help_clearance <= 0:
            raise exceptions.TerminalTooThin(maxlen_opts_help_clearance)

        opt_the_fn = self.option_type_help_example(
            maxlen_type_string,
            maxlen_opts_help,
        )  # Option [type, help, and example] parser

        for opt_name, opt_cfg in opts.items():
            # Fetch Values
            ## Primary
            a = opt_cfg.args
            kw = options_kwargs[opt_name]

            ## Secondary
            if len(a) != 0:
                a[0] = f"--{a[0]}"
                a.insert(0, f"-{opt_name}")
            else:
                a.insert(0, f"--{opt_name}")

            ## Tertiary
            o_type, o_help, o_example = opt_the_fn(opt_name, kw, opt_cfg.help)

            if o_example and (not o_help):
                o_example = o_example.strip()
            kw["help"] = (
                "\b\n"
                + o_type
                + " " * (maxlen_type_string - len(o_type))
                + o_help
                + o_example
            )
            click_args[opt_name] = a
            click_kwargs[opt_name] = kw

        def inner(
            func: Callable[[Any], Any],
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
            for i in list(click_args.keys()):
                func = click.option(*click_args[i], **click_kwargs[i])(func)
            return func

        return inner

    def option_type_help_example(  # noqa: C901
        self,
        maxlen_type_string: int,
        maxlen_opts_help: int,
    ) -> Callable[..., tuple[str, str, str]]:
        def inner(  # noqa: C901
            opt_name: str,
            kw: dict[str, Any],
            vh: CommandOptionsHelpSchema,
        ) -> tuple[str, str, str]:
            # Primary Variables
            o_type_raw: Any = kw["type"]
            o_help: str | None = vh.help
            o_example: str | None = vh.example

            o_type = ""
            if o_type_raw:
                if isinstance(o_type_raw, ParamType):
                    o_type = o_type_raw.name
                else:
                    o_type = o_type_raw.__name__

            if o_help:
                hls = []

                # Modify option's help string using option's args and kwargs
                if default := kw.get("default"):
                    o_help = f"Defaults to `{default}`. " + o_help
                if kw.pop("required", False):
                    self.cfg["required_options"].append(opt_name)
                    o_help = "[REQUIRED] " + o_help

                for idx, i in enumerate(o_help.splitlines()):
                    indent = " " * maxlen_type_string
                    ils = wrap(
                        text=i,
                        width=maxlen_opts_help,
                        initial_indent=indent if idx else "",
                        subsequent_indent=" " * (len(i) - len(i.lstrip())),
                        replace_whitespace=False,
                    )
                    hls.append("\n".join([ils[0], *[indent + i for i in ils[1:]]]))
                o_help = "\n".join(hls)
            else:
                o_help = ""

            if o_example:
                o_example_ls = []
                for idx, i in enumerate(o_example.split("\n")):
                    indent = " " * maxlen_type_string
                    if idx:
                        initial_indent = " " * CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR_LEN
                    else:
                        initial_indent = CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR
                    subsequent_indent = " " * (
                        CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR_LEN
                        + len(i)
                        - len(i.lstrip())
                    )
                    ils = wrap(
                        text=i,
                        width=maxlen_opts_help,
                        initial_indent=(" " * maxlen_type_string) + initial_indent,
                        subsequent_indent=subsequent_indent,
                        replace_whitespace=False,
                    )
                    o_example_ls.append(
                        "\n".join([ils[0], *[indent + i for i in ils[1:]]]),
                    )
                o_example = "\n" + "\n".join(o_example_ls)
            else:
                o_example = ""

            return o_type, o_help, o_example

        return inner

    def kwargs_preprocessor(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def inner(**kwargs: dict[str, Any]) -> Any:
            for i in self.cfg["required_options"]:
                if kwargs.get(i) is None:
                    raise exceptions.CLIOptionRequired(i)
            return func(**kwargs)

        inner.__name__ = func.__name__
        return inner

    def wrap(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Wrap given function with corresponding click decorators.

        Args:
        - func (`Callable[..., Any]`): Function to be wrapped.

        Returns:
        `Callable[..., Any]`: Wrapped function.

        """

        self.cmd: CommandSchema = self.command_config[func.__name__]
        self.arguments_cfg = self.cmd.arguments
        wrappers_ls = self.command(), self.arguments(), self.options()
        func = self.kwargs_preprocessor(func)
        for wrapper in wrappers_ls:
            func = wrapper(func)
        return func


def command(
    group: Group,
    command_config: dict[str, CommandSchema],  # type: ignore
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Wrapper for click commands.

    Args:
    - command_config (`dict[str, CommandSchema]`): Command configuration.
    - group (`Group`): Command group of the command to be under.

    Returns:
    - `Callable[[Callable[..., Any]], Callable[..., Any]]`

    """

    return CommandWrapper(command_config, group).wrap

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

import typing
from collections import abc
from collections.abc import Callable, Sequence
from functools import update_wrapper
from textwrap import wrap
from typing import Any, Final, Optional, TypeVar, Union, cast, overload

import click
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
from alltheutils.cli.dataclasses import CommandConfig, CommandSchema
from alltheutils.exceptions import CLICommandNotFound

# Constants
CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR: Final[str] = "Ex.: "
DEFAULT_OPTIONS_KWARGS: Final[dict[str, Any]] = {"metavar": ""}
TERMINAL_CLEARANCE: Final[int] = 10

# Derived Constants
CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR_LEN: Final[int] = len(
    CLICK_CMD_OPTIONS_EXAMPLE_INDICATOR,
)


def show_help(ctx: click.Context, param: click.Parameter, value: str) -> None:
    if value and not ctx.resilient_parsing:
        click.utils.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()


class Command(click.Command):
    def __init__(
        self,
        name: Optional[str],
        context_settings: Optional[dict[str, Any]] = None,
        callback: Optional[Callable[..., Any]] = None,
        params: Optional[list[click.core.Parameter]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: Optional[str] = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
    ) -> None:
        super().__init__(name, context_settings)
        #: the callback to execute when the command fires.  This might be
        #: `None` in which case nothing happens.
        self.callback = callback
        #: the list of parameters for this command in the order they
        #: should show up in the help page and execute.  Eager parameters
        #: will automatically be handled before non eager ones.
        self.name = name
        self.params: list[click.core.Parameter] = params or []
        self.help = help
        self.epilog = epilog
        self.options_metavar = options_metavar
        self.short_help = short_help
        self.add_help_option = add_help_option
        self.no_args_is_help = no_args_is_help
        self.hidden = hidden
        self.deprecated = deprecated

    def format_usage(
        self,
        ctx: click.Context,
        formatter: click.formatting.HelpFormatter,
    ) -> None:
        pieces = self.collect_usage_pieces(ctx)
        formatter.write_usage(self.name or ctx.command_path, " ".join(pieces))

    def get_help_option(self, ctx: click.Context) -> Optional[click.Option]:
        """Returns the help option object."""
        help_options = self.get_help_option_names(ctx)

        if not help_options or not self.add_help_option:
            return None

        return click.Option(
            help_options,
            is_flag=True,
            is_eager=True,
            expose_value=False,
            callback=show_help,
            help="show help",
        )


class MultiCommand(Command):
    allow_extra_args = True
    allow_interspersed_args = False

    def __init__(  # noqa: C901
        self,
        name: Optional[str] = None,
        invoke_without_command: bool = False,
        no_args_is_help: Optional[bool] = None,
        subcommand_metavar: Optional[str] = None,
        chain: bool = False,
        result_callback: Optional[Callable[..., Any]] = None,
        **attrs: Any,
    ) -> None:
        super().__init__(name, **attrs)

        if no_args_is_help is None:
            no_args_is_help = not invoke_without_command

        self.no_args_is_help = no_args_is_help
        self.invoke_without_command = invoke_without_command

        if subcommand_metavar is None:
            if chain:
                subcommand_metavar = "COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]..."
            else:
                subcommand_metavar = "COMMAND [ARGS]..."

        self.subcommand_metavar = subcommand_metavar
        self.chain = chain
        self._result_callback = result_callback

        if self.chain:
            for param in self.params:
                if isinstance(param, click.Argument) and not param.required:
                    raise RuntimeError(
                        "Multi commands in chain mode cannot have"
                        " optional arguments.",
                    )

    def to_info_dict(self, ctx: click.Context) -> dict[str, Any]:
        info_dict = super().to_info_dict(ctx)
        commands = {}

        for name in self.list_commands(ctx):
            command = self.get_command(ctx, name)

            if command is None:
                continue

            sub_ctx = ctx._make_sub_context(command)

            with sub_ctx.scope(cleanup=False):
                commands[name] = command.to_info_dict(sub_ctx)

        info_dict.update(commands=commands, chain=self.chain)
        return info_dict

    def collect_usage_pieces(self, ctx: click.Context) -> list[str]:
        rv = super().collect_usage_pieces(ctx)
        rv.append(self.subcommand_metavar)
        return rv

    def format_options(
        self,
        ctx: click.Context,
        formatter: click.HelpFormatter,
    ) -> None:
        super().format_options(ctx, formatter)
        self.format_commands(ctx, formatter)

    def result_callback(
        self,
        replace: bool = False,
    ) -> Callable[[click.core.F], click.core.F]:
        def decorator(f: click.core.F) -> click.core.F:
            old_callback = self._result_callback

            if old_callback is None or replace:
                self._result_callback = f
                return f

            def function(__value, *args, **kwargs):  # type: ignore
                inner = old_callback(__value, *args, **kwargs)  # type: ignore
                return f(inner, *args, **kwargs)

            self._result_callback = rv = update_wrapper(cast(click.core.F, function), f)
            return rv  # type: ignore

        return decorator

    def format_commands(  # noqa: C901
        self,
        ctx: click.Context,
        formatter: click.HelpFormatter,
    ) -> None:
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            if cmd is None:
                continue
            if cmd.hidden:
                continue

            commands.append((subcommand, cmd))

        if len(commands):
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)

            rows = []
            for subcommand, cmd in commands:
                help = cmd.get_short_help_str(limit)
                rows.append((subcommand, help))

            if rows:
                with formatter.section("Commands"):
                    formatter.write_dl(rows)

    def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]:
        if not args and self.no_args_is_help and not ctx.resilient_parsing:
            click.utils.echo(ctx.get_help(), color=ctx.color)
            ctx.exit()

        rest = super().parse_args(ctx, args)

        if self.chain:
            ctx.protected_args = rest
            ctx.args = []
        elif rest:
            ctx.protected_args, ctx.args = rest[:1], rest[1:]

        return ctx.args

    def invoke(self, ctx: click.Context) -> Any:  # noqa: C901
        def _process_result(value: Any) -> Any:
            if self._result_callback is not None:
                value = ctx.invoke(self._result_callback, value, **ctx.params)
            return value

        if not ctx.protected_args:
            if self.invoke_without_command:
                with ctx:
                    rv = super().invoke(ctx)
                    return _process_result([] if self.chain else rv)
            ctx.fail("Missing command.")

        args = [*ctx.protected_args, *ctx.args]
        ctx.args = []
        ctx.protected_args = []

        if not self.chain:
            with ctx:
                og_args = args
                cmd_name, cmd, args = self.resolve_command(ctx, args)
                if cmd is None:
                    raise CLICommandNotFound(" ".join(og_args))
                ctx.invoked_subcommand = cmd_name
                super().invoke(ctx)
                sub_ctx = cmd.make_context(cmd_name, args, parent=ctx)
                with sub_ctx:
                    return _process_result(sub_ctx.command.invoke(sub_ctx))

        with ctx:
            ctx.invoked_subcommand = "*" if args else None
            super().invoke(ctx)

            contexts = []
            while args:
                cmd_name, cmd, args = self.resolve_command(ctx, args)
                assert cmd is not None
                sub_ctx = cmd.make_context(
                    cmd_name,
                    args,
                    parent=ctx,
                    allow_extra_args=True,
                    allow_interspersed_args=False,
                )
                contexts.append(sub_ctx)
                args, sub_ctx.args = sub_ctx.args, []

            rv = []
            for sub_ctx in contexts:
                with sub_ctx:
                    rv.append(sub_ctx.command.invoke(sub_ctx))
            return _process_result(rv)

    def resolve_command(
        self,
        ctx: click.Context,
        args: list[str],
    ) -> tuple[Optional[str], Optional[Command], list[str]]:
        cmd_name = click.utils.make_str(args[0])
        original_cmd_name = cmd_name

        cmd = self.get_command(ctx, cmd_name)

        if cmd is None and ctx.token_normalize_func is not None:
            cmd_name = ctx.token_normalize_func(cmd_name)
            cmd = self.get_command(ctx, cmd_name)

            if click.parser.split_opt(cmd_name)[0]:
                self.parse_args(ctx, ctx.args)
            ctx.fail("No such command {name!r}.".format(name=original_cmd_name))
        return cmd_name if cmd else None, cmd, args[1:]

    def get_command(self, ctx: click.Context, cmd_name: str) -> Optional[Command]:
        raise NotImplementedError

    def list_commands(self, ctx: click.Context) -> list[str]:
        return []

    def shell_complete(self, ctx: click.Context, incomplete: str):  # type: ignore[no-untyped-def]
        from click.shell_completion import CompletionItem

        results = [
            CompletionItem(name, help=command.get_short_help_str())
            for name, command in click.core._complete_visible_commands(ctx, incomplete)
        ]
        results.extend(super().shell_complete(ctx, incomplete))
        return results


class Group(MultiCommand):
    command_class: Optional[type[Command]] = None
    group_class: Optional[type["Group"] | type[type]] = None

    def __init__(
        self,
        name: Optional[str] = None,
        commands: Optional[Union[dict[str, Command], Sequence[Command]]] = None,
        **attrs: Any,
    ) -> None:
        super().__init__(name, **attrs)

        if commands is None:
            commands = {}
        elif isinstance(commands, abc.Sequence):
            commands = {c.name: c for c in commands if c.name is not None}

        #: The registered subcommands by their exported names.
        self.commands: dict[str, Command] = commands

    def add_command(self, cmd: Command, name: Optional[str] = None) -> None:
        name = name or cmd.name
        if name is None:
            raise TypeError("Command has no name.")
        click.core._check_multicommand(self, name, cmd, register=True)  # type: ignore[arg-type]
        self.commands[name] = cmd

    @overload  # type: ignore[override]
    def command(self, __func: Callable[..., Any]) -> Command: ...

    @overload
    def command(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Callable[[Callable[..., Any]], Command]: ...

    def command(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Callable[[Callable[..., Any]], Command] | Command:
        if self.command_class and kwargs.get("cls") is None:
            kwargs["cls"] = self.command_class

        func: Callable[[Callable[..., Any]], Command] | None = None

        if args and callable(args[0]):
            assert (
                len(args) == 1 and not kwargs
            ), "Use 'command(**kwargs)(callable)' to provide arguments."
            (func,) = args
            args = ()

        def decorator(f: Callable[..., Any]) -> Command:
            cmd: Command = custom_command(*args, **kwargs)(f)
            self.add_command(cmd)
            return cmd

        if func is not None:
            return decorator(func)

        return decorator

    @overload
    def group(self, __func: Callable[..., Any]) -> "Group": ...

    @overload
    def group(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Callable[[Callable[..., Any]], "Group"]: ...

    def group(  # noqa: C901
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Union[Callable[[Callable[..., Any]], "Group"], "Group"]:
        from click.decorators import group

        func: Optional[Callable] = None  # type: ignore[type-arg]

        if args and callable(args[0]):
            assert (
                len(args) == 1 and not kwargs
            ), "Use 'group(**kwargs)(callable)' to provide arguments."
            (func,) = args
            args = ()

        if self.group_class is not None and kwargs.get("cls") is None:
            if self.group_class is type:
                kwargs["cls"] = type(self)
            else:
                kwargs["cls"] = self.group_class

        def decorator(f: Callable[..., Any]) -> "Group":
            cmd: Group = group(*args, **kwargs)(f)
            self.add_command(cmd)
            return cmd

        if func is not None:
            return decorator(func)

        return decorator

    def get_command(self, ctx: click.Context, cmd_name: str) -> Optional[Command]:
        return self.commands.get(cmd_name)

    def list_commands(self, ctx: click.Context) -> list[str]:
        return sorted(self.commands)


class ExtInquirerControl(InquirerControl):  # type: ignore[misc]
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


CmdType = TypeVar("CmdType", bound=Command)


@overload
def custom_command(
    __func: Callable[..., Any],
) -> Command: ...


@overload
def custom_command(
    name: Optional[str] = None,
    **attrs: Any,
) -> Callable[..., Command]: ...


@overload
def custom_command(
    name: Optional[str] = None,
    cls: type[CmdType] = ...,  # type: ignore
    **attrs: Any,
) -> Callable[..., CmdType]: ...


def custom_command(  # noqa: C901
    name: str | Callable[..., Any] | None = None,
    cls: Optional[type[Command]] = None,
    **attrs: Any,
) -> Command | Callable[..., Command]:
    func: Optional[Callable[..., Any]] = None

    if callable(name):
        func = name
        name = None
        assert cls is None, "Use 'command(cls=cls)(callable)' to specify a class."
        assert not attrs, "Use 'command(**kwargs)(callable)' to provide arguments."

    if cls is None:
        cls = Command

    def decorator(f: Callable[..., Any]) -> Command:
        if isinstance(f, Command):
            raise TypeError("Attempted to convert a callback into a command twice.")

        attr_params = attrs.pop("params", None)
        params = attr_params if attr_params is not None else []

        try:
            decorator_params = f.__click_params__  # type: ignore
        except AttributeError:
            pass
        else:
            del f.__click_params__  # type: ignore
            params.extend(reversed(decorator_params))

        if attrs.get("help") is None:
            attrs["help"] = f.__doc__

        cmd = cls(  # type: ignore[misc]
            name=name or f.__name__.lower().replace("_", "-"),  # type: ignore[arg-type]
            callback=f,
            params=params,
            **attrs,
        )
        cmd.__doc__ = f.__doc__
        return cmd

    if func is not None:
        return decorator(func)

    return decorator


def command_group(name: str | Callable[..., Any] | None = None, **attrs: Any) -> Group:
    if attrs.get("cls") is None:
        attrs["cls"] = Group

    if callable(name):
        op: Group = typing.cast(Group, custom_command(**attrs))(name)
        return op

    return typing.cast(Group, custom_command(name, **attrs))


# Base CLI Logic
class CommandWrapper:
    """Returns wrappers for a click command evaluated from the given arguments."""

    def __init__(self, command_config: CommandConfig, group: Group) -> None:
        """
        Initialize object.

        Args:
        - command_config (`CommandConfig`): Command config for initialization of the command.
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
            vh: dict[str, str],
        ) -> tuple[str, str, str]:
            # Primary Variables
            o_type: str = vh["type"]
            o_help: str | None = vh.get("help")
            o_example: str | None = vh.get("example")

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

        self.cmd: CommandSchema = self.command_config.root[func.__name__]
        self.arguments_cfg = self.cmd.arguments
        wrappers_ls = self.command(), self.arguments(), self.options()
        func = self.kwargs_preprocessor(func)
        for wrapper in wrappers_ls:
            func = wrapper(func)
        return func


def command(
    group: Group,
    command_config: CommandConfig,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Wrapper for click commands.

    Args:
    - command_config (`CommandConfig`): Command configuration.
    - group (`Group`): Command group of the command to be under.

    Returns:
    - `Callable[[Callable[..., Any]], Callable[..., Any]]`

    """

    return CommandWrapper(command_config, group).wrap

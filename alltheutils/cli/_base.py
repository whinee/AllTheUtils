from collections.abc import Callable
from typing import Any, Optional

import click


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

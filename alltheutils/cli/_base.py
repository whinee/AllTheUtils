import click


def show_help(ctx: click.Context, param: click.Parameter, value: str) -> None:
    if value and not ctx.resilient_parsing:
        click.utils.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()

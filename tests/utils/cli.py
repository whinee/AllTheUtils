import os
from typing import Any

from alltheutils.cli.base import command, command_group
from alltheutils.config import read_conf_file
from alltheutils.utils import parent_dir_nth_times


@command_group(
    name="test",
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli(**kwargs: dict[str, Any]) -> None:
    """Main command group."""


ccli = command(
    cli,
    read_conf_file(os.path.join(parent_dir_nth_times(__file__, 1), "cmd.yaml")),
)


@ccli
def version():
    with open("dev/version") as f:
        print(f.read().strip())


cli()

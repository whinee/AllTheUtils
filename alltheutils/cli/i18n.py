from collections.abc import Callable
from typing import Any

from alltheutils.exceptions import NewNestedDictExceptions
from alltheutils.instance_config import get_instance_config
from alltheutils.utils import get_value_from_or_update_nested_dict

mapping = {
    "help.overview": "help.overview",
    "help.description": "help.description",
}


def if_key_in_help_texts_put_in_this_location(
    commands_help_texts: dict,
    raw_command_config: dict[str, Any],
) -> Callable[[str, str], None]:
    def inner(cht_key: str, rcc_key: str) -> None:
        try:
            get_value_from_or_update_nested_dict(commands_help_texts, cht_key)
        except NewNestedDictExceptions:
            return
        get_value_from_or_update_nested_dict(
            raw_command_config,
            rcc_key,
            get_value_from_or_update_nested_dict(commands_help_texts, cht_key),
        )

    return inner


def merge_command_config_n_help_text(raw_command_config: dict[str, Any]) -> dict[str, Any]:  # noqa: C901
    commands_help_texts = get_value_from_or_update_nested_dict(
        get_instance_config("language_texts"),
        "cli.commands",
    )

    ikihtpitl = if_key_in_help_texts_put_in_this_location(
        commands_help_texts,
        raw_command_config,
    )

    for key, value in mapping.items():
        ikihtpitl(key, value)

    for command_name, command_value in raw_command_config["commands"].items():
        raw_command_config["commands"][command_name]["help"] = {}
        for key in ["description", "overview"]:
            cht_rcc_key = f"{command_name}.help.{key}"
            ikihtpitl(cht_rcc_key, cht_rcc_key)

        for paramater_type in ["arguments", "options"]:
            for command_options_name in command_value.get(
                paramater_type,
                {},
            ):
                raw_command_config["commands"][command_name][paramater_type][command_options_name]["help"] = {}
                for key in ["help", "example"]:
                    cht_rcc_key = f"{command_name}.{paramater_type}.{command_options_name}.help.{key}"
                    ikihtpitl(cht_rcc_key, cht_rcc_key)

    return raw_command_config

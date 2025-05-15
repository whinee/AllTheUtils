from collections.abc import Callable
from typing import Any

from alltheutils.exceptions import NewNestedDictExceptions
from alltheutils.instance_config import get_instance_config
from alltheutils.utils import get_value_from_or_update_nested_dict

mapping = {
    "help.help": "group_command_params.help",
    "help.epilog": "group_command_params.epilog",
    "help.short_help": "group_command_params.short_help",
}


def if_key_in_help_texts_put_in_this_location(
    commands_help_texts: dict,
    raw_command_config: dict[str, Any],
) -> Callable[[str, str], None]:
    def inner(cht_key: str, rcc_key: str) -> None:

        try:
            value = get_value_from_or_update_nested_dict(commands_help_texts, cht_key)
        except NewNestedDictExceptions:
            return
        get_value_from_or_update_nested_dict(
            raw_command_config,
            rcc_key,
            value,
        )

    return inner


def merge_command_config_n_help_text(  # noqa: C901
    raw_command_config: dict[str, Any],
) -> dict[str, Any]:
    commands_help_texts = get_value_from_or_update_nested_dict(
        get_instance_config("language_texts"),
        "cli",
    )

    ikihtpitl = if_key_in_help_texts_put_in_this_location(
        commands_help_texts,
        raw_command_config,
    )

    for key, value in mapping.items():
        ikihtpitl(key, value)

    for command_name, command_value in raw_command_config["commands"].items():
        get_value_from_or_update_nested_dict(
            raw_command_config,
            f"commands.{command_name}.help",
            {},
        )
        for key in ["description", "overview"]:
            cht_rcc_key = f"commands.{command_name}.help.{key}"
            ikihtpitl(cht_rcc_key, cht_rcc_key)

        for paramater_type in ["arguments", "options"]:
            for command_parameter_name, command_parameter_value in command_value.get(
                paramater_type,
                {},
            ):
                get_value_from_or_update_nested_dict(
                    command_parameter_value,
                    f"commands.{command_name}.{paramater_type}.{command_parameter_name}.help",
                    {},
                )
                for key in ["help", "example"]:
                    cht_rcc_key = f"commands.{command_name}.{paramater_type}.{command_parameter_name}.help.{key}"
                    ikihtpitl(cht_rcc_key, cht_rcc_key)

    return raw_command_config

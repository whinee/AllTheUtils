import json
import os
from collections.abc import Callable
from typing import Any

import yaml

from alltheutils.exceptions import ConfigFileExtensionNotSupported
from alltheutils.utils import yaml_str_presenter


class ParserRegistry:
    def __init__(self) -> None:
        self.parsers: dict[str, dict[str, Callable[[str], Any]]] = {"r": {}, "w": {}}

    def register(self, ext: str | list[str], mode: str, func: Callable[[Any], Any]):
        """
        Register a parser for a given file extension and mode.

        Args:
        - ext (`str`): The file extension (e.g., "yaml", "json").
        - mode (`str`): The mode, either "r" (read) or "w" (write).
        - func (`Callable[[Any], Any]`): The function to handle parsing or dumping.

        Raises:
        `ValueError`: if the mode is not "r" or "w".

        """
        if mode not in self.parsers:
            raise ValueError(f"Invalid mode: {mode}. Use 'r' or 'w'.")

        if isinstance(ext, str):
            self.parsers[mode][ext] = func
        elif isinstance(ext, list) and all(isinstance(e, str) for e in ext):
            for e in ext:
                self.parsers[mode][e] = func
        else:
            raise ValueError(
                f"Invalid extension: {ext}.\nUse a string or a list of strings.",
            )

    def get_parser(self, ext: str, mode: str) -> Callable[[Any], Any]:
        """
        Retrieve a parser function for the given file extension and mode.

        Args:
        - ext (`str`): The file extension (e.g., "yaml", "json").
        - mode (`str`): The mode, either "r" (read) or "w" (write).

        Raises:
        - `ConfigFileExtensionNotSupported`: if no parser is found.

        """
        if ext in self.parsers[mode]:
            return self.parsers[mode][ext]
        raise ConfigFileExtensionNotSupported(ext)


# Custom YAML Presenter
yaml.add_representer(str, yaml_str_presenter)

# Create a global registry instance
registry = ParserRegistry()

# Register YAML parsers
registry.register(["yaml", "yml"], "r", yaml.safe_load)
registry.register(["yaml", "yml"], "w", lambda x: yaml.dump(x, indent=2))

# Register JSON parsers
registry.register("json", "r", json.loads)
registry.register("json", "w", lambda x: json.dumps(x, indent=4, sort_keys=False))


def parse_conf_str(data_str: str, ext: str) -> Any:
    """
    Parses a given string into a dictionary based on the extension.

    Args:
    - data_str (`str`): The string to parse.
    - ext (`str`): The file extension (e.g., "json", "yaml").

    Returns:
    `Any`: The parsed dictionary.

    Raises:
    - `ConfigFileExtensionNotSupported`: if no parser is available.

    """
    parser = registry.get_parser(ext, "r")
    return parser(data_str)


def dump_conf_obj(data: Any, ext: str) -> str:
    """
    Dumps a dictionary into a string based on the extension.

    Args:
    - data (`Any`): The data to serialize.
    - ext (`str`): The file extension (e.g., "json", "yaml").

    Returns:
    - `str`: The serialized data.

    Raises:
    - `ConfigFileExtensionNotSupported`: if no serializer is available.

    """
    serializer = registry.get_parser(ext, "w")
    return serializer(data)


def read_conf_file(file_path: str) -> Any:
    """
    Reads the contents of a file and parses it based on the file extension.

    Args:
    - file_path (`str`): Path to the file.

    Returns:
    - `Any`: Parsed file content.

    Raises:
    - `ConfigFileExtensionNotSupported`: If the file extension is not supported.
    - `FileNotFoundError`: If the file does not exist.

    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, encoding="utf-8") as f:
        return parse_conf_str(f.read(), file_path.split(".")[-1])


def write_to_conf_file(file_path: str, value: Any) -> None:
    """
    Writes data to a file, serializing it based on the file extension.

    Args:
    - file_path (`str`): Path to the file.
    - value (`Any`): Data to write.

    Raises:
    - `ConfigFileExtensionNotSupported`: If the file extension is not supported.

    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(dump_conf_obj(value, file_path.split(".")[-1]))

import json
from typing import Any

import yaml

try:
    from . import types
    from .exceptions import CFGExceptions
    from .utils import yaml_str_presenter
except ImportError:
    from alltheutils import types
    from alltheutils.exceptions import CFGExceptions
    from alltheutils.utils import yaml_str_presenter

TYPES: dict[
    str,
    tuple[
        tuple[str | tuple[str] | tuple[str, str], tuple[str, types.CallableAnyAny]],
        ...,
    ],
] = {
    "r": (
        (("yaml", "yml"), ("r", lambda x: yaml.safe_load(x))),
        (("json"), ("r", lambda x: json.loads(x))),
    ),
    "w": (
        (("yaml", "yml"), ("w", lambda x: yaml.dump(x, indent=2))),
        (("json"), ("w", lambda x: json.dumps(x, indent=4, sort_keys=False))),
    ),
}

yaml.add_representer(str, yaml_str_presenter)


def pcfg(d: str, type: str) -> dict[Any, Any]:
    """
    Parse the given string as the given type.

    Args:
    - d (`str`): String to parse.
    - type (`str`): Type to parse the string as.

    Returns:
    `dict`: The parsed string.
    """

    for k, v in TYPES["r"]:
        if type in k:
            return v[1](d)
    raise CFGExceptions.ExtensionNotSupported(type)


def dcfg(value: dict[str, Any], ext: str) -> str:
    """
    Dump the given value to a string with the given extension.

    Args:
    - value (`dict`): Value to dump to a string.
    - ext (`str`): Extension to dump the value to.

    Returns:
    `str`: The dumped value.
    """

    for k, v in TYPES["w"]:
        if ext in k:
            op: str = v[1](value)
            return op
    raise CFGExceptions.ExtensionNotSupported(ext)


def rcfg(file: str) -> dict[Any, Any]:
    """
    Read the contents of a file with the given file name.

    Args:
    - file (`str`): File name of the file to read the contents of.

    Returns:
    `dict`: The contents of the file.
    """

    ext = file.split(".")[-1]
    for k, v in TYPES["r"]:
        if ext in k:
            with open(file, v[0]) as f:
                return v[1](f.read())
    raise CFGExceptions.ExtensionNotSupported(ext)


def wcfg(file: str, value: dict[Any, Any] | list[Any]) -> None:
    """
    Write the given value to a file with the given file name.

    Args:
    - file (`str`): File name of the file to write the value to.
    - value (`dict[Any, Any] | list[Any])`: Value to write to the file.
    """
    ext = file.split(".")[-1]
    for k, v in TYPES["w"]:
        if ext in k:
            with open(file, v[0]) as f:
                if value.__class__.__mro__[-2] is dict:
                    value = dict(value)
                f.write(v[1](value))

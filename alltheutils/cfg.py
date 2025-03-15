import functools
import warnings
from typing import Any, Optional

from alltheutils.config import (
    dump_conf_obj,
    parse_conf_str,
    read_conf_file,
    write_to_conf_file,
)


# ============================= Top dependencies ===============================
def deprecated(
    version: str,
    replacement: Optional[str] = None,
    reason: Optional[str] = None,
):
    """
    Decorator to mark functions as deprecated.

    Args:
        version (str): The version in which the function will be removed.
        replacement (str, optional): The new function to use instead.

    """

    def decorator(func):
        func_name = func.__name__  # Get function name automatically

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            message = (
                f"{func_name}() is deprecated and will be removed in version {version}."
            )
            if replacement:
                message += f" Use {replacement}() instead."
            if reason:
                message += f" {reason}"
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)  # Pass all arguments properly

        return wrapper

    return decorator


# =========================== Deprecated Functions =============================
@deprecated("3.0.0", "alltheutils.config.parse_conf_str")
def pcfg(d: str, type: str) -> dict[Any, Any]:
    """
    Parse the given string as the given type.

    Args:
    - d (`str`): String to parse.
    - type (`str`): Type to parse the string as.

    Returns:
    `dict`: The parsed string.

    """

    return parse_conf_str(d, type)


@deprecated("3.0.0", "alltheutils.config.parse_conf_str")
def dcfg(value: dict[str, Any], ext: str) -> str:
    """
    Dump the given value to a string with the given extension.

    Args:
    - value (`dict`): Value to dump to a string.
    - ext (`str`): Extension to dump the value to.

    Returns:
    `str`: The dumped value.

    """

    return dump_conf_obj(value, ext)


def rcfg(file: str) -> dict[Any, Any]:
    """
    Read the contents of a file with the given file name.

    Args:
    - file (`str`): File name of the file to read the contents of.

    Returns:
    `dict`: The contents of the file.

    """

    return read_conf_file(file)


def wcfg(file: str, value: dict[Any, Any] | list[Any]) -> None:
    """
    Write the given value to a file with the given file name.

    Args:
    - file (`str`): File name of the file to write the value to.
    - value (`dict[Any, Any] | list[Any])`: Value to write to the file.

    """

    write_to_conf_file(file, value)

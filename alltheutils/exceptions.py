import functools
import warnings
from typing import Any, Optional

from alltheutils import TW
from alltheutils.base_exceptions import (
    CustomBaseException,
    custom_exception,
)
from alltheutils.types import Kwargs

"""
`Common` exceptions are raised if an error occured and it is of the `Common` exception's common variant of error.
"""


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


class GeneralExceptions:
    class ValidationError:
        class FileNotFound(FileNotFoundError, CustomBaseException):
            def __init__(self, fp: str) -> None:
                """
                Raised when a file in a given path is not found.

                Args:
                - parameter (`fp`): Path of the file that can not be found.

                """
                self.message = f"`{fp}` does not exist."

        class Arguments(CustomBaseException):
            def __init__(
                self,
                parameter: str,
                argument: Any,
                specification: str,
                **kwargs: Kwargs,
            ) -> None:
                """
                Raised when a parameter is required to be of specification, but is not followed.

                Args:
                - parameter (`str`): Name of the parameter.
                - argument (`any`): Argument passed to the parameter.
                - specification (`str`): Specification/s of the parameter.

                """
                self.message = f"Argument `{parameter}` needs to {specification}. Instead, passed in the following: {argument}"

        @custom_exception
        class Common(CustomBaseException):
            pass

    class PrerequisiteNotFound(CustomBaseException):
        def __init__(
            self,
            prerequisite: str,
            inst_instruction: Optional[str] = None,
            **kwargs: Kwargs,
        ) -> None:
            """
            Raised when a prerequisite is needed by the program, but is not installed in the machine.

            Args:
            - prerequisite (`str`): Name of the prerequisite.
            - inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.

            """
            self.message = f"prerequisite `{prerequisite}` cannot be found."


class CLIExceptions:
    class TerminalTooThin(CustomBaseException):
        def __init__(self, min_width: int) -> None:
            """
            Raised when terminal is too thin for content to be rendered.

            Args:
            - min_width (`int`): Required minimum terminal width.

            """
            self.message = f"Please widen terminal.\nCurrent Width: {TW}\nMinimum Width: {min_width}"

    class ValidationError:
        class OptionRequired(CustomBaseException):
            def __init__(self, option: str) -> None:
                """
                Raised when an option is required but no argument is passed.

                Args:
                - option (`str`): Required option with no arguments passed into it.

                """
                self.message = f"Option `{option}` is required."

        @custom_exception
        class Common(CustomBaseException):
            pass


class ConfigExceptions:
    class ExtensionNotSupported(NotImplementedError, CustomBaseException):
        def __init__(self, ext: str) -> None:
            """
            Raise when extension `{ext}` is not supported.

            Args:
                ext (`str`): The extension not supported.

            """
            self.message = f"Extension `{ext}` is not supported."


class CFGExceptions:
    @deprecated(
        "3.0.0",
        "alltheutils.exceptions.ConfigExceptions.ExtensionNotSupported",
    )
    class ExtensionNotSupported(NotImplementedError, CustomBaseException):
        def __init__(self, ext: str) -> None:
            self.message = f"Extension `{ext}` is not supported."


class NestedDictExceptions:
    class NonDictReplacementValue(TypeError, CustomBaseException):
        def __init__(self) -> None:
            self.message = "Cannot replace a dict with a non-dict."

    class ValueNotAList(TypeError, CustomBaseException):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[: idx + 1])}' is not a list."

    class ValueNotADict(TypeError, CustomBaseException):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[:idx])}' is not a dict."

    class ValueDoesNotExist(KeyError, CustomBaseException):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = (
                f"Value of path '{'.'.join(keys[: idx + 1])}' does not exist."
            )

    class ValueIsAListAndIndexIsOutOfRange(IndexError, CustomBaseException):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[: idx + 1])}' is a list and index is out of range."

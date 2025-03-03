from typing import Any, Optional

from alltheutils import TW
from alltheutils.base_exceptions import custom_exception, custom_exception_str
from alltheutils.types import Kwargs

"""
`Common` exceptions are raised if an error occured and it is of the `Common` exception's common variant of error.
"""


class GeneralExceptions:
    class ValidationError:
        @custom_exception_str
        class FileNotFound(FileNotFoundError):
            def __init__(self, fp: str, **kwargs: Kwargs) -> None:
                """
                Raised when a file in a given path is not found.

                Args:
                - parameter (`fp`): Path of the file that can not be found.
                """
                self.message = f"`{fp}` does not exist."

        @custom_exception_str
        class Arguments(Exception):
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
        class Common(Exception):
            pass

    @custom_exception_str
    class PrerequisiteNotFound(Exception):
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
    @custom_exception_str
    class TerminalTooThin(Exception):
        def __init__(self, min_width: int, **kwargs: Kwargs) -> None:
            """
            Raised when terminal is too thin for content to be rendered.

            Args:
            - min_width (`int`): Required minimum terminal width.
            """
            self.message = f"Please widen terminal.\nCurrent Width: {TW}\nMinimum Width: {min_width}"

    class ValidationError:
        @custom_exception_str
        class OptionRequired(Exception):
            def __init__(self, option: str, **kwargs: Kwargs) -> None:
                """
                Raised when an option is required but no argument is passed.

                Args:
                - option (`str`): Required option with no arguments passed into it.
                """
                self.message = f"Option `{option}` is required."

        @custom_exception
        class Common(Exception):
            pass


class CFGExceptions:
    @custom_exception_str
    class ExtensionNotSupported(NotImplementedError):
        def __init__(self, ext: str, **kwargs: Kwargs) -> None:
            self.message = f"Extension `{ext}` is not supported."


class NestedDictExceptions:
    @custom_exception_str
    class NonDictReplacementValue(TypeError):
        def __init__(self) -> None:
            self.message = "Cannot replace a dict with a non-dict."

    @custom_exception_str
    class ValueNotAList(TypeError):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[: idx + 1])}' is not a list."

    @custom_exception_str
    class ValueNotADict(TypeError):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[:idx])}' is not a dict."

    @custom_exception_str
    class ValueDoesNotExist(KeyError):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = (
                f"Value of path '{'.'.join(keys[: idx + 1])}' does not exist."
            )

    @custom_exception_str
    class ValueIsAListAndIndexIsOutOfRange(IndexError):
        def __init__(self, keys: list[str], idx: int) -> None:
            self.message = f"Value of path '{'.'.join(keys[: idx + 1])}' is a list and index is out of range."

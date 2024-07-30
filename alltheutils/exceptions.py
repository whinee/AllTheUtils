from typing import Any, Optional

try:
    from . import TW
    from .base_exc import c_exc, c_exc_str
    from .types import Kwargs
except ImportError:
    from alltheutils import TW
    from alltheutils.base_exc import c_exc, c_exc_str
    from alltheutils.types import Kwargs

"""
`Common` exceptions are raised if an error occured and it is of the `Common` exception's common variant of error.
"""


class GeneralExceptions:
    class ValidationError:
        @c_exc_str
        class FileNotFound(FileNotFoundError):
            def __init__(self, fp: str, **kwargs: Kwargs) -> None:
                """
                Raised when a file in a given path is not found.

                Args:
                - parameter (`fp`): Path of the file that can not be found.
                """
                self.message = f"`{fp}` does not exist."

        @c_exc_str
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

        @c_exc
        class Common(Exception):
            pass

    @c_exc_str
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
    @c_exc_str
    class TerminalTooThin(Exception):
        def __init__(self, min_width: int, **kwargs: Kwargs) -> None:
            """
            Raised when terminal is too thin for content to be rendered.

            Args:
            - min_width (`int`): Required minimum terminal width.
            """
            self.message = f"Please widen terminal.\nCurrent Width: {TW}\nMinimum Width: {min_width}"

    class ValidationError:
        @c_exc_str
        class OptionRequired(Exception):
            def __init__(self, option: str, **kwargs: Kwargs) -> None:
                """
                Raised when an option is required but no argument is passed.

                Args:
                - option (`str`): Required option with no arguments passed into it.
                """
                self.message = f"Option `{option}` is required."

        @c_exc
        class Common(Exception):
            pass


class CDExceptions:
    class API:
        class KeyError:
            @c_exc_str
            class NotInElement(KeyError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = (
                        f"`{sep.join(og_path.split(sep)[:idx])}` not in element"
                    )

        class TypeError:
            @c_exc_str
            class KeyNotStrOrInt(TypeError):
                def __init__(self, tc: type, **kwargs: Kwargs) -> None:
                    self.message = f"Expected key to be of type `int` or `str`, but instead got `{tc.__name__}`."

            @c_exc_str
            class CurrentElementNotDict(TypeError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    tc: type,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "indexed element expected to be of type `dict`"
                    self.details = f"`{sep.join(og_path.split(sep)[:idx])}` expected to be of type `dict`, instead was `{tc.__name__}`"

            @c_exc_str
            class CurrentElementNotListOrTuple(TypeError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    tc: type,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "indexed element expected as sized iterable"
                    self.details = f"`{sep.join(og_path.split(sep)[:idx])}` expected as a sized iterable, instead was `{tc.__name__}`"

            @c_exc_str
            class CurrentElementNotDictListOrTuple(TypeError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    tc: type,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "indexed element expected to be of type `dict` or as sized iterable"
                    self.details = f"`{sep.join(og_path.split(sep)[:idx])}` expected as a dictionary or a sized iterable, instead was `{tc.__name__}`"

        class IndexError:
            @c_exc_str
            class EmptyString(IndexError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    tc: type,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "index expected as an integer"
                    self.details = f"`{sep.join(og_path.split(sep)[:idx])}`'s indexed element is a sized iterable (type {tc.__name__}); expected index to be an integer, but instead was an empty string."

            @c_exc_str
            class NotInteger(IndexError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    tc: type,
                    key: Any,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "index expected as an integer"
                    self.details = f"`{sep.join(og_path.split(sep)[:idx])}` is a sized iterable (type {tc.__name__}); index expected to be an integer, but instead was set to `{key}`."

            @c_exc_str
            class OutOfRange(IndexError):
                def __init__(
                    self,
                    sep: str,
                    og_path: str,
                    idx: int,
                    ls_idx: int,
                    len_iter: int,
                    **kwargs: Kwargs,
                ) -> None:
                    self.message = "sized iterable index out of range"
                    self.details = f"""`{sep.join(og_path.split(sep)[:idx])}`:
                    Index is `{ls_idx}` while the length of the sized iterable is only `{len_iter}`.
                    The index should fulfill the following condition:
                    (len(iter)) > idx > (-1 - len(iter))

                    The index should be less than the length of the sized iterable OR more than the difference of negative 1 and the length of the sized iterable."""

    class Internals:
        @c_exc_str
        class StateUnexpected(IndexError):
            def __init__(self, state: Any, max_state: int, **kwargs: Kwargs) -> None:
                """
                Raised when the state passed in between functions is not of type `int` or exceeds the bounds of possible states.

                Args:
                - state (`Any`): Faulty state.
                - max_state (`Optional[str]`): Maximum integer for state.
                """
                self.message = "state index out of range"
                self.details = f"""Passed state is `{state}` while the max integer for state is `{max_state}`.
                The index should fulfill the following condition:
                - State should be an integer
                - State should be more than `-1` or less than `{max_state + 1}`"""


class CFGExceptions:
    @c_exc_str
    class ExtensionNotSupported(NotImplementedError):
        def __init__(self, ext: str, **kwargs: Kwargs) -> None:
            self.message = f"Extension `{ext}` is not supported."

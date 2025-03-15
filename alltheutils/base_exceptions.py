import functools
import sys
import warnings
from collections.abc import Callable
from types import TracebackType
from typing import Optional

from alltheutils import types


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


class CustomBaseException(BaseException):
    """Base class for all custom exceptions."""

    message: str
    details: Optional[str] = None

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message

    def print_details(self) -> None:
        if self.details:
            print(self.details)


@deprecated(
    "3.0.0",
    reason="Inherit the custom exception class from `alltheutils.exceptions.CustomBaseException` instead, alongside any inherited exception/s.",
)
def custom_exception_str(cls: type[BaseException]) -> type[BaseException]:
    """
    Decorator to add the __str__ method to an exception.

    Args:
    - cls (`BaseException`): The exception to add the __str__ method to.

    Returns:
    `BaseException`: The exception to raise.

    """

    old_init: Callable[..., None] = cls.__init__

    def init_fn(
        self: type[BaseException],
        *args: types.Args,
        **kwargs: types.Kwargs,
    ) -> None:
        old_init(self, *args, **kwargs)  # type: ignore

    def str_fn(self: type[BaseException]) -> str:
        return self.message  # type: ignore

    def print_details_fn(self: BaseException) -> None:
        if details := getattr(self, "details", None):
            print(details)

    cls.__init__ = init_fn  # type: ignore[assignment]
    cls.__str__ = str_fn  # type: ignore[assignment]
    cls.print_details = print_details_fn  # type: ignore
    return cls


def custom_exception(cls: type[CustomBaseException]) -> type[CustomBaseException]:
    """
    Decorator to raise a custom exception.

    This function gives the class an __init__ function that raises the exception.
    If the class does not inherit from any Exception, it will be automatically inherit from Exception.
    This function also wraps the Exception with `c_exc_str` method, for adding the `__str__` method.

    Args:
    - cls (`BaseException | Object`): The exception to modify.

    Returns:
    `BaseException`: The exception to raise.

    """
    if cls.__mro__[-2] is BaseException:
        exc = cls.__mro__[1]
    else:
        exc = Exception

    def init(
        self: type[BaseException],
        message: str,
        details: Optional[str] = None,
    ) -> None:
        self.message = message  # type: ignore
        if details is not None:
            self.details = details  # type: ignore
        exc(self.message)  # type: ignore

    cls.__init__ = init  # type: ignore[assignment]
    return cls


def custom_exception_hook(
    exctype: type[CustomBaseException],
    value: CustomBaseException,
    traceback: Optional[TracebackType],
) -> None:
    sys.__excepthook__(exctype, value, traceback)
    if hasattr(value, "print_details"):
        value.print_details()


sys.excepthook = custom_exception_hook  # type: ignore[assignment]

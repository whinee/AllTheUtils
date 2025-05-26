import sys
from types import TracebackType
from typing import Optional


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

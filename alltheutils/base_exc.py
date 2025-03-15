import functools
import warnings
from typing import Optional

from alltheutils.base_exceptions import custom_exception, custom_exception_str


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
@deprecated("3.0.0", "alltheutils.base_exceptions.custom_exception_str")
def c_exc_str(cls: type[BaseException]) -> type[BaseException]:
    """
    Decorator to add the __str__ method to an exception.

    Args:
    - cls (`BaseException`): The exception to add the __str__ method to.

    Returns:
    `BaseException`: The exception to raise.

    """
    return custom_exception_str(cls)


@deprecated("3.0.0", "alltheutils.base_exceptions.custom_exception")
def c_exc(cls: type[BaseException]) -> type[BaseException]:
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
    return custom_exception(cls)  # type: ignore

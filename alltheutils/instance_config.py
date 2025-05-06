import functools
from typing import Any

from alltheutils.exceptions import (
    MissingInstanceConfigValue,
)

_INSTANCE_CONFIG: dict[str, Any] = {}


def set_instance_config(key, value):
    _INSTANCE_CONFIG[key] = value


def get_instance_config(key):
    return _INSTANCE_CONFIG[key]


def has_instance_config(key):
    return key in _INSTANCE_CONFIG


def clear_instance_config():
    _INSTANCE_CONFIG.clear()


def requires_instance_config(*keys):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            missing_constants = [k for k in keys if not has_instance_config(k)]
            if missing_constants:
                raise MissingInstanceConfigValue(func.__name__, missing_constants)

            injected_kwargs = {k: get_instance_config(k) for k in keys}
            return func(
                *args,
                **{**injected_kwargs, **kwargs},
            )  # user-supplied kwargs override if needed

        return wrapper

    return decorator

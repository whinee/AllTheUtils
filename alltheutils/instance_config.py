from typing import Any

_INSTANCE_CONFIG: dict[str, Any] = {}


def set_instance_config(key, value):
    _INSTANCE_CONFIG[key] = value


def get_instance_config(key):
    return _INSTANCE_CONFIG[key]


def has_instance_config(key):
    return key in _INSTANCE_CONFIG


def clear_instance_config():
    _INSTANCE_CONFIG.clear()

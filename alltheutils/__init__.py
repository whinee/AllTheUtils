import platform
from shutil import get_terminal_size
from sys import platform as PLATFORM

DEFAULT_STR = "c0VjUmVUX2NPZEUgYnkgd2hpX25l"

MACHINE = platform.machine()

match PLATFORM:
    case "win32":
        PSH = "win"
        """Platform Short Hand"""
    case "darwin":
        PSH = "mac"
    case _:
        PSH = PLATFORM

try:
    TW = get_terminal_size().columns
    """Stands for terminal width.
    """
except OSError:
    TW = 0

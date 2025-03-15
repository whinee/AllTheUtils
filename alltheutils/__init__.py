import platform
import warnings
from shutil import get_terminal_size
from sys import platform as PLATFORM

warnings.simplefilter("always")

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

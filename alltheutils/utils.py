import ast
import difflib
import functools
import hashlib
import inspect
import itertools
import os
import re
import shlex
import shutil
import sys
import unicodedata
import warnings
from collections.abc import Callable, Generator, Iterable, Sized
from datetime import datetime, timezone
from itertools import cycle
from multiprocessing import Pool, pool
from os import makedirs
from os.path import dirname
from re import Pattern
from subprocess import call
from typing import Any, Final, Optional

from alltheutils import PSH, types
from alltheutils.exceptions import (
    FileNotFound,
    NDNonDictReplacementValue,
    NDValueDoesNotExist,
    NDValueIsAListAndIndexIsOutOfRange,
    NDValueNotADict,
    NDValueNotAList,
)

# ================================ Constants ===================================
PR = ["alpha", "beta", "rc"]  # Prerelease strings
CATEGORIES: Final[set[str]] = {"Cn"}

# ============================ Derived Constants ===============================
ALL_CHARS: Final[Generator[str, None, None]] = (chr(i) for i in range(sys.maxunicode))
CCHARS: Final[str] = "".join(
    map(chr, itertools.chain(range(0x20), range(0x7F, 0xA0))),
)
CCHARS_RE: Final[Pattern[str]] = re.compile("[{}]".format(re.escape(CCHARS)))  # type: ignore


# ================================= Classes ====================================
class PoolTerminate:
    def __init__(self, pool: pool.Pool, callback: types.CallableAny) -> None:
        self.called = False
        self.pool = pool
        self.callback = callback

    def inner(self, err: bool, *args: types.Args, **kwargs: types.Kwargs) -> None:
        if err and (not self.called):
            self.called = True
            self.pool.terminate()
            self.callback(*args, **kwargs)


class CallbackGetResult:
    def __init__(self) -> None:
        self.args: tuple[None] | tuple[Any, ...] = ()

    def callback(self, *args: types.Args) -> None:
        self.args = args

    def get(self) -> tuple[None] | tuple[Any, ...]:
        return self.args


# ============================= Top dependencies ===============================
def deprecated(
    version: str,
    replacement: Optional[str] = None,
    reason: Optional[str] = None,
):
    """
    Decorator to mark functions as deprecated.

    Args:
    - version (`str`): The version in which the function will be removed.
    - replacement (`str`, optional): The new function to use instead.
    - reason (`str`, optional): Reason for deprecation. Defaults to None.

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


def deprecated_class(
    version: str,
    replacement: Optional[str] = None,
    reason: Optional[str] = None,
):
    """
    Decorator to mark a classes as deprecated.

    Args:
    - version (`str`): The version in which the exception will be removed.
    - replacement (`str`, optional): The new exception to use instead.
    - reason (`str`, optional): Additional reason for deprecation.

    """

    def decorator(cls):
        orig_init = cls.__init__

        @functools.wraps(orig_init)
        def new_init(self, *args, **kwargs):
            message = f"{cls.__name__} is deprecated and will be removed in version {version}."
            if replacement:
                message += f" Use {replacement} instead."
            if reason:
                message += f" {reason}"

            warnings.warn(message, DeprecationWarning, stacklevel=2)
            orig_init(self, *args, **kwargs)  # Pass all arguments properly

        cls.__init__ = new_init
        return cls

    return decorator


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp_qir",
    "This is probably broken anyways.",
)
def run_mp_qir(
    func: types.CallableAny,
    iterable: types.IterAny,
    callback: types.CallableAny,
) -> None:
    """
    Run `multiprocessing.Pool().map_async()`, and quit in return.

    Iterate over `iterable` and apply iterated item to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

    This function requires the given function to return a bool, or an iterable with its first item as a bool. This bool is then used to decide whether to trigger the callback and terminate the pool.

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterAny`): Iterable containing items to iterate over and pass to `func`.
    - callback (`types.CallableAny`): Function to be called when a process in the pool returns.

    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        for i in iterable:
            pool.apply_async(
                func,
                args=(i,),
                callback=PoolTerminate(pool, callback).inner,
            )
        pool.close()
        pool.join()


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp_star_qir",
    "This is probably broken anyways.",
)
def run_mp_star_qir(
    func: types.CallableAny,
    iterable: types.IterIterAny,
    callback: types.CallableAny,
) -> None:
    """
    Run `multiprocessing.Pool().starmap_async()`, and quit in return.

    Iterate over `iterable` and apply iterated items to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.
    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        for i in iterable:
            pool.apply_async(func, args=i, callback=PoolTerminate(pool, callback).inner)
        pool.close()
        pool.join()


# ================================ Functions ===================================
def batch_replace(text: str, key_value_map: dict[str, list[str]]) -> str:
    """
    Iterate through the dictionary, find the values in the given string and replace it with the corresponding key, and output the modified string.

    Args:
    - text (`str`): String to modify the contents of.
    - key_value_map (`dict[str, list[str]]`): Key-value pairs of string to replace the substring with and list of string to replace with the corresponding key.

    Returns:
    `str`: Modified string.

    """
    for k, v in key_value_map.items():
        if v:
            for i in v:
                text = text.replace(i, k)
    return text


def calculate_sha256_hash(input: str) -> str:
    """
    Given a string, calculate its hash and return it.

    Args:
    - input (str): String to hash.

    Returns:
    `str`: Hash of the string.

    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input.encode("utf-8"))
    return sha256_hash.hexdigest()


def caller_relative_path(relative_path: str, idx: Optional[int] = None) -> str:
    """
    Given a path, output the same path, relative to the absolute directory path of the file that invoked this function.

    An optional argument `idx` can be supplied to change what script to get the absolute directory path from. Consider the following scenario:

    A helper function in `src/utils` that takes in a relative path as an argument wants to transform the path into one relative to the caller's path. However, the said function needs to call this function directly. Said function can then use an index of `2` so that the given path to this function will be processed to be relative from the caller's path, not from the funciton in `src/utils/utils`.

    Args:
    - relative_path (`str`): Path to output relative to the caller's path.
    - idx (`Optional[int]`, optional): Index of the stack to relativize the path from. Defaults to `1`.

    Returns:
    `str`: Path relative to the caller's path.

    """
    if idx is None:
        idx = 1
    return os.path.normpath(
        os.path.join(os.path.dirname(inspect.stack()[idx][1]), relative_path),
    )


def custom_version_ls_to_str(
    vls: list[str | int] | list[int] | list[str],
) -> tuple[str, str]:
    """
    Given the list of custom version numbers, convert them to their string representation both in modified semver form and semver-compliant form.

    Args:
    - vls (`list[str | int]`): List of version numbers.

    Returns:
    `tuple[str, str]`: List of string representation of given list of version numbers, both in modified semver form and semver-compliant form.

    """
    pr = ""
    ivls = [int(i) for i in vls]
    if ivls[4] < 3:
        pr = f"-{PR[ivls[4]]}.{ivls[5]}"
    return (
        ".".join([str(i) for i in ivls[0:4]]) + pr,
        ".".join([str(i) for i in [*ivls[0:2], 3 ** ivls[2] * 2 ** ivls[3]]]) + pr,
    )


def dict_get_first_match(
    dictionary: dict[Any, Any],
    keys: list[int | list[str | int | tuple[str, ...]] | str],
    default_value: Optional[Any] = None,
) -> Any:
    """
    Iterate through the `keys` and see if the value exists in the `dictionary`. First one that exists will be returned. If none exists, return `default_value`.

    Args:
    - dictionary (`dict[Any, Any]`): Dictionary to retrieve the value from.
    - keys (`list[int | tuple[str | int | tuple] | str]`): List of keys to iterate through.
    - default_value (`Any`, optional): Default object to be returned. Defaults to None.

    Returns:
    `Any`: Retrieved value.

    """

    for i in keys:
        if op := dictionary.get(i):
            return op
    return default_value


def ensure_parent_dir(
    file_path: str,
    make_dir_append_to_ls: Optional[list[str]] = None,
) -> str:
    """
    If the directory of the file path does not exist, then make it.

    Args:
    - file_path (`str`): File path to check if it is a directory, and if not, to make one of the same name.
    - ls (`Optional[list[str]]`, optional): A list of string to which this function can append the file path to if the given file path is not a directory. Defaults to `None`.

    Returns:
    `str`: Given filepath.

    """

    pd = os.path.dirname(file_path)
    if (pd) and (not os.path.isdir(pd)):
        makedirs(pd)
        if make_dir_append_to_ls:
            make_dir_append_to_ls.append(pd)
    return file_path


def file_exists(fp: str) -> str:
    """
    Check if the given file path exists.

    Args:
    - fp (`str`): File path to check if it exists.

    Raises:
    - `alltheutils.exceptions.FileNotFound`: Raised when a file in the path is not found.

    Returns:
    `str`: Return `fp` when file path exists.

    """
    if not os.path.exists(fp):
        raise FileNotFound(fp)
    return fp


def fill_ls(
    *,
    ls: types.SequenceAny,
    length: int,
    filler: Optional[Any] = None,
) -> types.SequenceAny:
    """
    Fill given list (`ls`) with `filler` up to `length`.

    Args:
    - ls (`types.SequenceAny`): List to fill with `filler` up to `length`
    - length (`int`): Length of the list to achieve.
    - filler (`Optional[Any]`, optional): Filler to use. Defaults to `None`.

    Returns:
    `types.SequenceAny`: Filled list.

    """
    lls = len(ls)
    if lls < length:
        return ls

    return [*ls, *[filler for _ in range(length - lls)]]


def first_not_none_in_ls(ls: types.ListOptionalAny) -> Any:
    """
    Return First Non-None.

    Return the first argument that is not `None`, else return `None`.

    Args:
    - ls (`types.ListAny`): List of objects to check.

    Returns:
    `Any`: The first argument that is not `None`, else `None`.

    """
    for i in ls:
        if i is not None:
            return i


def flatten_element(  # noqa: C901
    elem: dict[Any, Any],
    sep: str = "/",
) -> dict[Any, Any]:
    flattened_dict = {}
    stack = [(elem, "")]

    while stack:
        current_elem, parent_key = stack.pop(0)

        if isinstance(current_elem, list) or isinstance(current_elem, tuple):
            for i, item in enumerate(current_elem):
                item_key = str(i)
                new_key = f"{parent_key}{sep}{item_key}" if parent_key else item_key
                if isinstance(item, dict):
                    stack.append((item, new_key))
                else:
                    flattened_dict[new_key] = item
        elif isinstance(current_elem, dict):
            for key, value in current_elem.items():
                if not isinstance(key, int) and not isinstance(key, str):
                    raise TypeError(
                        f"Expected key to be of type `int` or `str`, but instead got `{type(key).__name__}`.",
                    )
                new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)

                if isinstance(value, dict):
                    stack.append((value, new_key))
                elif isinstance(value, list) or isinstance(value, tuple):
                    for i, item in enumerate(value):
                        item_key = f"{new_key}{sep}{i}"
                        flattened_dict[item_key] = item
                else:
                    flattened_dict[new_key] = value

    return flattened_dict


def get_value_from_or_update_nested_dict(  # noqa: C901
    data: types.RecursiveDict,
    address: str,
    new_value: int | types.RecursiveDict | str | None = None,
):
    """
    Updates or retrieves a nested dictionary value at the given dot-separated address.

    - If `new_value` is provided, updates the value.
    - If `new_value` is `None`, returns the current value at `address`.
    """
    if not address or address == ".":
        if new_value is None:
            return data  # Return the whole dictionary if no update
        if isinstance(new_value, dict):
            if new_value:
                data.clear()
                data.update(new_value)
            return data
        raise NDNonDictReplacementValue

    keys = address.split(".")
    current = data

    for idx, key in enumerate(keys):
        new_key: int | str = key
        start_key = key[:4]
        if start_key in ["int>", "str>"]:
            new_key = key[4:]
            if start_key == "int>" and new_key.isdigit():
                new_key = int(new_key)

        is_dict = isinstance(current, dict)

        if isinstance(new_key, int):
            if new_key not in current and not isinstance(current, list):
                raise NDValueNotAList(keys, idx)
            is_dict = False
        elif not is_dict:
            raise NDValueNotADict(keys, idx)

        if idx == len(keys) - 1:
            if new_value is None:
                if new_key in current:
                    return current[new_key]  # type: ignore
                raise NDValueDoesNotExist(keys, idx)
            current[new_key] = new_value  # type: ignore
        else:
            # Navigate deeper, create dicts if missing
            if is_dict:
                current = current.setdefault(new_key, {})  # type: ignore
            else:
                len_current = len(current)
                new_key_int: int = new_key  # type: ignore
                if new_key not in current:
                    current = current[new_key_int]
                elif len(current) <= new_key_int or new_key_int < (0 - len_current):
                    raise NDValueIsAListAndIndexIsOutOfRange(
                        keys,
                        idx,
                    )

    return data


def if_none(variable: Any, default: Any) -> Any:
    """
    "If variable is None, then return the default".

    If `variable` is `None`, return `default` else `var`.

    Args:
    - variable (`Any`): Variable to check if it is None.
    - default (`Any`): Default value to return if var is None.

    Returns:
    `Any`: `variable` if `variable` is not None else `default`.

    """
    if variable is None:
        return default
    return variable


def iter_ls_with_items(
    ls: types.ListAny,
    *items: types.ListAny,
) -> Generator[tuple[Any, ...], None, None]:
    for i in ls:
        yield i, *items


def literal_eval(expr: Optional[str]) -> Any:
    """
    Literal Evaluation.

    Args:
    - expr (`Optional[str]`): Expression to be evaluated.

    Returns:
    `Any`: Expression literally evaluated.

    """
    if expr is not None:
        return ast.literal_eval(expr)


def noop(*args: types.ListAny, **kwargs: dict[str, Any]) -> None:
    """No operation."""


def noop_single_kwargs(arg: Any) -> Any:
    return arg


def parent_dir_nth_times(filename: str, n: Optional[int] = None) -> str:
    """
    Dirname N-th times.

    Given a file name and a number, find the parent directory of the given filename as many times as the given number.

    Args:
    - filename (`str`): The filename to find the parent directory of.
    - n (`int`): How many times the parent directory of the given filename should be found.

    Returns:
    `str`: Parent directory of the given filename.

    """
    op = filename
    for _ in range(n or 1):
        op = dirname(op)
    return op


def run_cmd(cmd: str) -> None:
    """
    Given a string, execute it as a shell command.

    Args:
    - cmd (`str`): Shell command to excute.

    """
    call(shlex.split(cmd))  # noqa: S603


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp",
    "This is probably broken anyways.",
)
def run_mp(func: types.CallableAny, iterable: types.IterAny) -> types.ListAny:
    with Pool() as pool:
        return pool.map(func, iterable)


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp_qgr",
    "This is probably broken anyways.",
)
def run_mp_qgr(func: types.CallableAny, iterable: types.IterAny) -> types.TupleAny:
    res_cb = CallbackGetResult()
    run_mp_qir(func, iterable, res_cb.callback)
    return res_cb.get()


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp_star",
    "This is probably broken anyways.",
)
def run_mp_star(func: types.CallableAny, iterable: types.IterIterAny) -> types.ListAny:
    with Pool() as pool:
        return pool.starmap(func, iterable)


@deprecated(
    "3.0.0",
    "alltheutils.multi_processing.run_mp_star_qgr",
    "This is probably broken anyways.",
)
def run_mp_star_qgr(
    func: types.CallableAny,
    iterable: types.IterIterAny,
) -> types.TupleAny:
    res_cb = CallbackGetResult()
    run_mp_star_qir(func, iterable, res_cb.callback)
    return res_cb.get()


def sanitize_text(s: str) -> str:
    """
    Sanitize input text.

    Reference: https://stackoverflow.com/a/93029

    Args:
    - s (`str`): Text to be sanitized.

    Returns:
    `str`: Sanitized text.

    """

    if isinstance(s, str):
        return unicodedata.normalize("NFKD", CCHARS_RE.sub("", s)).strip()


def search_query(
    query: str,
    possibilities: list[str],
    cutoff: int | float = 0.6,
    *,
    processor: Callable[[Any], Any] = lambda x: x,
) -> Generator[tuple[None, str] | tuple[float, str], None, None]:
    """
    Custom search query.

    Args:
    - query (`str`): String to search for in the possibilities.
    - possibilities (`list[str]`): The possibilities to search from.
    - cutoff (`int | float`, optional): The minimum percentage of similarity from the given possibilities. Defaults to `0.6`.
    - processor (`Callable[[Any], Any]`, optional): Processes the possibilities before comparing it with the query. Defaults to `lambda x: x`.

    Returns:
    `Generator[tuple[None, str] | tuple[float, str], None, None]`: Generator object of mastching search quries.

    """

    sequence_matcher = difflib.SequenceMatcher()
    sequence_matcher.set_seq2(query)

    for search_value in possibilities:
        sequence_matcher.set_seq1(processor(search_value))
        if query.lower() in processor(search_value).lower():
            yield (None, search_value)
            continue
        if (
            sequence_matcher.real_quick_ratio() >= cutoff
            and sequence_matcher.quick_ratio() >= cutoff
            and sequence_matcher.ratio() >= cutoff
        ):
            yield (sequence_matcher.ratio(), search_value)


def str2int(num: int | str) -> Optional[int]:
    """
    If given number is int, return it. Else, if given number is string and is decimal, convert string to integer. Otherwise, return None.

    Args:
    - s (`int | str`): int or string to convert to integer.

    Returns:
    `Optional[int]`: If given argument can be converted to integer, it will be returned. Otherwise, None will be.

    """
    if isinstance(num, int):
        return num
    if (len(num) != 0) and (num[0] in ("-", "+")) and (num[1:].isdecimal()):
        return int(num)
    if num.isdecimal():
        return int(num)
    return None


def unix_timestamp_to_iso(timestamp: int) -> str:
    """
    Convert the given unix timestamp to ISO 8601 format.

    Args:
    - ts (`int`): unix timestamp to be converted to ISO 8601 format

    Returns:
    `str`: Formatted datetime string

    """

    return datetime.fromtimestamp(timestamp, tz=timezone.UTC).strftime(  # type: ignore
        "%Y-%m-%dT%H:%M:%S",
    )


def which_ls(  # noqa: C901
    cmd: str,
    mode: Optional[int] = None,
    path: Optional[str] = None,
) -> Optional[types.TupleStr]:
    """
    Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH, or None if there is no such file. Yoinked from shutil.

    Args:
    - mode (`int`, optional): File mode to look for. Defaults to `os.F_OK | os.X_OK`.
    - path (`str`, optional): Path to search the command at. Defaults to the result of os.environ.get("PATH").

    Returns:
    `Optional[types.TupleStr]`: Tuple of commands that conforms to the given arguments as said above.

    """

    if mode is None:
        mode = os.F_OK | os.X_OK

    # If we're given a path with a directory part, look it up directly rather
    # than referring to PATH directories. This includes checking relative to the
    # current directory, e.g. ./script
    if os.path.dirname(cmd):
        if shutil._access_check(cmd, mode):  # type: ignore
            return (cmd,)
        return None

    if path is None:
        path = os.environ.get("PATH", None)
        if path is None:
            try:
                path = os.confstr("CS_PATH")
            except (AttributeError, ValueError):
                # os.confstr() or CS_PATH is not available
                path = os.defpath
        # bpo-35755: Don't use os.defpath if the PATH environment variable is
        # set to an empty string

    # PATH='' doesn't match, whereas PATH=':' looks in the current directory
    if not path:
        return None

    path = os.fsdecode(path).split(os.pathsep)  # type: ignore[assignment]

    if PSH == "win":
        curdir = os.curdir
        if curdir not in path:  # type: ignore
            path.insert(0, curdir)  # type: ignore

        # PATHEXT is necessary to check on Windows.
        pathext_source = os.getenv("PATHEXT") or shutil._WIN_DEFAULT_PATHEXT  # type: ignore
        pathext = [ext for ext in pathext_source.split(os.pathsep) if ext]

        # See if the given file matches any of the expected path extensions.
        # This will allow us to short circuit when given "python.exe".
        # If it does match, only test that one, otherwise we have to try
        # others.
        if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
            files = [cmd]
        else:
            files = [cmd + ext for ext in pathext]
    else:
        # On other platforms you don't have things like PATHEXT to tell you
        # what file suffixes are executable, so just pass on cmd as-is.
        files = [cmd]

    seen = set()
    op = set()
    for dir in path:
        normdir = os.path.normcase(dir)
        if normdir not in seen:
            seen.add(normdir)
            for thefile in files:
                name = os.path.join(dir, thefile)
                if shutil._access_check(name, mode):  # type: ignore
                    op.add(name)
    return tuple(op)


def yaml_str_presenter(dumper, data):  # type: ignore[no-untyped-def]
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def zip_extend(a: Sized, b: Sized) -> Iterable[Any]:
    """
    Given two list, iterate through both of them, and cycle the shorter list until the longer list has been exhausted.

    Args:
    - a (`Sized`): First sized iterable.
    - b (`Sized`): Second sized iterable.

    Returns:
    `Iterable[Any]`: Zipped extended iterable.

    """
    if len(a) > len(b):
        return zip(a, cycle(b), strict=False)  # type: ignore[arg-type, call-overload, no-any-return]
    return zip(cycle(a), b, strict=False)  # type: ignore[arg-type, call-overload, no-any-return]

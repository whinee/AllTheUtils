# <h1 id="module-alltheutilsutils"><a href="#module-alltheutilsutils">Module alltheutils.utils</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="batch_replace"><a href="#batch_replace">`batch_replace`</a></h3>
```python
(text: str, key_value_map: dict[str, list[str]]) → str
```

Iterate through the dictionary, find the values in the given string and replace it with the corresponding key, and output the modified string.

Args:
- text (`str`): String to modify the contents of.
- key_value_map (`dict[str, list[str]]`): Key-value pairs of string to replace the substring with and list of string to replace with the corresponding key.

Returns:
`str`: Modified string.

<h3 id="calculate_sha256_hash"><a href="#calculate_sha256_hash">`calculate_sha256_hash`</a></h3>
```python
(input: str) → str
```

Given a string, calculate its hash and return it.

Args:
- input (str): String to hash.

Returns:
`str`: Hash of the string.

<h3 id="caller_relative_path"><a href="#caller_relative_path">`caller_relative_path`</a></h3>
```python
(relative_path: str, idx: int | None = None) → str
```

Given a path, output the same path, relative to the absolute directory path of the file that invoked this function.

An optional argument `idx` can be supplied to change what script to get the absolute directory path from. Consider the following scenario:

A helper function in `src/utils` that takes in a relative path as an argument wants to transform the path into one relative to the caller's path. However, the said function needs to call this function directly. Said function can then use an index of `2` so that the given path to this function will be processed to be relative from the caller's path, not from the funciton in `src/utils/utils`.

Args:
- relative_path (`str`): Path to output relative to the caller's path.
- idx (`Optional[int]`, optional): Index of the stack to relativize the path from. Defaults to `1`.

Returns:
`str`: Path relative to the caller's path.

<h3 id="custom_version_ls_to_str"><a href="#custom_version_ls_to_str">`custom_version_ls_to_str`</a></h3>
```python
(vls: list[str | int] | list[int] | list[str]) → tuple[str, str]
```

Given the list of custom version numbers, convert them to their string representation both in modified semver form and semver-compliant form.

Args:
- vls (`list[str | int]`): List of version numbers.

Returns:
`tuple[str, str]`: List of string representation of given list of version numbers, both in modified semver form and semver-compliant form.

<h3 id="deprecated"><a href="#deprecated">`deprecated`</a></h3>
```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.
- reason (`str`, optional): Reason for deprecation. Defaults to None.

<h3 id="deprecated_class"><a href="#deprecated_class">`deprecated_class`</a></h3>
```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

<h3 id="dict_get_first_match"><a href="#dict_get_first_match">`dict_get_first_match`</a></h3>
```python
(dictionary: dict[typing.Any, typing.Any], keys: list[int | list[str | int | tuple[str, ...]] | str], default_value: Any | None = None) → Any
```

Iterate through the `keys` and see if the value exists in the `dictionary`. First one that exists will be returned. If none exists, return `default_value`.

Args:
- dictionary (`dict[Any, Any]`): Dictionary to retrieve the value from.
- keys (`list[int | tuple[str | int | tuple] | str]`): List of keys to iterate through.
- default_value (`Any`, optional): Default object to be returned. Defaults to None.

Returns:
`Any`: Retrieved value.

<h3 id="ensure_parent_dir"><a href="#ensure_parent_dir">`ensure_parent_dir`</a></h3>
```python
(file_path: str, make_dir_append_to_ls: list[str] | None = None) → str
```

If the directory of the file path does not exist, then make it.

Args:
- file_path (`str`): File path to check if it is a directory, and if not, to make one of the same name.
- ls (`Optional[list[str]]`, optional): A list of string to which this function can append the file path to if the given file path is not a directory. Defaults to `None`.

Returns:
`str`: Given filepath.

<h3 id="file_exists"><a href="#file_exists">`file_exists`</a></h3>
```python
(fp: str) → str
```

Check if the given file path exists.

Args:
- fp (`str`): File path to check if it exists.

Raises:
- `alltheutils.exceptions.FileNotFound`: Raised when a file in the path is not found.

Returns:
`str`: Return `fp` when file path exists.

<h3 id="fill_ls"><a href="#fill_ls">`fill_ls`</a></h3>
```python
(*, ls: Sequence[typing.Any], length: int, filler: Any | None = None) → Sequence[typing.Any]
```

Fill given list (`ls`) with `filler` up to `length`.

Args:
- ls (`types.SequenceAny`): List to fill with `filler` up to `length`
- length (`int`): Length of the list to achieve.
- filler (`Optional[Any]`, optional): Filler to use. Defaults to `None`.

Returns:
`types.SequenceAny`: Filled list.

<h3 id="first_not_none_in_ls"><a href="#first_not_none_in_ls">`first_not_none_in_ls`</a></h3>
```python
(ls: list[Any | None]) → Any
```

Return First Non-None.

Return the first argument that is not `None`, else return `None`.

Args:
- ls (`types.ListAny`): List of objects to check.

Returns:
`Any`: The first argument that is not `None`, else `None`.

<h3 id="flatten_element"><a href="#flatten_element">`flatten_element`</a></h3>
```python
(elem: dict[typing.Any, typing.Any], sep: str = '/') → dict[typing.Any, typing.Any]
```

<h3 id="get_value_from_or_update_nested_dict"><a href="#get_value_from_or_update_nested_dict">`get_value_from_or_update_nested_dict`</a></h3>
```python
(data: dict, address: str, new_value: int | dict | str | None = None)
```

Updates or retrieves a nested dictionary value at the given dot-separated address.

- If `new_value` is provided, updates the value.
- If `new_value` is `None`, returns the current value at `address`.

<h3 id="if_none"><a href="#if_none">`if_none`</a></h3>
```python
(variable: Any, default: Any) → Any
```

"If variable is None, then return the default".

If `variable` is `None`, return `default` else `var`.

Args:
- variable (`Any`): Variable to check if it is None.
- default (`Any`): Default value to return if var is None.

Returns:
`Any`: `variable` if `variable` is not None else `default`.

<h3 id="iter_ls_with_items"><a href="#iter_ls_with_items">`iter_ls_with_items`</a></h3>
```python
(ls: list[typing.Any], *items: list[typing.Any]) → Generator[tuple[typing.Any, ...], None, None]
```

<h3 id="literal_eval"><a href="#literal_eval">`literal_eval`</a></h3>
```python
(expr: str | None) → Any
```

Literal Evaluation.

Args:
- expr (`Optional[str]`): Expression to be evaluated.

Returns:
`Any`: Expression literally evaluated.

<h3 id="noop"><a href="#noop">`noop`</a></h3>
```python
(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) → None
```

No operation.

<h3 id="noop_single_kwargs"><a href="#noop_single_kwargs">`noop_single_kwargs`</a></h3>
```python
(arg: Any) → Any
```

<h3 id="parent_dir_nth_times"><a href="#parent_dir_nth_times">`parent_dir_nth_times`</a></h3>
```python
(filename: str, n: int | None = None) → str
```

Dirname N-th times.

Given a file name and a number, find the parent directory of the given filename as many times as the given number.

Args:
- filename (`str`): The filename to find the parent directory of.
- n (`int`): How many times the parent directory of the given filename should be found.

Returns:
`str`: Parent directory of the given filename.

<h3 id="run_cmd"><a href="#run_cmd">`run_cmd`</a></h3>
```python
(cmd: str) → None
```

Given a string, execute it as a shell command.

Args:
- cmd (`str`): Shell command to excute.

<h3 id="run_mp"><a href="#run_mp">`run_mp`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → list[typing.Any]
```

<h3 id="run_mp_qgr"><a href="#run_mp_qgr">`run_mp_qgr`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

<h3 id="run_mp_qir"><a href="#run_mp_qir">`run_mp_qir`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any], callback: Callable[..., typing.Any]) → None
```

Run `multiprocessing.Pool().map_async()`, and quit in return.

Iterate over `iterable` and apply iterated item to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

This function requires the given function to return a bool, or an iterable with its first item as a bool. This bool is then used to decide whether to trigger the callback and terminate the pool.

Args:
- func (`types.CallableAny`): Function to be run on each item in parallel.
- iterable (`types.IterAny`): Iterable containing items to iterate over and pass to `func`.
- callback (`types.CallableAny`): Function to be called when a process in the pool returns.

<h3 id="run_mp_star"><a href="#run_mp_star">`run_mp_star`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → list[typing.Any]
```

<h3 id="run_mp_star_qgr"><a href="#run_mp_star_qgr">`run_mp_star_qgr`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

<h3 id="run_mp_star_qir"><a href="#run_mp_star_qir">`run_mp_star_qir`</a></h3>
```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]], callback: Callable[..., typing.Any]) → None
```

Run `multiprocessing.Pool().starmap_async()`, and quit in return.

Iterate over `iterable` and apply iterated items to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

<h3 id="sanitize_text"><a href="#sanitize_text">`sanitize_text`</a></h3>
```python
(s: str) → str
```

Sanitize input text.

Reference: https://stackoverflow.com/a/93029

Args:
- s (`str`): Text to be sanitized.

Returns:
`str`: Sanitized text.

<h3 id="search_query"><a href="#search_query">`search_query`</a></h3>
```python
(query: str, possibilities: list[str], cutoff: int | float = 0.6, *, processor: Callable[[typing.Any], typing.Any] = <function <lambda>>) → Generator[tuple[None, str] | tuple[float, str], None, None]
```

Custom search query.

Args:
- query (`str`): String to search for in the possibilities.
- possibilities (`list[str]`): The possibilities to search from.
- cutoff (`int | float`, optional): The minimum percentage of similarity from the given possibilities. Defaults to `0.6`.
- processor (`Callable[[Any], Any]`, optional): Processes the possibilities before comparing it with the query. Defaults to `lambda x: x`.

Returns:
`Generator[tuple[None, str] | tuple[float, str], None, None]`: Generator object of mastching search quries.

<h3 id="str2int"><a href="#str2int">`str2int`</a></h3>
```python
(num: int | str) → int | None
```

If given number is int, return it. Else, if given number is string and is decimal, convert string to integer. Otherwise, return None.

Args:
- s (`int | str`): int or string to convert to integer.

Returns:
`Optional[int]`: If given argument can be converted to integer, it will be returned. Otherwise, None will be.

<h3 id="unix_timestamp_to_iso"><a href="#unix_timestamp_to_iso">`unix_timestamp_to_iso`</a></h3>
```python
(timestamp: int) → str
```

Convert the given unix timestamp to ISO 8601 format.

Args:
- ts (`int`): unix timestamp to be converted to ISO 8601 format

Returns:
`str`: Formatted datetime string

<h3 id="which_ls"><a href="#which_ls">`which_ls`</a></h3>
```python
(cmd: str, mode: int | None = None, path: str | None = None) → tuple[str] | tuple[str, ...] | None
```

Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH, or None if there is no such file. Yoinked from shutil.

Args:
- mode (`int`, optional): File mode to look for. Defaults to `os.F_OK | os.X_OK`.
- path (`str`, optional): Path to search the command at. Defaults to the result of os.environ.get("PATH").

Returns:
`Optional[types.TupleStr]`: Tuple of commands that conforms to the given arguments as said above.

<h3 id="yaml_str_presenter"><a href="#yaml_str_presenter">`yaml_str_presenter`</a></h3>
```python
(dumper, data)
```

<h3 id="zip_extend"><a href="#zip_extend">`zip_extend`</a></h3>
```python
(a: <class 'collections.abc.Sized'>, b: <class 'collections.abc.Sized'>) → Iterable[typing.Any]
```

Given two list, iterate through both of them, and cycle the shorter list until the longer list has been exhausted.

Args:
- a (`Sized`): First sized iterable.
- b (`Sized`): Second sized iterable.

Returns:
`Iterable[Any]`: Zipped extended iterable.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="callbackgetresult"><a href="#callbackgetresult">`CallbackGetResult`</a></h3>

<h4 id="methods"><a href="#methods">Methods</a></h4>

<h5 id="callback"><a href="#callback">`callback`</a></h5>
```python
(self, *args: tuple[typing.Any, ...]) → None
```

<h5 id="get"><a href="#get">`get`</a></h5>
```python
(self) → tuple[None] | tuple[typing.Any, ...]
```

<h3 id="poolterminate"><a href="#poolterminate">`PoolTerminate`</a></h3>
```python
(pool: multiprocessing.pool.Pool, callback: Callable[..., typing.Any])
```

<h4 id="methods"><a href="#methods">Methods</a></h4>

<h5 id="inner"><a href="#inner">`inner`</a></h5>
```python
(self, err: bool, *args: tuple[typing.Any, ...], **kwargs: dict[str, typing.Any]) → None
```

---

[← Go back to `alltheutils`](./index.md)
<h1 id=""><a href="#">Module alltheutils.utils</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-batch_replace"><a href="#functions-batch_replace"><pre>batch_replace</pre></a></h3>

```python
(text: str, key_value_map: dict[str, list[str]]) → str
```

Iterate through the dictionary, find the values in the given string and replace it with the corresponding key, and output the modified string.

Args:
- text (`str`): String to modify the contents of.
- key_value_map (`dict[str, list[str]]`): Key-value pairs of string to replace the substring with and list of string to replace with the corresponding key.

Returns:
`str`: Modified string.

<h3 id="functions-calculate_sha256_hash"><a href="#functions-calculate_sha256_hash"><pre>calculate_sha256_hash</pre></a></h3>

```python
(input: str) → str
```

Given a string, calculate its hash and return it.

Args:
- input (str): String to hash.

Returns:
`str`: Hash of the string.

<h3 id="functions-caller_relative_path"><a href="#functions-caller_relative_path"><pre>caller_relative_path</pre></a></h3>

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

<h3 id="functions-custom_version_ls_to_str"><a href="#functions-custom_version_ls_to_str"><pre>custom_version_ls_to_str</pre></a></h3>

```python
(vls: list[str | int] | list[int] | list[str]) → tuple[str, str]
```

Given the list of custom version numbers, convert them to their string representation both in modified semver form and semver-compliant form.

Args:
- vls (`list[str | int]`): List of version numbers.

Returns:
`tuple[str, str]`: List of string representation of given list of version numbers, both in modified semver form and semver-compliant form.

<h3 id="functions-deprecated"><a href="#functions-deprecated"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.
- reason (`str`, optional): Reason for deprecation. Defaults to None.

<h3 id="functions-deprecated_class"><a href="#functions-deprecated_class"><pre>deprecated_class</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

<h3 id="functions-dict_get_first_match"><a href="#functions-dict_get_first_match"><pre>dict_get_first_match</pre></a></h3>

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

<h3 id="functions-ensure_parent_dir"><a href="#functions-ensure_parent_dir"><pre>ensure_parent_dir</pre></a></h3>

```python
(file_path: str, make_dir_append_to_ls: list[str] | None = None) → str
```

If the directory of the file path does not exist, then make it.

Args:
- file_path (`str`): File path to check if it is a directory, and if not, to make one of the same name.
- ls (`Optional[list[str]]`, optional): A list of string to which this function can append the file path to if the given file path is not a directory. Defaults to `None`.

Returns:
`str`: Given filepath.

<h3 id="functions-file_exists"><a href="#functions-file_exists"><pre>file_exists</pre></a></h3>

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

<h3 id="functions-fill_ls"><a href="#functions-fill_ls"><pre>fill_ls</pre></a></h3>

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

<h3 id="functions-first_not_none_in_ls"><a href="#functions-first_not_none_in_ls"><pre>first_not_none_in_ls</pre></a></h3>

```python
(ls: list[Any | None]) → Any
```

Return First Non-None.

Return the first argument that is not `None`, else return `None`.

Args:
- ls (`types.ListAny`): List of objects to check.

Returns:
`Any`: The first argument that is not `None`, else `None`.

<h3 id="functions-flatten_element"><a href="#functions-flatten_element"><pre>flatten_element</pre></a></h3>

```python
(elem: dict[typing.Any, typing.Any], sep: str = '/') → dict[typing.Any, typing.Any]
```

<h3 id="functions-get_value_from_or_update_nested_dict"><a href="#functions-get_value_from_or_update_nested_dict"><pre>get_value_from_or_update_nested_dict</pre></a></h3>

```python
(data: dict, address: str, new_value: int | dict | str | None = None)
```

Updates or retrieves a nested dictionary value at the given dot-separated address.

- If `new_value` is provided, updates the value.
- If `new_value` is `None`, returns the current value at `address`.

<h3 id="functions-if_none"><a href="#functions-if_none"><pre>if_none</pre></a></h3>

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

<h3 id="functions-iter_ls_with_items"><a href="#functions-iter_ls_with_items"><pre>iter_ls_with_items</pre></a></h3>

```python
(ls: list[typing.Any], *items: list[typing.Any]) → Generator[tuple[typing.Any, ...], None, None]
```

<h3 id="functions-literal_eval"><a href="#functions-literal_eval"><pre>literal_eval</pre></a></h3>

```python
(expr: str | None) → Any
```

Literal Evaluation.

Args:
- expr (`Optional[str]`): Expression to be evaluated.

Returns:
`Any`: Expression literally evaluated.

<h3 id="functions-noop"><a href="#functions-noop"><pre>noop</pre></a></h3>

```python
(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) → None
```

No operation.

<h3 id="functions-noop_single_kwargs"><a href="#functions-noop_single_kwargs"><pre>noop_single_kwargs</pre></a></h3>

```python
(arg: Any) → Any
```

<h3 id="functions-parent_dir_nth_times"><a href="#functions-parent_dir_nth_times"><pre>parent_dir_nth_times</pre></a></h3>

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

<h3 id="functions-requires_instance_config"><a href="#functions-requires_instance_config"><pre>requires_instance_config</pre></a></h3>

```python
(*keys)
```

<h3 id="functions-run_cmd"><a href="#functions-run_cmd"><pre>run_cmd</pre></a></h3>

```python
(cmd: str) → None
```

Given a string, execute it as a shell command.

Args:
- cmd (`str`): Shell command to excute.

<h3 id="functions-run_mp"><a href="#functions-run_mp"><pre>run_mp</pre></a></h3>

```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → list[typing.Any]
```

<h3 id="functions-run_mp_qgr"><a href="#functions-run_mp_qgr"><pre>run_mp_qgr</pre></a></h3>

```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

<h3 id="functions-run_mp_qir"><a href="#functions-run_mp_qir"><pre>run_mp_qir</pre></a></h3>

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

<h3 id="functions-run_mp_star"><a href="#functions-run_mp_star"><pre>run_mp_star</pre></a></h3>

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → list[typing.Any]
```

<h3 id="functions-run_mp_star_qgr"><a href="#functions-run_mp_star_qgr"><pre>run_mp_star_qgr</pre></a></h3>

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

<h3 id="functions-run_mp_star_qir"><a href="#functions-run_mp_star_qir"><pre>run_mp_star_qir</pre></a></h3>

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]], callback: Callable[..., typing.Any]) → None
```

Run `multiprocessing.Pool().starmap_async()`, and quit in return.

Iterate over `iterable` and apply iterated items to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

<h3 id="functions-sanitize_text"><a href="#functions-sanitize_text"><pre>sanitize_text</pre></a></h3>

```python
(s: str) → str
```

Sanitize input text.

Reference: https://stackoverflow.com/a/93029

Args:
- s (`str`): Text to be sanitized.

Returns:
`str`: Sanitized text.

<h3 id="functions-search_query"><a href="#functions-search_query"><pre>search_query</pre></a></h3>

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

<h3 id="functions-str2int"><a href="#functions-str2int"><pre>str2int</pre></a></h3>

```python
(num: int | str) → int | None
```

If given number is int, return it. Else, if given number is string and is decimal, convert string to integer. Otherwise, return None.

Args:
- s (`int | str`): int or string to convert to integer.

Returns:
`Optional[int]`: If given argument can be converted to integer, it will be returned. Otherwise, None will be.

<h3 id="functions-unix_timestamp_to_iso"><a href="#functions-unix_timestamp_to_iso"><pre>unix_timestamp_to_iso</pre></a></h3>

```python
(timestamp: int) → str
```

Convert the given unix timestamp to ISO 8601 format.

Args:
- ts (`int`): unix timestamp to be converted to ISO 8601 format

Returns:
`str`: Formatted datetime string

<h3 id="functions-which_ls"><a href="#functions-which_ls"><pre>which_ls</pre></a></h3>

```python
(cmd: str, mode: int | None = None, path: str | None = None) → tuple[str] | tuple[str, ...] | None
```

Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH, or None if there is no such file. Yoinked from shutil.

Args:
- mode (`int`, optional): File mode to look for. Defaults to `os.F_OK | os.X_OK`.
- path (`str`, optional): Path to search the command at. Defaults to the result of os.environ.get("PATH").

Returns:
`Optional[types.TupleStr]`: Tuple of commands that conforms to the given arguments as said above.

<h3 id="functions-yaml_str_presenter"><a href="#functions-yaml_str_presenter"><pre>yaml_str_presenter</pre></a></h3>

```python
(dumper, data)
```

<h3 id="functions-zip_extend"><a href="#functions-zip_extend"><pre>zip_extend</pre></a></h3>

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

<h3 id="classes-callbackgetresult"><a href="#classes-callbackgetresult"><pre>CallbackGetResult</pre></a></h3>

<h4 id="classes-callbackgetresult-methods"><a href="#classes-callbackgetresult-methods">Methods</a></h4>

<h5 id="classes-callbackgetresult-methods-callback"><a href="#classes-callbackgetresult-methods-callback"><pre>callback</pre></a></h5>

```python
(self, *args: tuple[typing.Any, ...]) → None
```

<h5 id="classes-callbackgetresult-methods-get"><a href="#classes-callbackgetresult-methods-get"><pre>get</pre></a></h5>

```python
(self) → tuple[None] | tuple[typing.Any, ...]
```

<h3 id="classes-poolterminate"><a href="#classes-poolterminate"><pre>PoolTerminate</pre></a></h3>

```python
(pool: multiprocessing.pool.Pool, callback: Callable[..., typing.Any])
```

<h4 id="classes-poolterminate-methods"><a href="#classes-poolterminate-methods">Methods</a></h4>

<h5 id="classes-poolterminate-methods-inner"><a href="#classes-poolterminate-methods-inner"><pre>inner</pre></a></h5>

```python
(self, err: bool, *args: tuple[typing.Any, ...], **kwargs: dict[str, typing.Any]) → None
```

---

[← Go back to `alltheutils`](./index.md)
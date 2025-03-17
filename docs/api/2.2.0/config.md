<h1 id=""><a href="#">Module alltheutils.config</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-predump_conf_objpre"><a href="#functions-predump_conf_objpre"><pre>dump_conf_obj</pre></a></h3>

```python
(data: Any, ext: str) → str
```

Dumps a dictionary into a string based on the extension.

Args:
- data (`Any`): The data to serialize.
- ext (`str`): The file extension (e.g., "json", "yaml").

Returns:
- `str`: The serialized data.

Raises:
- `ConfigFileExtensionNotSupported`: if no serializer is available.

<h3 id="functions-preparse_conf_strpre"><a href="#functions-preparse_conf_strpre"><pre>parse_conf_str</pre></a></h3>

```python
(data_str: str, ext: str) → Any
```

Parses a given string into a dictionary based on the extension.

Args:
- data_str (`str`): The string to parse.
- ext (`str`): The file extension (e.g., "json", "yaml").

Returns:
`Any`: The parsed dictionary.

Raises:
- `ConfigFileExtensionNotSupported`: if no parser is available.

<h3 id="functions-preread_conf_filepre"><a href="#functions-preread_conf_filepre"><pre>read_conf_file</pre></a></h3>

```python
(file_path: str) → Any
```

Reads the contents of a file and parses it based on the file extension.

Args:
- file_path (`str`): Path to the file.

Returns:
- `Any`: Parsed file content.

Raises:
- `ConfigFileExtensionNotSupported`: If the file extension is not supported.
- `FileNotFoundError`: If the file does not exist.

<h3 id="functions-prewrite_to_conf_filepre"><a href="#functions-prewrite_to_conf_filepre"><pre>write_to_conf_file</pre></a></h3>

```python
(file_path: str, value: Any) → None
```

Writes data to a file, serializing it based on the file extension.

Args:
- file_path (`str`): Path to the file.
- value (`Any`): Data to write.

Raises:
- `ConfigFileExtensionNotSupported`: If the file extension is not supported.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-preparserregistrypre"><a href="#classes-preparserregistrypre"><pre>ParserRegistry</pre></a></h3>

<h4 id="classes-preparserregistrypre-methods"><a href="#classes-preparserregistrypre-methods">Methods</a></h4>

<h5 id="classes-preparserregistrypre-methods-preget_parserpre"><a href="#classes-preparserregistrypre-methods-preget_parserpre"><pre>get_parser</pre></a></h5>

```python
(self, ext: str, mode: str) → Callable[[typing.Any], typing.Any]
```

Retrieve a parser function for the given file extension and mode.

Args:
- ext (`str`): The file extension (e.g., "yaml", "json").
- mode (`str`): The mode, either "r" (read) or "w" (write).

Raises:
- `ConfigFileExtensionNotSupported`: if no parser is found.

<h5 id="classes-preparserregistrypre-methods-preregisterpre"><a href="#classes-preparserregistrypre-methods-preregisterpre"><pre>register</pre></a></h5>

```python
(self, ext: str | list[str], mode: str, func: Callable[[typing.Any], typing.Any])
```

Register a parser for a given file extension and mode.

Args:
- ext (`str`): The file extension (e.g., "yaml", "json").
- mode (`str`): The mode, either "r" (read) or "w" (write).
- func (`Callable[[Any], Any]`): The function to handle parsing or dumping.

Raises:
`ValueError`: if the mode is not "r" or "w".

---

[← Go back to `alltheutils`](./index.md)
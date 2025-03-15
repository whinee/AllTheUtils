# <h1 id="module-alltheutilsconfig"><a href="#module-alltheutilsconfig">Module alltheutils.config</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="dump_conf_obj"><a href="#dump_conf_obj">`dump_conf_obj`</a></h3>
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

<h3 id="parse_conf_str"><a href="#parse_conf_str">`parse_conf_str`</a></h3>
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

<h3 id="read_conf_file"><a href="#read_conf_file">`read_conf_file`</a></h3>
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

<h3 id="write_to_conf_file"><a href="#write_to_conf_file">`write_to_conf_file`</a></h3>
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

<h3 id="parserregistry"><a href="#parserregistry">`ParserRegistry`</a></h3>

<h4 id="methods"><a href="#methods">Methods</a></h4>

<h5 id="get_parser"><a href="#get_parser">`get_parser`</a></h5>
```python
(self, ext: str, mode: str) → Callable[[typing.Any], typing.Any]
```

Retrieve a parser function for the given file extension and mode.

Args:
- ext (`str`): The file extension (e.g., "yaml", "json").
- mode (`str`): The mode, either "r" (read) or "w" (write).

Raises:
- `ConfigFileExtensionNotSupported`: if no parser is found.

<h5 id="register"><a href="#register">`register`</a></h5>
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
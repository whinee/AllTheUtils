# Module alltheutils.config

[← Go back to `alltheutils`](./index.md)

## Functions

### `dump_conf_obj`

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

### `parse_conf_str`

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

### `read_conf_file`

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

### `write_to_conf_file`

```python
(file_path: str, value: Any) → None
```

Writes data to a file, serializing it based on the file extension.

Args:
- file_path (`str`): Path to the file.
- value (`Any`): Data to write.

Raises:
- `ConfigFileExtensionNotSupported`: If the file extension is not supported.

## Classes

### `ParserRegistry`

#### Methods

##### `get_parser`

```python
(self, ext: str, mode: str) → Callable[[typing.Any], typing.Any]
```

Retrieve a parser function for the given file extension and mode.

Args:
- ext (`str`): The file extension (e.g., "yaml", "json").
- mode (`str`): The mode, either "r" (read) or "w" (write).

Raises:
- `ConfigFileExtensionNotSupported`: if no parser is found.

##### `register`

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
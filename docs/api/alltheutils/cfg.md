# Module alltheutils.cfg

[← Go back to `alltheutils`](./index.md)

## Functions

### `dcfg`

```python
(value: dict[str, typing.Any], ext: str) → str
```

Dump the given value to a string with the given extension.

Args:
- value (`dict`): Value to dump to a string.
- ext (`str`): Extension to dump the value to.

Returns:
`str`: The dumped value.

### `deprecated`

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

### `pcfg`

```python
(d: str, type: str) → dict[typing.Any, typing.Any]
```

Parse the given string as the given type.

Args:
- d (`str`): String to parse.
- type (`str`): Type to parse the string as.

Returns:
`dict`: The parsed string.

### `rcfg`

```python
(file: str) → dict[typing.Any, typing.Any]
```

Read the contents of a file with the given file name.

Args:
- file (`str`): File name of the file to read the contents of.

Returns:
`dict`: The contents of the file.

### `wcfg`

```python
(file: str, value: dict[typing.Any, typing.Any] | list[typing.Any]) → None
```

Write the given value to a file with the given file name.

Args:
- file (`str`): File name of the file to write the value to.
- value (`dict[Any, Any] | list[Any])`: Value to write to the file.

---

[← Go back to `alltheutils`](./index.md)
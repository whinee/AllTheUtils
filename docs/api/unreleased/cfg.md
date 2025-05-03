<h1 id=""><a href="#">Module alltheutils.cfg</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-dcfg"><a href="#functions-dcfg"><pre>dcfg</pre></a></h3>

```python
(value: dict[str, typing.Any], ext: str) → str
```

Dump the given value to a string with the given extension.

Args:
- value (`dict`): Value to dump to a string.
- ext (`str`): Extension to dump the value to.

Returns:
`str`: The dumped value.

<h3 id="functions-deprecated"><a href="#functions-deprecated"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

<h3 id="functions-pcfg"><a href="#functions-pcfg"><pre>pcfg</pre></a></h3>

```python
(d: str, type: str) → dict[typing.Any, typing.Any]
```

Parse the given string as the given type.

Args:
- d (`str`): String to parse.
- type (`str`): Type to parse the string as.

Returns:
`dict`: The parsed string.

<h3 id="functions-rcfg"><a href="#functions-rcfg"><pre>rcfg</pre></a></h3>

```python
(file: str) → dict[typing.Any, typing.Any]
```

Read the contents of a file with the given file name.

Args:
- file (`str`): File name of the file to read the contents of.

Returns:
`dict`: The contents of the file.

<h3 id="functions-wcfg"><a href="#functions-wcfg"><pre>wcfg</pre></a></h3>

```python
(file: str, value: dict[typing.Any, typing.Any] | list[typing.Any]) → None
```

Write the given value to a file with the given file name.

Args:
- file (`str`): File name of the file to write the value to.
- value (`dict[Any, Any] | list[Any])`: Value to write to the file.

---

[← Go back to `alltheutils`](./index.md)
# Module alltheutils.base_exc

[← Go back to `alltheutils`](./index.md)

## Functions

### `c_exc`

```python
(cls: type[BaseException]) → type[BaseException]
```

Decorator to raise a custom exception.

This function gives the class an __init__ function that raises the exception.
If the class does not inherit from any Exception, it will be automatically inherit from Exception.
This function also wraps the Exception with `c_exc_str` method, for adding the `__str__` method.

Args:
- cls (`BaseException | Object`): The exception to modify.

Returns:
`BaseException`: The exception to raise.

### `c_exc_str`

```python
(cls: type[BaseException]) → type[BaseException]
```

Decorator to add the __str__ method to an exception.

Args:
- cls (`BaseException`): The exception to add the __str__ method to.

Returns:
`BaseException`: The exception to raise.

### `deprecated`

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

---

[← Go back to `alltheutils`](./index.md)
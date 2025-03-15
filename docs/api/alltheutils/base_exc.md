# <h1 id="module-alltheutilsbase_exc"><a href="#module-alltheutilsbase_exc">Module alltheutils.base_exc</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="c_exc"><a href="#c_exc">`c_exc`</a></h3>
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

<h3 id="c_exc_str"><a href="#c_exc_str">`c_exc_str`</a></h3>
```python
(cls: type[BaseException]) → type[BaseException]
```

Decorator to add the __str__ method to an exception.

Args:
- cls (`BaseException`): The exception to add the __str__ method to.

Returns:
`BaseException`: The exception to raise.

<h3 id="deprecated"><a href="#deprecated">`deprecated`</a></h3>
```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

---

[← Go back to `alltheutils`](./index.md)
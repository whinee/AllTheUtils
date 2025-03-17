<h1 id=""><a href="#">Module alltheutils.base_exc</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-prec_excpre"><a href="#functions-prec_excpre"><pre>c_exc</pre></a></h3>

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

<h3 id="functions-prec_exc_strpre"><a href="#functions-prec_exc_strpre"><pre>c_exc_str</pre></a></h3>

```python
(cls: type[BaseException]) → type[BaseException]
```

Decorator to add the __str__ method to an exception.

Args:
- cls (`BaseException`): The exception to add the __str__ method to.

Returns:
`BaseException`: The exception to raise.

<h3 id="functions-predeprecatedpre"><a href="#functions-predeprecatedpre"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

---

[← Go back to `alltheutils`](./index.md)
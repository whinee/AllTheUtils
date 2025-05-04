<h1 id=""><a href="#">Module alltheutils.base_exceptions</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-custom_exception"><a href="#functions-custom_exception"><pre>custom_exception</pre></a></h3>

```python
(cls: type[alltheutils.base_exceptions.CustomBaseException]) → type[alltheutils.base_exceptions.CustomBaseException]
```

Decorator to raise a custom exception.

This function gives the class an __init__ function that raises the exception.
If the class does not inherit from any Exception, it will be automatically inherit from Exception.
This function also wraps the Exception with `c_exc_str` method, for adding the `__str__` method.

Args:
- cls (`BaseException | Object`): The exception to modify.

Returns:
`BaseException`: The exception to raise.

<h3 id="functions-custom_exception_hook"><a href="#functions-custom_exception_hook"><pre>custom_exception_hook</pre></a></h3>

```python
(exctype: type[alltheutils.base_exceptions.CustomBaseException], value: alltheutils.base_exceptions.CustomBaseException, traceback: traceback | None) → None
```

<h3 id="functions-custom_exception_str"><a href="#functions-custom_exception_str"><pre>custom_exception_str</pre></a></h3>

```python
(cls: type[BaseException]) → type[BaseException]
```

Decorator to add the __str__ method to an exception.

Args:
- cls (`BaseException`): The exception to add the __str__ method to.

Returns:
`BaseException`: The exception to raise.

<h3 id="functions-deprecated"><a href="#functions-deprecated"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
    version (str): The version in which the function will be removed.
    replacement (str, optional): The new function to use instead.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-custombaseexception"><a href="#classes-custombaseexception"><pre>CustomBaseException</pre></a></h3>

```python
(message: str)
```

Base class for all custom exceptions.

<h4 id="classes-custombaseexception-ancestors-in-mro"><a href="#classes-custombaseexception-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-custombaseexception-descendants"><a href="#classes-custombaseexception-descendants">Descendants</a></h4>

- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CFGExceptions.ExtensionNotSupported
- alltheutils.exceptions.CLICommandNotFound
- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIExceptions.TerminalTooThin
- alltheutils.exceptions.CLIExceptions.ValidationError.Common
- alltheutils.exceptions.CLIExceptions.ValidationError.OptionRequired
- alltheutils.exceptions.CLIOptionRequired
- alltheutils.exceptions.CommonValidationError
- alltheutils.exceptions.ConfigExceptions.ExtensionNotSupported
- alltheutils.exceptions.ConfigFileExtensionNotSupported
- alltheutils.exceptions.FileNotFound
- alltheutils.exceptions.GeneralExceptions.PrerequisiteNotFound
- alltheutils.exceptions.GeneralExceptions.ValidationError.Arguments
- alltheutils.exceptions.GeneralExceptions.ValidationError.Common
- alltheutils.exceptions.GeneralExceptions.ValidationError.FileNotFound
- alltheutils.exceptions.MissingInstanceConfigValue
- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueIsAListAndIndexIsOutOfRange
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList
- alltheutils.exceptions.NestedDictExceptions.NonDictReplacementValue
- alltheutils.exceptions.NestedDictExceptions.ValueDoesNotExist
- alltheutils.exceptions.NestedDictExceptions.ValueIsAListAndIndexIsOutOfRange
- alltheutils.exceptions.NestedDictExceptions.ValueNotADict
- alltheutils.exceptions.NestedDictExceptions.ValueNotAList
- alltheutils.exceptions.PrerequisiteNotFound
- alltheutils.exceptions.TerminalTooThin

<h4 id="classes-custombaseexception-class-variables"><a href="#classes-custombaseexception-class-variables">Class variables</a></h4>

<h5 id="classes-custombaseexception-class-variables-details"><a href="#classes-custombaseexception-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

<h5 id="classes-custombaseexception-class-variables-message"><a href="#classes-custombaseexception-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

<h4 id="classes-custombaseexception-methods"><a href="#classes-custombaseexception-methods">Methods</a></h4>

<h5 id="classes-custombaseexception-methods-print_details"><a href="#classes-custombaseexception-methods-print_details"><pre>print_details</pre></a></h5>

```python
(self) → None
```

---

[← Go back to `alltheutils`](./index.md)
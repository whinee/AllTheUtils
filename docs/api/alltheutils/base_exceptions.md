# Module alltheutils.base_exceptions

[← Go back to `alltheutils`](./index.md)

## Functions

### `custom_exception`

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

### `custom_exception_hook`

```python
(exctype: type[alltheutils.base_exceptions.CustomBaseException], value: alltheutils.base_exceptions.CustomBaseException, traceback: traceback | None) → None
```

### `custom_exception_str`

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

## Classes

### `CustomBaseException`

```python
(message: str)
```

Base class for all custom exceptions.

#### Ancestors (in MRO)

- builtins.BaseException

#### Descendants

- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CFGExceptions.ExtensionNotSupported
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

#### Class variables

##### `details`

```python
str | None
```

##### `message`

```python
str
```

#### Methods

##### `print_details`

```python
(self) → None
```

---

[← Go back to `alltheutils`](./index.md)
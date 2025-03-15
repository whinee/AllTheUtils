# Module alltheutils.exceptions

[← Go back to `alltheutils`](./index.md)

## Functions

### `deprecated`

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.

### `deprecated_class`

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

## Classes

### `ArgumentsNotFollowingSpec`

```python
(parameter: str, argument: Any, specification: str, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a parameter is required to be of specification, but is not followed.

Args:
- parameter (`str`): Name of the parameter.
- argument (`any`): Argument passed to the parameter.
- specification (`str`): Specification/s of the parameter.

#### Ancestors (in MRO)

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `CFGExceptions`

#### Class variables

##### `ExtensionNotSupported`

Method or function hasn't been implemented yet.

### `CLICommonError`

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `CLIExceptions`

#### Class variables

##### `TerminalTooThin`

Base class for all custom exceptions.

##### `ValidationError`

### `CLIOptionRequired`

```python
(option: str)
```

Base class for all custom exceptions.

Raised when an option is required but no argument is passed.

Args:
- option (`str`): Required option with no arguments passed into it.

#### Ancestors (in MRO)

- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `CLIValidationError`

```python
(*args, **kwargs)
```

Common base class for all exceptions

#### Ancestors (in MRO)

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- builtins.BaseException

#### Descendants

- alltheutils.exceptions.CLIOptionRequired

### `CommonValidationError`

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

#### Ancestors (in MRO)

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `ConfigExceptions`

#### Class variables

##### `ExtensionNotSupported`

Method or function hasn't been implemented yet.

### `ConfigFileExtensionNotSupported`

```python
(ext: str)
```

Method or function hasn't been implemented yet.

Raise when extension `{ext}` is not supported.

Args:
    ext (`str`): The extension not supported.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewConfigExceptions
- builtins.NotImplementedError
- builtins.RuntimeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `FileNotFound`

```python
(fp: str)
```

File not found.

Raised when a file in a given path is not found.

Args:
- parameter (`fp`): Path of the file that can not be found.

#### Ancestors (in MRO)

- alltheutils.exceptions.ValidationError
- builtins.FileNotFoundError
- builtins.OSError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `GeneralExceptions`

#### Class variables

##### `PrerequisiteNotFound`

Base class for all custom exceptions.

##### `ValidationError`

### `NDNonDictReplacementValue`

Inappropriate argument type.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `NDValueDoesNotExist`

```python
(keys: list[str], idx: int)
```

Mapping key not found.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `NDValueIsAListAndIndexIsOutOfRange`

```python
(keys: list[str], idx: int)
```

Sequence index out of range.

#### Ancestors (in MRO)

- builtins.IndexError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `NDValueNotADict`

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `NDValueNotAList`

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `NestedDictExceptions`

#### Class variables

##### `NonDictReplacementValue`

Inappropriate argument type.

##### `ValueDoesNotExist`

Mapping key not found.

##### `ValueIsAListAndIndexIsOutOfRange`

Sequence index out of range.

##### `ValueNotADict`

Inappropriate argument type.

##### `ValueNotAList`

Inappropriate argument type.

### `NewCLIExceptions`

```python
(*args, **kwargs)
```

Common base class for all exceptions

#### Ancestors (in MRO)

- builtins.BaseException

#### Descendants

- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.TerminalTooThin

### `NewConfigExceptions`

```python
(*args, **kwargs)
```

Common base class for all exceptions

#### Ancestors (in MRO)

- builtins.BaseException

#### Descendants

- alltheutils.exceptions.ConfigFileExtensionNotSupported

### `NewNestedDictExceptions`

```python
(*args, **kwargs)
```

Common base class for all exceptions

#### Ancestors (in MRO)

- builtins.BaseException

#### Descendants

- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList

### `PrerequisiteNotFound`

```python
(prerequisite: str, inst_instruction: str | None = None, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a prerequisite is needed by the program, but is not installed in the machine.

Args:
- prerequisite (`str`): Name of the prerequisite.
- inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.

#### Ancestors (in MRO)

- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `TerminalTooThin`

```python
(min_width: int)
```

Base class for all custom exceptions.

Raised when terminal is too thin for content to be rendered.

Args:
- min_width (`int`): Required minimum terminal width.

#### Ancestors (in MRO)

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

### `ValidationError`

```python
(*args, **kwargs)
```

Common base class for all exceptions

#### Ancestors (in MRO)

- builtins.BaseException

#### Descendants

- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.CommonValidationError
- alltheutils.exceptions.FileNotFound

---

[← Go back to `alltheutils`](./index.md)
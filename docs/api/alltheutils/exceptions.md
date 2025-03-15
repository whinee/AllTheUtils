# <h1 id="module-alltheutilsexceptions"><a href="#module-alltheutilsexceptions">Module alltheutils.exceptions</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="deprecated"><a href="#deprecated">`deprecated`</a></h3>
```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.

<h3 id="deprecated_class"><a href="#deprecated_class">`deprecated_class`</a></h3>
```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="argumentsnotfollowingspec"><a href="#argumentsnotfollowingspec">`ArgumentsNotFollowingSpec`</a></h3>
```python
(parameter: str, argument: Any, specification: str, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a parameter is required to be of specification, but is not followed.

Args:
- parameter (`str`): Name of the parameter.
- argument (`any`): Argument passed to the parameter.
- specification (`str`): Specification/s of the parameter.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="cfgexceptions"><a href="#cfgexceptions">`CFGExceptions`</a></h3>

<h4 id="class-variables"><a href="#class-variables">Class variables</a></h4>

<h5 id="extensionnotsupported"><a href="#extensionnotsupported">`ExtensionNotSupported`</a></h5>

Method or function hasn't been implemented yet.

<h3 id="clicommonerror"><a href="#clicommonerror">`CLICommonError`</a></h3>
```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="cliexceptions"><a href="#cliexceptions">`CLIExceptions`</a></h3>

<h4 id="class-variables"><a href="#class-variables">Class variables</a></h4>

<h5 id="terminaltoothin"><a href="#terminaltoothin">`TerminalTooThin`</a></h5>

Base class for all custom exceptions.

<h5 id="validationerror"><a href="#validationerror">`ValidationError`</a></h5>

<h3 id="clioptionrequired"><a href="#clioptionrequired">`CLIOptionRequired`</a></h3>
```python
(option: str)
```

Base class for all custom exceptions.

Raised when an option is required but no argument is passed.

Args:
- option (`str`): Required option with no arguments passed into it.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="clivalidationerror"><a href="#clivalidationerror">`CLIValidationError`</a></h3>
```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- builtins.BaseException

<h4 id="descendants"><a href="#descendants">Descendants</a></h4>
- alltheutils.exceptions.CLIOptionRequired

<h3 id="commonvalidationerror"><a href="#commonvalidationerror">`CommonValidationError`</a></h3>
```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="configexceptions"><a href="#configexceptions">`ConfigExceptions`</a></h3>

<h4 id="class-variables"><a href="#class-variables">Class variables</a></h4>

<h5 id="extensionnotsupported"><a href="#extensionnotsupported">`ExtensionNotSupported`</a></h5>

Method or function hasn't been implemented yet.

<h3 id="configfileextensionnotsupported"><a href="#configfileextensionnotsupported">`ConfigFileExtensionNotSupported`</a></h3>
```python
(ext: str)
```

Method or function hasn't been implemented yet.

Raise when extension `{ext}` is not supported.

Args:
    ext (`str`): The extension not supported.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewConfigExceptions
- builtins.NotImplementedError
- builtins.RuntimeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="filenotfound"><a href="#filenotfound">`FileNotFound`</a></h3>
```python
(fp: str)
```

File not found.

Raised when a file in a given path is not found.

Args:
- parameter (`fp`): Path of the file that can not be found.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.ValidationError
- builtins.FileNotFoundError
- builtins.OSError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="generalexceptions"><a href="#generalexceptions">`GeneralExceptions`</a></h3>

<h4 id="class-variables"><a href="#class-variables">Class variables</a></h4>

<h5 id="prerequisitenotfound"><a href="#prerequisitenotfound">`PrerequisiteNotFound`</a></h5>

Base class for all custom exceptions.

<h5 id="validationerror"><a href="#validationerror">`ValidationError`</a></h5>

<h3 id="ndnondictreplacementvalue"><a href="#ndnondictreplacementvalue">`NDNonDictReplacementValue`</a></h3>

Inappropriate argument type.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="ndvaluedoesnotexist"><a href="#ndvaluedoesnotexist">`NDValueDoesNotExist`</a></h3>
```python
(keys: list[str], idx: int)
```

Mapping key not found.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="ndvalueisalistandindexisoutofrange"><a href="#ndvalueisalistandindexisoutofrange">`NDValueIsAListAndIndexIsOutOfRange`</a></h3>
```python
(keys: list[str], idx: int)
```

Sequence index out of range.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- builtins.IndexError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="ndvaluenotadict"><a href="#ndvaluenotadict">`NDValueNotADict`</a></h3>
```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="ndvaluenotalist"><a href="#ndvaluenotalist">`NDValueNotAList`</a></h3>
```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="nesteddictexceptions"><a href="#nesteddictexceptions">`NestedDictExceptions`</a></h3>

<h4 id="class-variables"><a href="#class-variables">Class variables</a></h4>

<h5 id="nondictreplacementvalue"><a href="#nondictreplacementvalue">`NonDictReplacementValue`</a></h5>

Inappropriate argument type.

<h5 id="valuedoesnotexist"><a href="#valuedoesnotexist">`ValueDoesNotExist`</a></h5>

Mapping key not found.

<h5 id="valueisalistandindexisoutofrange"><a href="#valueisalistandindexisoutofrange">`ValueIsAListAndIndexIsOutOfRange`</a></h5>

Sequence index out of range.

<h5 id="valuenotadict"><a href="#valuenotadict">`ValueNotADict`</a></h5>

Inappropriate argument type.

<h5 id="valuenotalist"><a href="#valuenotalist">`ValueNotAList`</a></h5>

Inappropriate argument type.

<h3 id="newcliexceptions"><a href="#newcliexceptions">`NewCLIExceptions`</a></h3>
```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- builtins.BaseException

<h4 id="descendants"><a href="#descendants">Descendants</a></h4>
- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.TerminalTooThin

<h3 id="newconfigexceptions"><a href="#newconfigexceptions">`NewConfigExceptions`</a></h3>
```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- builtins.BaseException

<h4 id="descendants"><a href="#descendants">Descendants</a></h4>
- alltheutils.exceptions.ConfigFileExtensionNotSupported

<h3 id="newnesteddictexceptions"><a href="#newnesteddictexceptions">`NewNestedDictExceptions`</a></h3>
```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- builtins.BaseException

<h4 id="descendants"><a href="#descendants">Descendants</a></h4>
- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList

<h3 id="prerequisitenotfound"><a href="#prerequisitenotfound">`PrerequisiteNotFound`</a></h3>
```python
(prerequisite: str, inst_instruction: str | None = None, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a prerequisite is needed by the program, but is not installed in the machine.

Args:
- prerequisite (`str`): Name of the prerequisite.
- inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="terminaltoothin"><a href="#terminaltoothin">`TerminalTooThin`</a></h3>
```python
(min_width: int)
```

Base class for all custom exceptions.

Raised when terminal is too thin for content to be rendered.

Args:
- min_width (`int`): Required minimum terminal width.

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="validationerror"><a href="#validationerror">`ValidationError`</a></h3>
```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="ancestors-in-mro"><a href="#ancestors-in-mro">Ancestors (in MRO)</a></h4>
- builtins.BaseException

<h4 id="descendants"><a href="#descendants">Descendants</a></h4>
- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.CommonValidationError
- alltheutils.exceptions.FileNotFound

---

[← Go back to `alltheutils`](./index.md)
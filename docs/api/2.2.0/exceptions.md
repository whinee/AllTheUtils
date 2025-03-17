<h1 id=""><a href="#">Module alltheutils.exceptions</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-predeprecatedpre"><a href="#functions-predeprecatedpre"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.

<h3 id="functions-predeprecated_classpre"><a href="#functions-predeprecated_classpre"><pre>deprecated_class</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-preargumentsnotfollowingspecpre"><a href="#classes-preargumentsnotfollowingspecpre"><pre>ArgumentsNotFollowingSpec</pre></a></h3>

```python
(parameter: str, argument: Any, specification: str, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a parameter is required to be of specification, but is not followed.

Args:
- parameter (`str`): Name of the parameter.
- argument (`any`): Argument passed to the parameter.
- specification (`str`): Specification/s of the parameter.

<h4 id="classes-preargumentsnotfollowingspecpre-ancestors-in-mro"><a href="#classes-preargumentsnotfollowingspecpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-precfgexceptionspre"><a href="#classes-precfgexceptionspre"><pre>CFGExceptions</pre></a></h3>

<h4 id="classes-precfgexceptionspre-class-variables"><a href="#classes-precfgexceptionspre-class-variables">Class variables</a></h4>

<h5 id="classes-precfgexceptionspre-class-variables-preextensionnotsupportedpre"><a href="#classes-precfgexceptionspre-class-variables-preextensionnotsupportedpre"><pre>ExtensionNotSupported</pre></a></h5>

Method or function hasn't been implemented yet.

<h3 id="classes-preclicommonerrorpre"><a href="#classes-preclicommonerrorpre"><pre>CLICommonError</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-preclicommonerrorpre-ancestors-in-mro"><a href="#classes-preclicommonerrorpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-precliexceptionspre"><a href="#classes-precliexceptionspre"><pre>CLIExceptions</pre></a></h3>

<h4 id="classes-precliexceptionspre-class-variables"><a href="#classes-precliexceptionspre-class-variables">Class variables</a></h4>

<h5 id="classes-precliexceptionspre-class-variables-preterminaltoothinpre"><a href="#classes-precliexceptionspre-class-variables-preterminaltoothinpre"><pre>TerminalTooThin</pre></a></h5>

Base class for all custom exceptions.

<h5 id="classes-precliexceptionspre-class-variables-prevalidationerrorpre"><a href="#classes-precliexceptionspre-class-variables-prevalidationerrorpre"><pre>ValidationError</pre></a></h5>

<h3 id="classes-preclioptionrequiredpre"><a href="#classes-preclioptionrequiredpre"><pre>CLIOptionRequired</pre></a></h3>

```python
(option: str)
```

Base class for all custom exceptions.

Raised when an option is required but no argument is passed.

Args:
- option (`str`): Required option with no arguments passed into it.

<h4 id="classes-preclioptionrequiredpre-ancestors-in-mro"><a href="#classes-preclioptionrequiredpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-preclivalidationerrorpre"><a href="#classes-preclivalidationerrorpre"><pre>CLIValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-preclivalidationerrorpre-ancestors-in-mro"><a href="#classes-preclivalidationerrorpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- builtins.BaseException

<h4 id="classes-preclivalidationerrorpre-descendants"><a href="#classes-preclivalidationerrorpre-descendants">Descendants</a></h4>

- alltheutils.exceptions.CLIOptionRequired

<h3 id="classes-precommonvalidationerrorpre"><a href="#classes-precommonvalidationerrorpre"><pre>CommonValidationError</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-precommonvalidationerrorpre-ancestors-in-mro"><a href="#classes-precommonvalidationerrorpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-preconfigexceptionspre"><a href="#classes-preconfigexceptionspre"><pre>ConfigExceptions</pre></a></h3>

<h4 id="classes-preconfigexceptionspre-class-variables"><a href="#classes-preconfigexceptionspre-class-variables">Class variables</a></h4>

<h5 id="classes-preconfigexceptionspre-class-variables-preextensionnotsupportedpre"><a href="#classes-preconfigexceptionspre-class-variables-preextensionnotsupportedpre"><pre>ExtensionNotSupported</pre></a></h5>

Method or function hasn't been implemented yet.

<h3 id="classes-preconfigfileextensionnotsupportedpre"><a href="#classes-preconfigfileextensionnotsupportedpre"><pre>ConfigFileExtensionNotSupported</pre></a></h3>

```python
(ext: str)
```

Method or function hasn't been implemented yet.

Raise when extension `{ext}` is not supported.

Args:
    ext (`str`): The extension not supported.

<h4 id="classes-preconfigfileextensionnotsupportedpre-ancestors-in-mro"><a href="#classes-preconfigfileextensionnotsupportedpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewConfigExceptions
- builtins.NotImplementedError
- builtins.RuntimeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prefilenotfoundpre"><a href="#classes-prefilenotfoundpre"><pre>FileNotFound</pre></a></h3>

```python
(fp: str)
```

File not found.

Raised when a file in a given path is not found.

Args:
- parameter (`fp`): Path of the file that can not be found.

<h4 id="classes-prefilenotfoundpre-ancestors-in-mro"><a href="#classes-prefilenotfoundpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- builtins.FileNotFoundError
- builtins.OSError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-pregeneralexceptionspre"><a href="#classes-pregeneralexceptionspre"><pre>GeneralExceptions</pre></a></h3>

<h4 id="classes-pregeneralexceptionspre-class-variables"><a href="#classes-pregeneralexceptionspre-class-variables">Class variables</a></h4>

<h5 id="classes-pregeneralexceptionspre-class-variables-preprerequisitenotfoundpre"><a href="#classes-pregeneralexceptionspre-class-variables-preprerequisitenotfoundpre"><pre>PrerequisiteNotFound</pre></a></h5>

Base class for all custom exceptions.

<h5 id="classes-pregeneralexceptionspre-class-variables-prevalidationerrorpre"><a href="#classes-pregeneralexceptionspre-class-variables-prevalidationerrorpre"><pre>ValidationError</pre></a></h5>

<h3 id="classes-prendnondictreplacementvaluepre"><a href="#classes-prendnondictreplacementvaluepre"><pre>NDNonDictReplacementValue</pre></a></h3>

Inappropriate argument type.

<h4 id="classes-prendnondictreplacementvaluepre-ancestors-in-mro"><a href="#classes-prendnondictreplacementvaluepre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prendvaluedoesnotexistpre"><a href="#classes-prendvaluedoesnotexistpre"><pre>NDValueDoesNotExist</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Mapping key not found.

<h4 id="classes-prendvaluedoesnotexistpre-ancestors-in-mro"><a href="#classes-prendvaluedoesnotexistpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prendvalueisalistandindexisoutofrangepre"><a href="#classes-prendvalueisalistandindexisoutofrangepre"><pre>NDValueIsAListAndIndexIsOutOfRange</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Sequence index out of range.

<h4 id="classes-prendvalueisalistandindexisoutofrangepre-ancestors-in-mro"><a href="#classes-prendvalueisalistandindexisoutofrangepre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.IndexError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prendvaluenotadictpre"><a href="#classes-prendvaluenotadictpre"><pre>NDValueNotADict</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-prendvaluenotadictpre-ancestors-in-mro"><a href="#classes-prendvaluenotadictpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prendvaluenotalistpre"><a href="#classes-prendvaluenotalistpre"><pre>NDValueNotAList</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-prendvaluenotalistpre-ancestors-in-mro"><a href="#classes-prendvaluenotalistpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prenesteddictexceptionspre"><a href="#classes-prenesteddictexceptionspre"><pre>NestedDictExceptions</pre></a></h3>

<h4 id="classes-prenesteddictexceptionspre-class-variables"><a href="#classes-prenesteddictexceptionspre-class-variables">Class variables</a></h4>

<h5 id="classes-prenesteddictexceptionspre-class-variables-prenondictreplacementvaluepre"><a href="#classes-prenesteddictexceptionspre-class-variables-prenondictreplacementvaluepre"><pre>NonDictReplacementValue</pre></a></h5>

Inappropriate argument type.

<h5 id="classes-prenesteddictexceptionspre-class-variables-prevaluedoesnotexistpre"><a href="#classes-prenesteddictexceptionspre-class-variables-prevaluedoesnotexistpre"><pre>ValueDoesNotExist</pre></a></h5>

Mapping key not found.

<h5 id="classes-prenesteddictexceptionspre-class-variables-prevalueisalistandindexisoutofrangepre"><a href="#classes-prenesteddictexceptionspre-class-variables-prevalueisalistandindexisoutofrangepre"><pre>ValueIsAListAndIndexIsOutOfRange</pre></a></h5>

Sequence index out of range.

<h5 id="classes-prenesteddictexceptionspre-class-variables-prevaluenotadictpre"><a href="#classes-prenesteddictexceptionspre-class-variables-prevaluenotadictpre"><pre>ValueNotADict</pre></a></h5>

Inappropriate argument type.

<h5 id="classes-prenesteddictexceptionspre-class-variables-prevaluenotalistpre"><a href="#classes-prenesteddictexceptionspre-class-variables-prevaluenotalistpre"><pre>ValueNotAList</pre></a></h5>

Inappropriate argument type.

<h3 id="classes-prenewcliexceptionspre"><a href="#classes-prenewcliexceptionspre"><pre>NewCLIExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-prenewcliexceptionspre-ancestors-in-mro"><a href="#classes-prenewcliexceptionspre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-prenewcliexceptionspre-descendants"><a href="#classes-prenewcliexceptionspre-descendants">Descendants</a></h4>

- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.TerminalTooThin

<h3 id="classes-prenewconfigexceptionspre"><a href="#classes-prenewconfigexceptionspre"><pre>NewConfigExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-prenewconfigexceptionspre-ancestors-in-mro"><a href="#classes-prenewconfigexceptionspre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-prenewconfigexceptionspre-descendants"><a href="#classes-prenewconfigexceptionspre-descendants">Descendants</a></h4>

- alltheutils.exceptions.ConfigFileExtensionNotSupported

<h3 id="classes-prenewnesteddictexceptionspre"><a href="#classes-prenewnesteddictexceptionspre"><pre>NewNestedDictExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-prenewnesteddictexceptionspre-ancestors-in-mro"><a href="#classes-prenewnesteddictexceptionspre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-prenewnesteddictexceptionspre-descendants"><a href="#classes-prenewnesteddictexceptionspre-descendants">Descendants</a></h4>

- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList

<h3 id="classes-preprerequisitenotfoundpre"><a href="#classes-preprerequisitenotfoundpre"><pre>PrerequisiteNotFound</pre></a></h3>

```python
(prerequisite: str, inst_instruction: str | None = None, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a prerequisite is needed by the program, but is not installed in the machine.

Args:
- prerequisite (`str`): Name of the prerequisite.
- inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.

<h4 id="classes-preprerequisitenotfoundpre-ancestors-in-mro"><a href="#classes-preprerequisitenotfoundpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-preterminaltoothinpre"><a href="#classes-preterminaltoothinpre"><pre>TerminalTooThin</pre></a></h3>

```python
(min_width: int)
```

Base class for all custom exceptions.

Raised when terminal is too thin for content to be rendered.

Args:
- min_width (`int`): Required minimum terminal width.

<h4 id="classes-preterminaltoothinpre-ancestors-in-mro"><a href="#classes-preterminaltoothinpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-prevalidationerrorpre"><a href="#classes-prevalidationerrorpre"><pre>ValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-prevalidationerrorpre-ancestors-in-mro"><a href="#classes-prevalidationerrorpre-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-prevalidationerrorpre-descendants"><a href="#classes-prevalidationerrorpre-descendants">Descendants</a></h4>

- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.CommonValidationError
- alltheutils.exceptions.FileNotFound

---

[← Go back to `alltheutils`](./index.md)
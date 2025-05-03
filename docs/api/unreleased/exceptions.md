<h1 id=""><a href="#">Module alltheutils.exceptions</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-deprecated"><a href="#functions-deprecated"><pre>deprecated</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark functions as deprecated.

Args:
- version (`str`): The version in which the function will be removed.
- replacement (`str`, optional): The new function to use instead.

<h3 id="functions-deprecated_class"><a href="#functions-deprecated_class"><pre>deprecated_class</pre></a></h3>

```python
(version: str, replacement: str | None = None, reason: str | None = None)
```

Decorator to mark a classes as deprecated.

Args:
- version (`str`): The version in which the exception will be removed.
- replacement (`str`, optional): The new exception to use instead.
- reason (`str`, optional): Additional reason for deprecation.

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-argumentsnotfollowingspec"><a href="#classes-argumentsnotfollowingspec"><pre>ArgumentsNotFollowingSpec</pre></a></h3>

```python
(parameter: str, argument: Any, specification: str, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a parameter is required to be of specification, but is not followed.

Args:
- parameter (`str`): Name of the parameter.
- argument (`any`): Argument passed to the parameter.
- specification (`str`): Specification/s of the parameter.

<h4 id="classes-argumentsnotfollowingspec-ancestors-in-mro"><a href="#classes-argumentsnotfollowingspec-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-cfgexceptions"><a href="#classes-cfgexceptions"><pre>CFGExceptions</pre></a></h3>

<h4 id="classes-cfgexceptions-class-variables"><a href="#classes-cfgexceptions-class-variables">Class variables</a></h4>

<h5 id="classes-cfgexceptions-class-variables-extensionnotsupported"><a href="#classes-cfgexceptions-class-variables-extensionnotsupported"><pre>ExtensionNotSupported</pre></a></h5>

Method or function hasn't been implemented yet.

<h3 id="classes-clicommandnotfound"><a href="#classes-clicommandnotfound"><pre>CLICommandNotFound</pre></a></h3>

```python
(command: str)
```

Base class for all custom exceptions.

Raised when a command is not found.

Args:
- command (`str`): Required option with no arguments passed into it.

<h4 id="classes-clicommandnotfound-ancestors-in-mro"><a href="#classes-clicommandnotfound-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-clicommonerror"><a href="#classes-clicommonerror"><pre>CLICommonError</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-clicommonerror-ancestors-in-mro"><a href="#classes-clicommonerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-cliexceptions"><a href="#classes-cliexceptions"><pre>CLIExceptions</pre></a></h3>

<h4 id="classes-cliexceptions-class-variables"><a href="#classes-cliexceptions-class-variables">Class variables</a></h4>

<h5 id="classes-cliexceptions-class-variables-terminaltoothin"><a href="#classes-cliexceptions-class-variables-terminaltoothin"><pre>TerminalTooThin</pre></a></h5>

Base class for all custom exceptions.

<h5 id="classes-cliexceptions-class-variables-validationerror"><a href="#classes-cliexceptions-class-variables-validationerror"><pre>ValidationError</pre></a></h5>

<h3 id="classes-clioptionrequired"><a href="#classes-clioptionrequired"><pre>CLIOptionRequired</pre></a></h3>

```python
(option: str)
```

Base class for all custom exceptions.

Raised when an option is required but no argument is passed.

Args:
- option (`str`): Required option with no arguments passed into it.

<h4 id="classes-clioptionrequired-ancestors-in-mro"><a href="#classes-clioptionrequired-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-clivalidationerror"><a href="#classes-clivalidationerror"><pre>CLIValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-clivalidationerror-ancestors-in-mro"><a href="#classes-clivalidationerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- builtins.BaseException

<h4 id="classes-clivalidationerror-descendants"><a href="#classes-clivalidationerror-descendants">Descendants</a></h4>

- alltheutils.exceptions.CLICommandNotFound
- alltheutils.exceptions.CLIOptionRequired

<h3 id="classes-commonvalidationerror"><a href="#classes-commonvalidationerror"><pre>CommonValidationError</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-commonvalidationerror-ancestors-in-mro"><a href="#classes-commonvalidationerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-configexceptions"><a href="#classes-configexceptions"><pre>ConfigExceptions</pre></a></h3>

<h4 id="classes-configexceptions-class-variables"><a href="#classes-configexceptions-class-variables">Class variables</a></h4>

<h5 id="classes-configexceptions-class-variables-extensionnotsupported"><a href="#classes-configexceptions-class-variables-extensionnotsupported"><pre>ExtensionNotSupported</pre></a></h5>

Method or function hasn't been implemented yet.

<h3 id="classes-configfileextensionnotsupported"><a href="#classes-configfileextensionnotsupported"><pre>ConfigFileExtensionNotSupported</pre></a></h3>

```python
(ext: str)
```

Method or function hasn't been implemented yet.

Raise when extension `{ext}` is not supported.

Args:
    ext (`str`): The extension not supported.

<h4 id="classes-configfileextensionnotsupported-ancestors-in-mro"><a href="#classes-configfileextensionnotsupported-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewConfigExceptions
- builtins.NotImplementedError
- builtins.RuntimeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-filenotfound"><a href="#classes-filenotfound"><pre>FileNotFound</pre></a></h3>

```python
(fp: str)
```

File not found.

Raised when a file in a given path is not found.

Args:
- parameter (`fp`): Path of the file that can not be found.

<h4 id="classes-filenotfound-ancestors-in-mro"><a href="#classes-filenotfound-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ValidationError
- builtins.FileNotFoundError
- builtins.OSError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-generalexceptions"><a href="#classes-generalexceptions"><pre>GeneralExceptions</pre></a></h3>

<h4 id="classes-generalexceptions-class-variables"><a href="#classes-generalexceptions-class-variables">Class variables</a></h4>

<h5 id="classes-generalexceptions-class-variables-prerequisitenotfound"><a href="#classes-generalexceptions-class-variables-prerequisitenotfound"><pre>PrerequisiteNotFound</pre></a></h5>

Base class for all custom exceptions.

<h5 id="classes-generalexceptions-class-variables-validationerror"><a href="#classes-generalexceptions-class-variables-validationerror"><pre>ValidationError</pre></a></h5>

<h3 id="classes-missinginstanceconfigvalue"><a href="#classes-missinginstanceconfigvalue"><pre>MissingInstanceConfigValue</pre></a></h3>

```python
(func_name: str, missing_constants: list[str])
```

Mapping key not found.

<h4 id="classes-missinginstanceconfigvalue-ancestors-in-mro"><a href="#classes-missinginstanceconfigvalue-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewConfigExceptions
- alltheutils.exceptions.ValidationError
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-ndnondictreplacementvalue"><a href="#classes-ndnondictreplacementvalue"><pre>NDNonDictReplacementValue</pre></a></h3>

Inappropriate argument type.

<h4 id="classes-ndnondictreplacementvalue-ancestors-in-mro"><a href="#classes-ndnondictreplacementvalue-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-ndvaluedoesnotexist"><a href="#classes-ndvaluedoesnotexist"><pre>NDValueDoesNotExist</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Mapping key not found.

<h4 id="classes-ndvaluedoesnotexist-ancestors-in-mro"><a href="#classes-ndvaluedoesnotexist-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-ndvalueisalistandindexisoutofrange"><a href="#classes-ndvalueisalistandindexisoutofrange"><pre>NDValueIsAListAndIndexIsOutOfRange</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Sequence index out of range.

<h4 id="classes-ndvalueisalistandindexisoutofrange-ancestors-in-mro"><a href="#classes-ndvalueisalistandindexisoutofrange-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.IndexError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-ndvaluenotadict"><a href="#classes-ndvaluenotadict"><pre>NDValueNotADict</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-ndvaluenotadict-ancestors-in-mro"><a href="#classes-ndvaluenotadict-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-ndvaluenotalist"><a href="#classes-ndvaluenotalist"><pre>NDValueNotAList</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-ndvaluenotalist-ancestors-in-mro"><a href="#classes-ndvaluenotalist-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-nesteddictexceptions"><a href="#classes-nesteddictexceptions"><pre>NestedDictExceptions</pre></a></h3>

<h4 id="classes-nesteddictexceptions-class-variables"><a href="#classes-nesteddictexceptions-class-variables">Class variables</a></h4>

<h5 id="classes-nesteddictexceptions-class-variables-nondictreplacementvalue"><a href="#classes-nesteddictexceptions-class-variables-nondictreplacementvalue"><pre>NonDictReplacementValue</pre></a></h5>

Inappropriate argument type.

<h5 id="classes-nesteddictexceptions-class-variables-valuedoesnotexist"><a href="#classes-nesteddictexceptions-class-variables-valuedoesnotexist"><pre>ValueDoesNotExist</pre></a></h5>

Mapping key not found.

<h5 id="classes-nesteddictexceptions-class-variables-valueisalistandindexisoutofrange"><a href="#classes-nesteddictexceptions-class-variables-valueisalistandindexisoutofrange"><pre>ValueIsAListAndIndexIsOutOfRange</pre></a></h5>

Sequence index out of range.

<h5 id="classes-nesteddictexceptions-class-variables-valuenotadict"><a href="#classes-nesteddictexceptions-class-variables-valuenotadict"><pre>ValueNotADict</pre></a></h5>

Inappropriate argument type.

<h5 id="classes-nesteddictexceptions-class-variables-valuenotalist"><a href="#classes-nesteddictexceptions-class-variables-valuenotalist"><pre>ValueNotAList</pre></a></h5>

Inappropriate argument type.

<h3 id="classes-newcliexceptions"><a href="#classes-newcliexceptions"><pre>NewCLIExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-newcliexceptions-ancestors-in-mro"><a href="#classes-newcliexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-newcliexceptions-descendants"><a href="#classes-newcliexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.TerminalTooThin

<h3 id="classes-newconfigexceptions"><a href="#classes-newconfigexceptions"><pre>NewConfigExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-newconfigexceptions-ancestors-in-mro"><a href="#classes-newconfigexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-newconfigexceptions-descendants"><a href="#classes-newconfigexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.ConfigFileExtensionNotSupported
- alltheutils.exceptions.MissingInstanceConfigValue

<h3 id="classes-newnesteddictexceptions"><a href="#classes-newnesteddictexceptions"><pre>NewNestedDictExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-newnesteddictexceptions-ancestors-in-mro"><a href="#classes-newnesteddictexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-newnesteddictexceptions-descendants"><a href="#classes-newnesteddictexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList

<h3 id="classes-prerequisitenotfound"><a href="#classes-prerequisitenotfound"><pre>PrerequisiteNotFound</pre></a></h3>

```python
(prerequisite: str, inst_instruction: str | None = None, **kwargs: dict[str, typing.Any])
```

Base class for all custom exceptions.

Raised when a prerequisite is needed by the program, but is not installed in the machine.

Args:
- prerequisite (`str`): Name of the prerequisite.
- inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.

<h4 id="classes-prerequisitenotfound-ancestors-in-mro"><a href="#classes-prerequisitenotfound-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-terminaltoothin"><a href="#classes-terminaltoothin"><pre>TerminalTooThin</pre></a></h3>

```python
(min_width: int)
```

Base class for all custom exceptions.

Raised when terminal is too thin for content to be rendered.

Args:
- min_width (`int`): Required minimum terminal width.

<h4 id="classes-terminaltoothin-ancestors-in-mro"><a href="#classes-terminaltoothin-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h3 id="classes-validationerror"><a href="#classes-validationerror"><pre>ValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-validationerror-ancestors-in-mro"><a href="#classes-validationerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-validationerror-descendants"><a href="#classes-validationerror-descendants">Descendants</a></h4>

- alltheutils.exceptions.ArgumentsNotFollowingSpec
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.CommonValidationError
- alltheutils.exceptions.FileNotFound
- alltheutils.exceptions.MissingInstanceConfigValue

---

[← Go back to `alltheutils`](./index.md)
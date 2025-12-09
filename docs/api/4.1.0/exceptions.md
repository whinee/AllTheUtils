<h1 id=""><a href="#">Module alltheutils.exceptions</a></h1>

[← Go back to `alltheutils`](./index.md)

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

<h4 id="classes-argumentsnotfollowingspec-class-variables"><a href="#classes-argumentsnotfollowingspec-class-variables">Class variables</a></h4>

<h5 id="classes-argumentsnotfollowingspec-class-variables-details"><a href="#classes-argumentsnotfollowingspec-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-argumentsnotfollowingspec-class-variables-message"><a href="#classes-argumentsnotfollowingspec-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-bumpversionexceptions"><a href="#classes-bumpversionexceptions"><pre>BumpVersionExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-bumpversionexceptions-ancestors-in-mro"><a href="#classes-bumpversionexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-bumpversionexceptions-descendants"><a href="#classes-bumpversionexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.BumpVersionNoPrerelease
- alltheutils.exceptions.BumpVersionPartUnknown

<h3 id="classes-bumpversionnoprerelease"><a href="#classes-bumpversionnoprerelease"><pre>BumpVersionNoPrerelease</pre></a></h3>

Inappropriate argument value (of correct type).

<h4 id="classes-bumpversionnoprerelease-ancestors-in-mro"><a href="#classes-bumpversionnoprerelease-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.BumpVersionExceptions
- builtins.ValueError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-bumpversionnoprerelease-class-variables"><a href="#classes-bumpversionnoprerelease-class-variables">Class variables</a></h4>

<h5 id="classes-bumpversionnoprerelease-class-variables-details"><a href="#classes-bumpversionnoprerelease-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-bumpversionnoprerelease-class-variables-message"><a href="#classes-bumpversionnoprerelease-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-bumpversionpartunknown"><a href="#classes-bumpversionpartunknown"><pre>BumpVersionPartUnknown</pre></a></h3>

```python
(part: str)
```

Inappropriate argument value (of correct type).

<h4 id="classes-bumpversionpartunknown-ancestors-in-mro"><a href="#classes-bumpversionpartunknown-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.BumpVersionExceptions
- builtins.ValueError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-bumpversionpartunknown-class-variables"><a href="#classes-bumpversionpartunknown-class-variables">Class variables</a></h4>

<h5 id="classes-bumpversionpartunknown-class-variables-details"><a href="#classes-bumpversionpartunknown-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-bumpversionpartunknown-class-variables-message"><a href="#classes-bumpversionpartunknown-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

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
- alltheutils.exceptions.CLIExceptions
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-clicommandnotfound-class-variables"><a href="#classes-clicommandnotfound-class-variables">Class variables</a></h4>

<h5 id="classes-clicommandnotfound-class-variables-details"><a href="#classes-clicommandnotfound-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-clicommandnotfound-class-variables-message"><a href="#classes-clicommandnotfound-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-clicommonerror"><a href="#classes-clicommonerror"><pre>CLICommonError</pre></a></h3>

```python
(message: str, details: str | None = None)
```

Base class for all custom exceptions.

<h4 id="classes-clicommonerror-ancestors-in-mro"><a href="#classes-clicommonerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIExceptions
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-clicommonerror-class-variables"><a href="#classes-clicommonerror-class-variables">Class variables</a></h4>

<h5 id="classes-clicommonerror-class-variables-details"><a href="#classes-clicommonerror-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-clicommonerror-class-variables-message"><a href="#classes-clicommonerror-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-cliexceptions"><a href="#classes-cliexceptions"><pre>CLIExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-cliexceptions-ancestors-in-mro"><a href="#classes-cliexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-cliexceptions-descendants"><a href="#classes-cliexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.CLICommonError
- alltheutils.exceptions.CLIValidationError
- alltheutils.exceptions.TerminalTooThin

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
- alltheutils.exceptions.CLIExceptions
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.exceptions.ValidationError
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-clioptionrequired-class-variables"><a href="#classes-clioptionrequired-class-variables">Class variables</a></h4>

<h5 id="classes-clioptionrequired-class-variables-details"><a href="#classes-clioptionrequired-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-clioptionrequired-class-variables-message"><a href="#classes-clioptionrequired-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-clivalidationerror"><a href="#classes-clivalidationerror"><pre>CLIValidationError</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-clivalidationerror-ancestors-in-mro"><a href="#classes-clivalidationerror-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIExceptions
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

<h4 id="classes-commonvalidationerror-class-variables"><a href="#classes-commonvalidationerror-class-variables">Class variables</a></h4>

<h5 id="classes-commonvalidationerror-class-variables-details"><a href="#classes-commonvalidationerror-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-commonvalidationerror-class-variables-message"><a href="#classes-commonvalidationerror-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-configexceptions"><a href="#classes-configexceptions"><pre>ConfigExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-configexceptions-ancestors-in-mro"><a href="#classes-configexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-configexceptions-descendants"><a href="#classes-configexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.ConfigFileExtensionNotSupported
- alltheutils.exceptions.MissingInstanceConfigValue

<h3 id="classes-configfileextensionnotsupported"><a href="#classes-configfileextensionnotsupported"><pre>ConfigFileExtensionNotSupported</pre></a></h3>

```python
(ext: str)
```

Method or function hasn't been implemented yet.

Raise when extension `{ext}` is not supported.

Args:
    ext (`str`): The extension not supported.

<h4 id="classes-configfileextensionnotsupported-ancestors-in-mro"><a href="#classes-configfileextensionnotsupported-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ConfigExceptions
- alltheutils.exceptions.NewConfigExceptions
- builtins.NotImplementedError
- builtins.RuntimeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-configfileextensionnotsupported-class-variables"><a href="#classes-configfileextensionnotsupported-class-variables">Class variables</a></h4>

<h5 id="classes-configfileextensionnotsupported-class-variables-details"><a href="#classes-configfileextensionnotsupported-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-configfileextensionnotsupported-class-variables-message"><a href="#classes-configfileextensionnotsupported-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

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

<h4 id="classes-filenotfound-class-variables"><a href="#classes-filenotfound-class-variables">Class variables</a></h4>

<h5 id="classes-filenotfound-class-variables-details"><a href="#classes-filenotfound-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-filenotfound-class-variables-message"><a href="#classes-filenotfound-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-loadlanguagetextslanguagenotfound"><a href="#classes-loadlanguagetextslanguagenotfound"><pre>LoadLanguageTextsLanguageNotFound</pre></a></h3>

```python
(lang: str)
```

Mapping key not found.

<h4 id="classes-loadlanguagetextslanguagenotfound-ancestors-in-mro"><a href="#classes-loadlanguagetextslanguagenotfound-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-loadlanguagetextslanguagenotfound-class-variables"><a href="#classes-loadlanguagetextslanguagenotfound-class-variables">Class variables</a></h4>

<h5 id="classes-loadlanguagetextslanguagenotfound-class-variables-details"><a href="#classes-loadlanguagetextslanguagenotfound-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-loadlanguagetextslanguagenotfound-class-variables-message"><a href="#classes-loadlanguagetextslanguagenotfound-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-missinginstanceconfigvalue"><a href="#classes-missinginstanceconfigvalue"><pre>MissingInstanceConfigValue</pre></a></h3>

```python
(func_name: str, missing_constants: list[str])
```

Mapping key not found.

<h4 id="classes-missinginstanceconfigvalue-ancestors-in-mro"><a href="#classes-missinginstanceconfigvalue-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.ConfigExceptions
- alltheutils.exceptions.NewConfigExceptions
- alltheutils.exceptions.ValidationError
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-missinginstanceconfigvalue-class-variables"><a href="#classes-missinginstanceconfigvalue-class-variables">Class variables</a></h4>

<h5 id="classes-missinginstanceconfigvalue-class-variables-details"><a href="#classes-missinginstanceconfigvalue-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-missinginstanceconfigvalue-class-variables-message"><a href="#classes-missinginstanceconfigvalue-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-ndnondictreplacementvalue"><a href="#classes-ndnondictreplacementvalue"><pre>NDNonDictReplacementValue</pre></a></h3>

Inappropriate argument type.

<h4 id="classes-ndnondictreplacementvalue-ancestors-in-mro"><a href="#classes-ndnondictreplacementvalue-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NestedDictExceptions
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-ndnondictreplacementvalue-class-variables"><a href="#classes-ndnondictreplacementvalue-class-variables">Class variables</a></h4>

<h5 id="classes-ndnondictreplacementvalue-class-variables-details"><a href="#classes-ndnondictreplacementvalue-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-ndnondictreplacementvalue-class-variables-message"><a href="#classes-ndnondictreplacementvalue-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-ndvaluedoesnotexist"><a href="#classes-ndvaluedoesnotexist"><pre>NDValueDoesNotExist</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Mapping key not found.

<h4 id="classes-ndvaluedoesnotexist-ancestors-in-mro"><a href="#classes-ndvaluedoesnotexist-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NestedDictExceptions
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.KeyError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-ndvaluedoesnotexist-class-variables"><a href="#classes-ndvaluedoesnotexist-class-variables">Class variables</a></h4>

<h5 id="classes-ndvaluedoesnotexist-class-variables-details"><a href="#classes-ndvaluedoesnotexist-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-ndvaluedoesnotexist-class-variables-message"><a href="#classes-ndvaluedoesnotexist-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-ndvalueisalistandindexisoutofrange"><a href="#classes-ndvalueisalistandindexisoutofrange"><pre>NDValueIsAListAndIndexIsOutOfRange</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Sequence index out of range.

<h4 id="classes-ndvalueisalistandindexisoutofrange-ancestors-in-mro"><a href="#classes-ndvalueisalistandindexisoutofrange-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NestedDictExceptions
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.IndexError
- builtins.LookupError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-ndvalueisalistandindexisoutofrange-class-variables"><a href="#classes-ndvalueisalistandindexisoutofrange-class-variables">Class variables</a></h4>

<h5 id="classes-ndvalueisalistandindexisoutofrange-class-variables-details"><a href="#classes-ndvalueisalistandindexisoutofrange-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-ndvalueisalistandindexisoutofrange-class-variables-message"><a href="#classes-ndvalueisalistandindexisoutofrange-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-ndvaluenotadict"><a href="#classes-ndvaluenotadict"><pre>NDValueNotADict</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-ndvaluenotadict-ancestors-in-mro"><a href="#classes-ndvaluenotadict-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NestedDictExceptions
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-ndvaluenotadict-class-variables"><a href="#classes-ndvaluenotadict-class-variables">Class variables</a></h4>

<h5 id="classes-ndvaluenotadict-class-variables-details"><a href="#classes-ndvaluenotadict-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-ndvaluenotadict-class-variables-message"><a href="#classes-ndvaluenotadict-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-ndvaluenotalist"><a href="#classes-ndvaluenotalist"><pre>NDValueNotAList</pre></a></h3>

```python
(keys: list[str], idx: int)
```

Inappropriate argument type.

<h4 id="classes-ndvaluenotalist-ancestors-in-mro"><a href="#classes-ndvaluenotalist-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.NestedDictExceptions
- alltheutils.exceptions.NewNestedDictExceptions
- builtins.TypeError
- builtins.Exception
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-ndvaluenotalist-class-variables"><a href="#classes-ndvaluenotalist-class-variables">Class variables</a></h4>

<h5 id="classes-ndvaluenotalist-class-variables-details"><a href="#classes-ndvaluenotalist-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-ndvaluenotalist-class-variables-message"><a href="#classes-ndvaluenotalist-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-nesteddictexceptions"><a href="#classes-nesteddictexceptions"><pre>NestedDictExceptions</pre></a></h3>

```python
(*args, **kwargs)
```

Common base class for all exceptions

<h4 id="classes-nesteddictexceptions-ancestors-in-mro"><a href="#classes-nesteddictexceptions-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- builtins.BaseException

<h4 id="classes-nesteddictexceptions-descendants"><a href="#classes-nesteddictexceptions-descendants">Descendants</a></h4>

- alltheutils.exceptions.NDNonDictReplacementValue
- alltheutils.exceptions.NDValueDoesNotExist
- alltheutils.exceptions.NDValueIsAListAndIndexIsOutOfRange
- alltheutils.exceptions.NDValueNotADict
- alltheutils.exceptions.NDValueNotAList

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
- alltheutils.exceptions.NDValueIsAListAndIndexIsOutOfRange
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

<h4 id="classes-prerequisitenotfound-class-variables"><a href="#classes-prerequisitenotfound-class-variables">Class variables</a></h4>

<h5 id="classes-prerequisitenotfound-class-variables-details"><a href="#classes-prerequisitenotfound-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-prerequisitenotfound-class-variables-message"><a href="#classes-prerequisitenotfound-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

<h3 id="classes-terminaltoothin"><a href="#classes-terminaltoothin"><pre>TerminalTooThin</pre></a></h3>

```python
(min_width: int)
```

Base class for all custom exceptions.

Raised when terminal is too thin for content to be rendered.

Args:
- min_width (`int`): Required minimum terminal width.

<h4 id="classes-terminaltoothin-ancestors-in-mro"><a href="#classes-terminaltoothin-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.exceptions.CLIExceptions
- alltheutils.exceptions.NewCLIExceptions
- alltheutils.base_exceptions.CustomBaseException
- builtins.BaseException

<h4 id="classes-terminaltoothin-class-variables"><a href="#classes-terminaltoothin-class-variables">Class variables</a></h4>

<h5 id="classes-terminaltoothin-class-variables-details"><a href="#classes-terminaltoothin-class-variables-details"><pre>details</pre></a></h5>

```python
str | None
```

The type of the None singleton.

<h5 id="classes-terminaltoothin-class-variables-message"><a href="#classes-terminaltoothin-class-variables-message"><pre>message</pre></a></h5>

```python
str
```

The type of the None singleton.

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
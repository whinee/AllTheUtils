<h1 id=""><a href="#">Module alltheutils.cli.dataclasses</a></h1>

[← Go back to `alltheutils.cli`](./index.md)

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-cliconfig"><a href="#classes-cliconfig"><pre>CLIConfig</pre></a></h3>

```python
(**data: Any)
```

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

<h4 id="classes-cliconfig-ancestors-in-mro"><a href="#classes-cliconfig-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-cliconfig-class-variables"><a href="#classes-cliconfig-class-variables">Class variables</a></h4>

<h5 id="classes-cliconfig-class-variables-commands"><a href="#classes-cliconfig-class-variables-commands"><pre>commands</pre></a></h5>

```python
dict[str, alltheutils.cli.dataclasses.CommandSchema]
```

<h5 id="classes-cliconfig-class-variables-group_command_params"><a href="#classes-cliconfig-class-variables-group_command_params"><pre>group_command_params</pre></a></h5>

```python
alltheutils.cli.dataclasses.CLIGroupCommandParamSchema
```

<h5 id="classes-cliconfig-class-variables-model_config"><a href="#classes-cliconfig-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-cligroupcommandparamschema"><a href="#classes-cligroupcommandparamschema"><pre>CLIGroupCommandParamSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-cligroupcommandparamschema-ancestors-in-mro"><a href="#classes-cligroupcommandparamschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-cligroupcommandparamschema-class-variables"><a href="#classes-cligroupcommandparamschema-class-variables">Class variables</a></h4>

<h5 id="classes-cligroupcommandparamschema-class-variables-add_help_option"><a href="#classes-cligroupcommandparamschema-class-variables-add_help_option"><pre>add_help_option</pre></a></h5>

```python
bool
```

By default each command registers a `--help` option. This can be disabled by this parameter.

<h5 id="classes-cligroupcommandparamschema-class-variables-cls"><a href="#classes-cligroupcommandparamschema-class-variables-cls"><pre>cls</pre></a></h5>

```python
type[click.core.Command] | None
```

<h5 id="classes-cligroupcommandparamschema-class-variables-context_settings"><a href="#classes-cligroupcommandparamschema-class-variables-context_settings"><pre>context_settings</pre></a></h5>

```python
dict[str, typing.Any] | None
```

An optional dictionary with defaults that are passed to the context object.

<h5 id="classes-cligroupcommandparamschema-class-variables-deprecated"><a href="#classes-cligroupcommandparamschema-class-variables-deprecated"><pre>deprecated</pre></a></h5>

```python
bool
```

If `True` or non-empty string, issues a message indicating that the command is deprecated and highlights its deprecation in --help. The message can be customized by using a string as the value.

<h5 id="classes-cligroupcommandparamschema-class-variables-epilog"><a href="#classes-cligroupcommandparamschema-class-variables-epilog"><pre>epilog</pre></a></h5>

```python
str | None
```

Like the help string but it's printed at the end of the help page after everything else.

<h5 id="classes-cligroupcommandparamschema-class-variables-help"><a href="#classes-cligroupcommandparamschema-class-variables-help"><pre>help</pre></a></h5>

```python
str | None
```

The help string to use for this command.

<h5 id="classes-cligroupcommandparamschema-class-variables-hidden"><a href="#classes-cligroupcommandparamschema-class-variables-hidden"><pre>hidden</pre></a></h5>

```python
bool
```

Hide this command from help outputs.

<h5 id="classes-cligroupcommandparamschema-class-variables-model_config"><a href="#classes-cligroupcommandparamschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-cligroupcommandparamschema-class-variables-name"><a href="#classes-cligroupcommandparamschema-class-variables-name"><pre>name</pre></a></h5>

```python
str | collections.abc.Callable[..., typing.Any] | None
```

The name of the command to use unless a group overrides it.

<h5 id="classes-cligroupcommandparamschema-class-variables-no_args_is_help"><a href="#classes-cligroupcommandparamschema-class-variables-no_args_is_help"><pre>no_args_is_help</pre></a></h5>

```python
bool
```

This controls what happens if no arguments are provided. This option is disabled by default. If enabled this will add `--help` as argument if no arguments are passed

<h5 id="classes-cligroupcommandparamschema-class-variables-options_metavar"><a href="#classes-cligroupcommandparamschema-class-variables-options_metavar"><pre>options_metavar</pre></a></h5>

```python
str | None
```

<h5 id="classes-cligroupcommandparamschema-class-variables-params"><a href="#classes-cligroupcommandparamschema-class-variables-params"><pre>params</pre></a></h5>

```python
list[click.core.Parameter] | None
```

The parameters to register with this command. This can be either :class:`Option` or :class:`Argument` objects.

<h5 id="classes-cligroupcommandparamschema-class-variables-short_help"><a href="#classes-cligroupcommandparamschema-class-variables-short_help"><pre>short_help</pre></a></h5>

```python
str | None
```

The short help to use for this command. This is shown on the command listing of the parent command.

<h3 id="classes-clihelpschema"><a href="#classes-clihelpschema"><pre>CLIHelpSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-clihelpschema-ancestors-in-mro"><a href="#classes-clihelpschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-clihelpschema-class-variables"><a href="#classes-clihelpschema-class-variables">Class variables</a></h4>

<h5 id="classes-clihelpschema-class-variables-model_config"><a href="#classes-clihelpschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-clihelpschema-class-variables-overview"><a href="#classes-clihelpschema-class-variables-overview"><pre>overview</pre></a></h5>

```python
str
```

<h3 id="classes-commandargumentshelpschema"><a href="#classes-commandargumentshelpschema"><pre>CommandArgumentsHelpSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandargumentshelpschema-ancestors-in-mro"><a href="#classes-commandargumentshelpschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandargumentshelpschema-class-variables"><a href="#classes-commandargumentshelpschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandargumentshelpschema-class-variables-example"><a href="#classes-commandargumentshelpschema-class-variables-example"><pre>example</pre></a></h5>

```python
str | None
```

Example of string that can be passed as an argument.

<h5 id="classes-commandargumentshelpschema-class-variables-help"><a href="#classes-commandargumentshelpschema-class-variables-help"><pre>help</pre></a></h5>

```python
str
```

Main help string.

<h5 id="classes-commandargumentshelpschema-class-variables-model_config"><a href="#classes-commandargumentshelpschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-commandargumentskwargsschema"><a href="#classes-commandargumentskwargsschema"><pre>CommandArgumentsKwargsSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandargumentskwargsschema-ancestors-in-mro"><a href="#classes-commandargumentskwargsschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandargumentskwargsschema-class-variables"><a href="#classes-commandargumentskwargsschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandargumentskwargsschema-class-variables-callback"><a href="#classes-commandargumentskwargsschema-class-variables-callback"><pre>callback</pre></a></h5>

```python
Callable[[click.core.Context, click.core.Parameter, typing.Any], typing.Any] | None
```

A function to further process or validate the value after type conversion. It is called as `f(ctx, param, value)` and must return the value. It is called for all sources, including prompts.

<h5 id="classes-commandargumentskwargsschema-class-variables-default"><a href="#classes-commandargumentskwargsschema-class-variables-default"><pre>default</pre></a></h5>

```python
Any | Callable[[], typing.Any] | None
```

The default value if omitted. This can also be a callable, in which case it's invoked when the default is needed without any arguments.

<h5 id="classes-commandargumentskwargsschema-class-variables-envvar"><a href="#classes-commandargumentskwargsschema-class-variables-envvar"><pre>envvar</pre></a></h5>

```python
str | Sequence[str] | None
```

A string or list of strings that are environment variables that should be checked.

<h5 id="classes-commandargumentskwargsschema-class-variables-expose_value"><a href="#classes-commandargumentskwargsschema-class-variables-expose_value"><pre>expose_value</pre></a></h5>

```python
bool
```

If this is `True` then the value is passed onwards to the command callback and stored on the context, otherwise it's skipped.

<h5 id="classes-commandargumentskwargsschema-class-variables-is_eager"><a href="#classes-commandargumentskwargsschema-class-variables-is_eager"><pre>is_eager</pre></a></h5>

```python
bool
```

Eager values are processed before non eager ones.  This should not be set for arguments or it will inverse the order of processing.

<h5 id="classes-commandargumentskwargsschema-class-variables-metavar"><a href="#classes-commandargumentskwargsschema-class-variables-metavar"><pre>metavar</pre></a></h5>

```python
str | None
```

How the value is represented in the help page.

<h5 id="classes-commandargumentskwargsschema-class-variables-model_config"><a href="#classes-commandargumentskwargsschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-commandargumentskwargsschema-class-variables-nargs"><a href="#classes-commandargumentskwargsschema-class-variables-nargs"><pre>nargs</pre></a></h5>

```python
int | None
```

The number of arguments to match.  If not `1` the return value is a tuple instead of single value.  The default for nargs is `1` (except if the type is a tuple, then it's the arity of the tuple). If `nargs=-1`, all remaining parameters are collected.

<h5 id="classes-commandargumentskwargsschema-class-variables-required"><a href="#classes-commandargumentskwargsschema-class-variables-required"><pre>required</pre></a></h5>

```python
bool
```

Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown.

<h5 id="classes-commandargumentskwargsschema-class-variables-shell_complete"><a href="#classes-commandargumentskwargsschema-class-variables-shell_complete"><pre>shell_complete</pre></a></h5>

```python
Callable[[click.core.Context, click.core.Parameter, str], list[click.shell_completion.CompletionItem] | list[str]] | None
```

A function that returns custom shell completions. Used instead of the param's type completion if given. Takes `ctx, param, incomplete` and must return a list of `click.shell_completion.CompletionItem` or a list of strings.

<h5 id="classes-commandargumentskwargsschema-class-variables-type"><a href="#classes-commandargumentskwargsschema-class-variables-type"><pre>type</pre></a></h5>

```python
click.types.ParamType | Any | None
```

<h3 id="classes-commandargumentsschema"><a href="#classes-commandargumentsschema"><pre>CommandArgumentsSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandargumentsschema-ancestors-in-mro"><a href="#classes-commandargumentsschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandargumentsschema-class-variables"><a href="#classes-commandargumentsschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandargumentsschema-class-variables-args"><a href="#classes-commandargumentsschema-class-variables-args"><pre>args</pre></a></h5>

```python
list[str]
```

Arguments to provide to `click.core.Argument`.

<h5 id="classes-commandargumentsschema-class-variables-help"><a href="#classes-commandargumentsschema-class-variables-help"><pre>help</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandArgumentsHelpSchema
```

<h5 id="classes-commandargumentsschema-class-variables-kwargs"><a href="#classes-commandargumentsschema-class-variables-kwargs"><pre>kwargs</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandArgumentsKwargsSchema
```

Keyword arguments to provide to `click.core.Argument`.

<h5 id="classes-commandargumentsschema-class-variables-model_config"><a href="#classes-commandargumentsschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-commandhelpschema"><a href="#classes-commandhelpschema"><pre>CommandHelpSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandhelpschema-ancestors-in-mro"><a href="#classes-commandhelpschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandhelpschema-class-variables"><a href="#classes-commandhelpschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandhelpschema-class-variables-description"><a href="#classes-commandhelpschema-class-variables-description"><pre>description</pre></a></h5>

```python
str
```

<h5 id="classes-commandhelpschema-class-variables-model_config"><a href="#classes-commandhelpschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-commandhelpschema-class-variables-overview"><a href="#classes-commandhelpschema-class-variables-overview"><pre>overview</pre></a></h5>

```python
str | None
```

<h3 id="classes-commandkwargsschema"><a href="#classes-commandkwargsschema"><pre>CommandKwargsSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandkwargsschema-ancestors-in-mro"><a href="#classes-commandkwargsschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandkwargsschema-class-variables"><a href="#classes-commandkwargsschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandkwargsschema-class-variables-add_help_option"><a href="#classes-commandkwargsschema-class-variables-add_help_option"><pre>add_help_option</pre></a></h5>

```python
bool
```

By default each command registers a `--help` option. This can be disabled by this parameter.

<h5 id="classes-commandkwargsschema-class-variables-context_settings"><a href="#classes-commandkwargsschema-class-variables-context_settings"><pre>context_settings</pre></a></h5>

```python
MutableMapping[str, typing.Any] | None
```

An optional dictionary with defaults that are passed to the context object.

<h5 id="classes-commandkwargsschema-class-variables-deprecated"><a href="#classes-commandkwargsschema-class-variables-deprecated"><pre>deprecated</pre></a></h5>

```python
bool
```

issues a message indicating that the command is deprecated.

<h5 id="classes-commandkwargsschema-class-variables-epilog"><a href="#classes-commandkwargsschema-class-variables-epilog"><pre>epilog</pre></a></h5>

```python
str | None
```

Like the help string but it's printed at the end of the help page after everything else.

<h5 id="classes-commandkwargsschema-class-variables-help"><a href="#classes-commandkwargsschema-class-variables-help"><pre>help</pre></a></h5>

```python
str | None
```

The help string to use for this command.

<h5 id="classes-commandkwargsschema-class-variables-hidden"><a href="#classes-commandkwargsschema-class-variables-hidden"><pre>hidden</pre></a></h5>

```python
bool
```

Hide this command from help outputs.

<h5 id="classes-commandkwargsschema-class-variables-model_config"><a href="#classes-commandkwargsschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-commandkwargsschema-class-variables-name"><a href="#classes-commandkwargsschema-class-variables-name"><pre>name</pre></a></h5>

```python
str | None
```

The name of the command to use unless a group overrides it.

<h5 id="classes-commandkwargsschema-class-variables-no_args_is_help"><a href="#classes-commandkwargsschema-class-variables-no_args_is_help"><pre>no_args_is_help</pre></a></h5>

```python
bool
```

this controls what happens if no arguments are provided. This option is disabled by default. If enabled this will add `--help` as argument if no arguments are passed.

<h5 id="classes-commandkwargsschema-class-variables-options_metavar"><a href="#classes-commandkwargsschema-class-variables-options_metavar"><pre>options_metavar</pre></a></h5>

```python
str | None
```

The metavar displayed for options in the help page.

<h5 id="classes-commandkwargsschema-class-variables-params"><a href="#classes-commandkwargsschema-class-variables-params"><pre>params</pre></a></h5>

```python
list[click.core.Parameter] | None
```

The parameters to register with this command. This can be either `Option` or `Argument` objects.

<h5 id="classes-commandkwargsschema-class-variables-short_help"><a href="#classes-commandkwargsschema-class-variables-short_help"><pre>short_help</pre></a></h5>

```python
str | None
```

The short help to use for this command. This is shown on the command listing of the parent command.

<h3 id="classes-commandoptionshelpschema"><a href="#classes-commandoptionshelpschema"><pre>CommandOptionsHelpSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandoptionshelpschema-ancestors-in-mro"><a href="#classes-commandoptionshelpschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandoptionshelpschema-class-variables"><a href="#classes-commandoptionshelpschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandoptionshelpschema-class-variables-example"><a href="#classes-commandoptionshelpschema-class-variables-example"><pre>example</pre></a></h5>

```python
str | None
```

Example of string that can be passed as an argument

<h5 id="classes-commandoptionshelpschema-class-variables-help"><a href="#classes-commandoptionshelpschema-class-variables-help"><pre>help</pre></a></h5>

```python
str
```

Main help string.

<h5 id="classes-commandoptionshelpschema-class-variables-model_config"><a href="#classes-commandoptionshelpschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-commandoptionskwargsschema"><a href="#classes-commandoptionskwargsschema"><pre>CommandOptionsKwargsSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandoptionskwargsschema-ancestors-in-mro"><a href="#classes-commandoptionskwargsschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandoptionskwargsschema-class-variables"><a href="#classes-commandoptionskwargsschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandoptionskwargsschema-class-variables-allow_from_autoenv"><a href="#classes-commandoptionskwargsschema-class-variables-allow_from_autoenv"><pre>allow_from_autoenv</pre></a></h5>

```python
bool
```

The help string.

<h5 id="classes-commandoptionskwargsschema-class-variables-callback"><a href="#classes-commandoptionskwargsschema-class-variables-callback"><pre>callback</pre></a></h5>

```python
Callable[[click.core.Context, click.core.Parameter, typing.Any], typing.Any]
```

A function to further process or validate the value after type conversion. It is called as `f(ctx, param, value)` and must return the value. It is called for all sources, including prompts.

<h5 id="classes-commandoptionskwargsschema-class-variables-confirmation_prompt"><a href="#classes-commandoptionskwargsschema-class-variables-confirmation_prompt"><pre>confirmation_prompt</pre></a></h5>

```python
bool | str
```

If set to `False`, the user will be prompted for input only when the option was specified as a flag without a value.

<h5 id="classes-commandoptionskwargsschema-class-variables-count"><a href="#classes-commandoptionskwargsschema-class-variables-count"><pre>count</pre></a></h5>

```python
bool
```

This flag makes an option increment an integer.

<h5 id="classes-commandoptionskwargsschema-class-variables-default"><a href="#classes-commandoptionskwargsschema-class-variables-default"><pre>default</pre></a></h5>

```python
Any | Callable[[], typing.Any] | None
```

The default value if omitted. This can also be a callable, in which case it's invoked when the default is needed without any arguments.

<h5 id="classes-commandoptionskwargsschema-class-variables-envvar"><a href="#classes-commandoptionskwargsschema-class-variables-envvar"><pre>envvar</pre></a></h5>

```python
str | Sequence[str] | None
```

A string or list of strings that are environment variables that should be checked.

<h5 id="classes-commandoptionskwargsschema-class-variables-expose_value"><a href="#classes-commandoptionskwargsschema-class-variables-expose_value"><pre>expose_value</pre></a></h5>

```python
bool
```

If this is `True` then the value is passed onwards to the command callback and stored on the context, otherwise it's skipped.

<h5 id="classes-commandoptionskwargsschema-class-variables-flag_value"><a href="#classes-commandoptionskwargsschema-class-variables-flag_value"><pre>flag_value</pre></a></h5>

```python
Any | None
```

If this is set to `True` then the argument is accepted multiple times and recorded.  This is similar to `nargs` in how it works but supports arbitrary number of arguments.

<h5 id="classes-commandoptionskwargsschema-class-variables-help"><a href="#classes-commandoptionskwargsschema-class-variables-help"><pre>help</pre></a></h5>

```python
str | None
```

The help string.

<h5 id="classes-commandoptionskwargsschema-class-variables-hidden"><a href="#classes-commandoptionskwargsschema-class-variables-hidden"><pre>hidden</pre></a></h5>

```python
bool
```

Hide this option from help outputs.

<h5 id="classes-commandoptionskwargsschema-class-variables-hide_input"><a href="#classes-commandoptionskwargsschema-class-variables-hide_input"><pre>hide_input</pre></a></h5>

```python
bool
```

If this is `True` then the input on the prompt will be hidden from the user. This is useful for password input.

<h5 id="classes-commandoptionskwargsschema-class-variables-is_eager"><a href="#classes-commandoptionskwargsschema-class-variables-is_eager"><pre>is_eager</pre></a></h5>

```python
bool
```

Eager values are processed before non eager ones.  This should not be set for arguments or it will inverse the order of processing.

<h5 id="classes-commandoptionskwargsschema-class-variables-is_flag"><a href="#classes-commandoptionskwargsschema-class-variables-is_flag"><pre>is_flag</pre></a></h5>

```python
bool | None
```

Forces this option to act as a flag. The default is auto detection.

<h5 id="classes-commandoptionskwargsschema-class-variables-metavar"><a href="#classes-commandoptionskwargsschema-class-variables-metavar"><pre>metavar</pre></a></h5>

```python
str | None
```

How the value is represented in the help page.

<h5 id="classes-commandoptionskwargsschema-class-variables-model_config"><a href="#classes-commandoptionskwargsschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-commandoptionskwargsschema-class-variables-multiple"><a href="#classes-commandoptionskwargsschema-class-variables-multiple"><pre>multiple</pre></a></h5>

```python
bool
```

<h5 id="classes-commandoptionskwargsschema-class-variables-nargs"><a href="#classes-commandoptionskwargsschema-class-variables-nargs"><pre>nargs</pre></a></h5>

```python
int | None
```

The number of arguments to match.  If not `1` the return value is a tuple instead of single value.  The default for nargs is `1` (except if the type is a tuple, then it's the arity of the tuple). If `nargs=-1`, all remaining parameters are collected.

<h5 id="classes-commandoptionskwargsschema-class-variables-prompt"><a href="#classes-commandoptionskwargsschema-class-variables-prompt"><pre>prompt</pre></a></h5>

```python
bool | str
```

If set to `True` or a non empty string then the user will be prompted for input. If set to `True` the prompt will be the option name capitalized.

<h5 id="classes-commandoptionskwargsschema-class-variables-prompt_required"><a href="#classes-commandoptionskwargsschema-class-variables-prompt_required"><pre>prompt_required</pre></a></h5>

```python
bool
```

<h5 id="classes-commandoptionskwargsschema-class-variables-required"><a href="#classes-commandoptionskwargsschema-class-variables-required"><pre>required</pre></a></h5>

```python
bool
```

Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown.

<h5 id="classes-commandoptionskwargsschema-class-variables-shell_complete"><a href="#classes-commandoptionskwargsschema-class-variables-shell_complete"><pre>shell_complete</pre></a></h5>

```python
Callable[[click.core.Context, click.core.Parameter, str], list[click.shell_completion.CompletionItem] | list[str]] | None
```

A function that returns custom shell completions. Used instead of the param's type completion if given. Takes `ctx, param, incomplete` and must return a list of `click.shell_completion.CompletionItem` or a list of strings.

<h5 id="classes-commandoptionskwargsschema-class-variables-show_choices"><a href="#classes-commandoptionskwargsschema-class-variables-show_choices"><pre>show_choices</pre></a></h5>

```python
bool
```

Show or hide choices if the passed type is a Choice. For example if type is a Choice of either day or week, show_choices is true and text is "Group by" then the prompt will be "Group by (day, week): ".

<h5 id="classes-commandoptionskwargsschema-class-variables-show_default"><a href="#classes-commandoptionskwargsschema-class-variables-show_default"><pre>show_default</pre></a></h5>

```python
bool | str | None
```

Show the default value for this option in its help text. Values are not shown by default, unless `Context.show_default` is `True`. If this value is a string, it shows that string in parentheses instead of the actual value. This is particularly useful for dynamic options. 

For single option boolean flags, the default remains hidden if its value is `False`.

<h5 id="classes-commandoptionskwargsschema-class-variables-show_envvar"><a href="#classes-commandoptionskwargsschema-class-variables-show_envvar"><pre>show_envvar</pre></a></h5>

```python
bool
```

Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown.

<h5 id="classes-commandoptionskwargsschema-class-variables-type"><a href="#classes-commandoptionskwargsschema-class-variables-type"><pre>type</pre></a></h5>

```python
click.types.ParamType | Any | None
```

<h3 id="classes-commandoptionsschema"><a href="#classes-commandoptionsschema"><pre>CommandOptionsSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandoptionsschema-ancestors-in-mro"><a href="#classes-commandoptionsschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandoptionsschema-class-variables"><a href="#classes-commandoptionsschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandoptionsschema-class-variables-args"><a href="#classes-commandoptionsschema-class-variables-args"><pre>args</pre></a></h5>

```python
list[str]
```

Arguments to provide to `click.core.Option`.

<h5 id="classes-commandoptionsschema-class-variables-help"><a href="#classes-commandoptionsschema-class-variables-help"><pre>help</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandOptionsHelpSchema
```

Help strings to show when the help option is invoked.

<h5 id="classes-commandoptionsschema-class-variables-kwargs"><a href="#classes-commandoptionsschema-class-variables-kwargs"><pre>kwargs</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandOptionsKwargsSchema
```

Keyword arguments to provide to `click.core.Option`.

<h5 id="classes-commandoptionsschema-class-variables-model_config"><a href="#classes-commandoptionsschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h3 id="classes-commandschema"><a href="#classes-commandschema"><pre>CommandSchema</pre></a></h3>

```python
(**data: Any)
```

<h4 id="classes-commandschema-ancestors-in-mro"><a href="#classes-commandschema-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- pydantic.main.BaseModel

<h4 id="classes-commandschema-class-variables"><a href="#classes-commandschema-class-variables">Class variables</a></h4>

<h5 id="classes-commandschema-class-variables-args"><a href="#classes-commandschema-class-variables-args"><pre>args</pre></a></h5>

```python
list[str]
```

Arguments to provide to `alltheutils.cli.base.Group.command`.

<h5 id="classes-commandschema-class-variables-arguments"><a href="#classes-commandschema-class-variables-arguments"><pre>arguments</pre></a></h5>

```python
dict[str, alltheutils.cli.dataclasses.CommandArgumentsSchema]
```

Arguments to attach to the command.

<h5 id="classes-commandschema-class-variables-help"><a href="#classes-commandschema-class-variables-help"><pre>help</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandHelpSchema
```

Help strings to show when the help option is invoked

<h5 id="classes-commandschema-class-variables-kwargs"><a href="#classes-commandschema-class-variables-kwargs"><pre>kwargs</pre></a></h5>

```python
alltheutils.cli.dataclasses.CommandKwargsSchema
```

Keyword arguments to provide to `alltheutils.cli.base.Group.command`.

<h5 id="classes-commandschema-class-variables-model_config"><a href="#classes-commandschema-class-variables-model_config"><pre>model_config</pre></a></h5>

<h5 id="classes-commandschema-class-variables-options"><a href="#classes-commandschema-class-variables-options"><pre>options</pre></a></h5>

```python
dict[str, alltheutils.cli.dataclasses.CommandOptionsSchema]
```

Options to attach to the command.

---

[← Go back to `alltheutils.cli`](./index.md)
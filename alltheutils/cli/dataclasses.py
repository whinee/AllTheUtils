from collections.abc import Callable, MutableMapping, Sequence
from typing import Any, Optional, Union

from click.core import Command, Context, Parameter
from click.shell_completion import CompletionItem
from click.types import ParamType
from pydantic import BaseModel, ConfigDict, Field

from alltheutils.cli._base import show_help

# __pdoc__: dict[str, bool | str] = {
#     f"{cls.__name__}.{method}": False
#     for method in ("BaseModel.", "model_computed_fields", "model_config")
#     for cls in (BaseModel, *BaseModel.__subclasses__())
# }
__pdoc__: dict[str, bool | str] = {}


class CommandKwargsSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandKwargsSchema"] = ""

    # Arguments to provide to `click.core.Command`
    name: Optional[str] = None
    __pdoc__["CommandKwargsSchema.name"] = (
        """The name of the command to use unless a group overrides it."""
    )

    context_settings: Optional[MutableMapping[str, Any]] = None
    __pdoc__["CommandKwargsSchema.context_settings"] = (
        """An optional dictionary with defaults that are passed to the context object."""
    )

    # callback: Optional[Callable[..., Any]] = None
    # __pdoc__["CommandKwargsSchema.callback"] = (
    #     """The callback to invoke. This is optional."""
    # )

    params: Optional[list[Parameter]] = None
    __pdoc__["CommandKwargsSchema.params"] = (
        """The parameters to register with this command. This can be either `Option` or `Argument` objects."""
    )

    # help: Optional[str] = None
    # __pdoc__["CommandKwargsSchema.help"] = (
    #     """The help string to use for this command."""
    # )

    epilog: Optional[str] = None
    __pdoc__["CommandKwargsSchema.epilog"] = (
        """Like the help string but it's printed at the end of the help page after everything else."""
    )

    # short_help: Optional[str] = None
    # __pdoc__["CommandKwargsSchema.short_help"] = (
    #     """The short help to use for this command. This is shown on the command listing of the parent command."""
    # )

    options_metavar: Optional[str] = "[OPTIONS]"
    __pdoc__["CommandKwargsSchema.options_metavar"] = (
        """The metavar displayed for options in the help page."""
    )

    # add_help_option: bool = True
    # __pdoc__["CommandKwargsSchema.add_help_option"] = (
    #     """By default each command registers a `--help` option. This can be disabled by this parameter."""
    # )

    no_args_is_help: bool = False
    __pdoc__["CommandKwargsSchema.no_args_is_help"] = (
        """this controls what happens if no arguments are provided. This option is disabled by default. If enabled this will add `--help` as argument if no arguments are passed."""
    )

    hidden: bool = False
    __pdoc__["CommandKwargsSchema.hidden"] = """Hide this command from help outputs."""

    deprecated: bool = False
    __pdoc__["CommandKwargsSchema.deprecated"] = (
        """issues a message indicating that the command is deprecated."""
    )


class CommandHelpSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandHelpSchema"] = ""

    # Help string to show when the help option is invoked in the group command
    # and not the command itself
    overview: Optional[str] = None
    # Help string to show when the help option is invoked in the command itself
    description: str


class CommandArgumentsKwargsSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandArgumentsKwargsSchema"] = ""

    # Arguments to provide to `click.core.Parameter`
    type: Optional[Union[ParamType, Any]] = None
    __pdoc__["CommandOptionsKwargsSchema.help"] = (
        """The type that should be used.  Either a `ParamType` or a Python type. The latter is converted into the former automatically if supported."""
    )

    required: bool = False
    __pdoc__["CommandArgumentsKwargsSchema.required"] = (
        """Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown."""
    )

    default: Optional[Union[Any, Callable[[], Any]]] = None
    __pdoc__["CommandArgumentsKwargsSchema.default"] = (
        """The default value if omitted. This can also be a callable, in which case it's invoked when the default is needed without any arguments."""
    )

    callback: Optional[Callable[[Context, Parameter, Any], Any]] = None
    __pdoc__["CommandArgumentsKwargsSchema.callback"] = (
        """A function to further process or validate the value after type conversion. It is called as `f(ctx, param, value)` and must return the value. It is called for all sources, including prompts."""
    )

    nargs: Optional[int] = None
    __pdoc__["CommandArgumentsKwargsSchema.nargs"] = (
        """The number of arguments to match.  If not `1` the return value is a tuple instead of single value.  The default for nargs is `1` (except if the type is a tuple, then it's the arity of the tuple). If `nargs=-1`, all remaining parameters are collected."""
    )

    metavar: Optional[str] = None
    __pdoc__["CommandArgumentsKwargsSchema.metavar"] = (
        """How the value is represented in the help page."""
    )

    expose_value: bool = True
    __pdoc__["CommandArgumentsKwargsSchema.expose_value"] = (
        """If this is `True` then the value is passed onwards to the command callback and stored on the context, otherwise it's skipped."""
    )

    is_eager: bool = False
    __pdoc__["CommandArgumentsKwargsSchema.is_eager"] = (
        """Eager values are processed before non eager ones.  This should not be set for arguments or it will inverse the order of processing."""
    )

    envvar: Optional[Union[str, Sequence[str]]] = None
    __pdoc__["CommandArgumentsKwargsSchema.envvar"] = (
        """A string or list of strings that are environment variables that should be checked."""
    )

    shell_complete: Optional[
        Callable[
            [Context, Parameter, str],
            Union[list["CompletionItem"], list[str]],
        ]
    ] = None
    __pdoc__["CommandArgumentsKwargsSchema.shell_complete"] = (
        """A function that returns custom shell completions. Used instead of the param's type completion if given. Takes `ctx, param, incomplete` and must return a list of `click.shell_completion.CompletionItem` or a list of strings."""
    )


class CommandArgumentsHelpSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandArgumentsHelpSchema"] = ""

    help: str
    __pdoc__["CommandArgumentsHelpSchema.help"] = """Main help string."""

    example: Optional[str] = None
    __pdoc__["CommandArgumentsHelpSchema.example"] = (
        """Example of string that can be passed as an argument."""
    )


class CommandArgumentsSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandArgumentsSchema"] = ""

    args: list[str] = Field(default_factory=list)
    __pdoc__["CommandArgumentsSchema.args"] = (
        """Arguments to provide to `click.core.Argument`."""
    )

    kwargs: CommandArgumentsKwargsSchema
    __pdoc__["CommandArgumentsSchema.kwargs"] = (
        """Keyword arguments to provide to `click.core.Argument`."""
    )

    help: CommandArgumentsHelpSchema
    __pdoc__["CommandArgumentsSchema.example"] = (
        """Help strings to show when the help option is invoked."""
    )


class CommandOptionsKwargsSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandOptionsKwargsSchema"] = ""

    # Arguments to provide to `click.core.Option`

    show_default: Union[bool, str, None] = None
    __pdoc__["CommandOptionsKwargsSchema.show_default"] = (
        """Show the default value for this option in its help text. Values are not shown by default, unless `Context.show_default` is `True`. If this value is a string, it shows that string in parentheses instead of the actual value. This is particularly useful for dynamic options. 
        
        For single option boolean flags, the default remains hidden if its value is `False`."""
    )

    prompt: Union[bool, str] = False
    __pdoc__["CommandOptionsKwargsSchema.prompt"] = (
        """If set to `True` or a non empty string then the user will be prompted for input. If set to `True` the prompt will be the option name capitalized."""
    )

    confirmation_prompt: Union[bool, str] = False
    __pdoc__["CommandOptionsKwargsSchema.confirmation_prompt"] = (
        """Prompt a second time to confirm the value if it was prompted for. Can be set to a string instead of `True` to customize the message."""
    )

    prompt_required: bool = True
    __pdoc__["CommandOptionsKwargsSchema.confirmation_prompt"] = (
        """If set to `False`, the user will be prompted for input only when the option was specified as a flag without a value."""
    )

    hide_input: bool = False
    __pdoc__["CommandOptionsKwargsSchema.hide_input"] = (
        """If this is `True` then the input on the prompt will be hidden from the user. This is useful for password input."""
    )

    is_flag: Optional[bool] = None
    __pdoc__["CommandOptionsKwargsSchema.is_flag"] = (
        """Forces this option to act as a flag. The default is auto detection."""
    )

    flag_value: Optional[Any] = None
    __pdoc__["CommandOptionsKwargsSchema.flag_value"] = (
        """Which value should be used for this flag if it's enabled. This is set to a boolean automatically if the option string contains a slash to mark two options."""
    )

    multiple: bool = False
    __pdoc__["CommandOptionsKwargsSchema.flag_value"] = (
        """If this is set to `True` then the argument is accepted multiple times and recorded.  This is similar to `nargs` in how it works but supports arbitrary number of arguments."""
    )

    count: bool = False
    __pdoc__["CommandOptionsKwargsSchema.count"] = (
        """This flag makes an option increment an integer."""
    )

    allow_from_autoenv: bool = True
    __pdoc__["CommandOptionsKwargsSchema.allow_from_autoenv"] = """The help string."""

    type: Optional[Union[ParamType, Any]] = None
    __pdoc__["CommandOptionsKwargsSchema.help"] = (
        """The type that should be used.  Either a `ParamType` or a Python type. The latter is converted into the former automatically if supported.
        
        This type will also appear in the help page."""
    )

    help: Optional[str] = None
    __pdoc__["CommandOptionsKwargsSchema.help"] = """The help string."""

    hidden: bool = False
    __pdoc__["CommandOptionsKwargsSchema.hidden"] = (
        """Hide this option from help outputs."""
    )

    show_choices: bool = True
    __pdoc__["CommandOptionsKwargsSchema.show_choices"] = (
        """Show or hide choices if the passed type is a Choice. For example if type is a Choice of either day or week, show_choices is true and text is "Group by" then the prompt will be "Group by (day, week): "."""
    )

    show_envvar: bool = False
    __pdoc__["CommandOptionsKwargsSchema.show_envvar"] = (
        """Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown."""
    )

    # Arguments to provide to `click.core.Parameter`
    required: bool = False
    __pdoc__["CommandOptionsKwargsSchema.required"] = (
        """Controls if an environment variable should be shown on the help page. Normally, environment variables are not shown."""
    )

    default: Optional[Union[Any, Callable[[], Any]]] = None
    __pdoc__["CommandOptionsKwargsSchema.default"] = (
        """The default value if omitted. This can also be a callable, in which case it's invoked when the default is needed without any arguments."""
    )

    callback: Callable[[Context, Parameter, Any], Any] = show_help
    __pdoc__["CommandOptionsKwargsSchema.callback"] = (
        """A function to further process or validate the value after type conversion. It is called as `f(ctx, param, value)` and must return the value. It is called for all sources, including prompts."""
    )

    nargs: Optional[int] = None
    __pdoc__["CommandOptionsKwargsSchema.nargs"] = (
        """The number of arguments to match.  If not `1` the return value is a tuple instead of single value.  The default for nargs is `1` (except if the type is a tuple, then it's the arity of the tuple). If `nargs=-1`, all remaining parameters are collected."""
    )

    metavar: Optional[str] = None
    __pdoc__["CommandOptionsKwargsSchema.metavar"] = (
        """How the value is represented in the help page."""
    )

    expose_value: bool = True
    __pdoc__["CommandOptionsKwargsSchema.expose_value"] = (
        """If this is `True` then the value is passed onwards to the command callback and stored on the context, otherwise it's skipped."""
    )

    is_eager: bool = False
    __pdoc__["CommandOptionsKwargsSchema.is_eager"] = (
        """Eager values are processed before non eager ones.  This should not be set for arguments or it will inverse the order of processing."""
    )

    envvar: Optional[Union[str, Sequence[str]]] = None
    __pdoc__["CommandOptionsKwargsSchema.envvar"] = (
        """A string or list of strings that are environment variables that should be checked."""
    )

    shell_complete: Optional[
        Callable[
            [Context, Parameter, str],
            Union[list["CompletionItem"], list[str]],
        ]
    ] = None
    __pdoc__["CommandOptionsKwargsSchema.shell_complete"] = (
        """A function that returns custom shell completions. Used instead of the param's type completion if given. Takes `ctx, param, incomplete` and must return a list of `click.shell_completion.CompletionItem` or a list of strings."""
    )

    # class Config:
    #     extra = "allow"


class CommandOptionsHelpSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandOptionsHelpSchema"] = ""

    help: str
    __pdoc__["CommandOptionsHelpSchema.help"] = """Main help string."""

    example: Optional[str] = None
    __pdoc__["CommandOptionsHelpSchema.example"] = (
        """Example of string that can be passed as an argument"""
    )


class CommandOptionsSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandOptionsSchema"] = ""

    args: list[str] = Field(default_factory=list)
    __pdoc__["CommandOptionsSchema.args"] = (
        """Arguments to provide to `click.core.Option`."""
    )

    kwargs: CommandOptionsKwargsSchema
    __pdoc__["CommandOptionsSchema.kwargs"] = (
        """Keyword arguments to provide to `click.core.Option`."""
    )

    help: CommandOptionsHelpSchema
    __pdoc__["CommandOptionsSchema.help"] = (
        """Help strings to show when the help option is invoked."""
    )


class CommandSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CommandSchema"] = ""

    args: list[str] = Field(default_factory=list)
    __pdoc__["CommandSchema.args"] = (
        """Arguments to provide to `alltheutils.cli.base.Group.command`."""
    )

    kwargs: CommandKwargsSchema = CommandKwargsSchema()
    __pdoc__["CommandSchema.kwargs"] = (
        """Keyword arguments to provide to `alltheutils.cli.base.Group.command`."""
    )

    help: CommandHelpSchema
    __pdoc__["CommandSchema.help"] = (
        """Help strings to show when the help option is invoked"""
    )

    arguments: dict[str, CommandArgumentsSchema] = Field(default_factory=dict)
    __pdoc__["CommandSchema.arguments"] = """Arguments to attach to the command."""

    options: dict[str, CommandOptionsSchema] = Field(default_factory=dict)
    __pdoc__["CommandSchema.options"] = """Options to attach to the command."""


class CLIHelpSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CLIHelpSchema"] = ""

    overview: str


class CLIGroupCommandParamSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    __pdoc__["CLIGroupCommandParamSchema"] = ""

    name: str | Callable[..., Any] | None = None
    __pdoc__["CLIGroupCommandParamSchema.name"] = (
        """The name of the command to use unless a group overrides it."""
    )

    cls: Optional[type[Command]] = None

    context_settings: Optional[dict[str, Any]] = None
    __pdoc__["CLIGroupCommandParamSchema.context_settings"] = (
        """An optional dictionary with defaults that are passed to the context object."""
    )

    # callback: Optional[Callable[..., Any]] = None
    # __pdoc__["CLIGroupCommandParamSchema.callback"] = (
    #     """The callback to invoke. This is optional."""
    # )

    params: Optional[list[Parameter]] = None
    __pdoc__["CLIGroupCommandParamSchema.params"] = (
        """The parameters to register with this command. This can be either :class:`Option` or :class:`Argument` objects."""
    )

    help: Optional[str] = None
    __pdoc__["CLIGroupCommandParamSchema.help"] = (
        """The help string to use for this command."""
    )

    epilog: Optional[str] = None
    __pdoc__["CLIGroupCommandParamSchema.epilog"] = (
        """Like the help string but it's printed at the end of the help page after everything else."""
    )

    # short_help: Optional[str] = None
    # __pdoc__["CLIGroupCommandParamSchema.short_help"] = (
    #     """The short help to use for this command. This is shown on the command listing of the parent command."""
    # )

    options_metavar: Optional[str] = "[OPTIONS]"
    __pdoc__["CommandKwargsSchema.options_metavar"] = (
        """The metavar displayed for options in the help page."""
    )

    add_help_option: bool = True
    __pdoc__["CLIGroupCommandParamSchema.add_help_option"] = (
        """By default each command registers a `--help` option. This can be disabled by this parameter."""
    )

    no_args_is_help: bool = False
    __pdoc__["CLIGroupCommandParamSchema.no_args_is_help"] = (
        """This controls what happens if no arguments are provided. This option is disabled by default. If enabled this will add `--help` as argument if no arguments are passed"""
    )

    hidden: bool = False
    __pdoc__["CLIGroupCommandParamSchema.hidden"] = (
        """Hide this command from help outputs."""
    )

    deprecated: bool = False
    __pdoc__["CLIGroupCommandParamSchema.deprecated"] = (
        """If `True` or non-empty string, issues a message indicating that the command is deprecated and highlights its deprecation in --help. The message can be customized by using a string as the value."""
    )


class CLIConfig(BaseModel):
    group_command_params: CLIGroupCommandParamSchema = CLIGroupCommandParamSchema()
    commands: dict[str, CommandSchema] = Field(default_factory=dict)

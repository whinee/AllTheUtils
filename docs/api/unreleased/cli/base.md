<h1 id=""><a href="#">Module alltheutils.cli.base</a></h1>

Parts of code in `alltheutils/cli/base.py` is derived from [click](https://github.com/pallets/click)

3-Clause BSD License

Copyright © 2014-2025 Pallets

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1.  Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

2.  Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

Hereunder resides functions for constructing CLI for this program.

> This module heavily documents my descent to madness.
>
> An unholy amalgamation of megalamonia, depression, God complex, and impostor syndrome filled my broken heart.
>
> This file is the digital manifestation of my mental woes.
>
> Masochistic tendencies fuelling my coding sessions.
>
> I wish upon this abyss to not touch this file ever again.

whi~nyaan! ― 2023

---

Update (April 23, 2025):

This still holds true to this day. Please, do not touch if you do not need to.

---

Update (May 4, 2025):

Bruh, why am I touching this?

[← Go back to `alltheutils.cli`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-command"><a href="#functions-command"><pre>command</pre></a></h3>

```python
(group: alltheutils.cli.base.Group, command_config: dict[str, typing.Any]) → Callable[[Callable[..., typing.Any]], Callable[..., typing.Any]]
```

Wrapper for click commands.

Args:
- command_config (`dict[str, Any]`): Command configuration dictionary.
- group (`Group`): Command group of the command to be under.

Returns:
- `Callable[[Callable[..., Any]], Callable[..., Any]]`

<h3 id="functions-command_group"><a href="#functions-command_group"><pre>command_group</pre></a></h3>

```python
(name: str | collections.abc.Callable[..., typing.Any] | None = None, **attrs: Any) → alltheutils.cli.base.Group
```

<h3 id="functions-custom_command"><a href="#functions-custom_command"><pre>custom_command</pre></a></h3>

```python
(name: str | collections.abc.Callable[..., typing.Any] | None = None, cls: type[alltheutils.cli.base.Command] | None = None, **attrs: Any) → alltheutils.cli.base.Command | collections.abc.Callable[..., alltheutils.cli.base.Command]
```

<h3 id="functions-show_help"><a href="#functions-show_help"><pre>show_help</pre></a></h3>

```python
(ctx: click.core.Context, param: click.core.Parameter, value: str) → None
```

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-command"><a href="#classes-command"><pre>Command</pre></a></h3>

```python
(name: str | None, context_settings: dict[str, typing.Any] | None = None, callback: Callable[..., typing.Any] | None = None, params: list[click.core.Parameter] | None = None, help: str | None = None, epilog: str | None = None, short_help: str | None = None, options_metavar: str | None = '[OPTIONS]', add_help_option: bool = True, no_args_is_help: bool = False, hidden: bool = False, deprecated: bool = False)
```

Commands are the basic building block of command line interfaces in
Click.  A basic command handles command line parsing and might dispatch
more parsing to commands nested below it.

:param name: the name of the command to use unless a group overrides it.
:param context_settings: an optional dictionary with defaults that are
                         passed to the context object.
:param callback: the callback to invoke.  This is optional.
:param params: the parameters to register with this command.  This can
               be either :class:`Option` or :class:`Argument` objects.
:param help: the help string to use for this command.
:param epilog: like the help string but it's printed at the end of the
               help page after everything else.
:param short_help: the short help to use for this command.  This is
                   shown on the command listing of the parent command.
:param add_help_option: by default each command registers a ``--help``
                        option.  This can be disabled by this parameter.
:param no_args_is_help: this controls what happens if no arguments are
                        provided.  This option is disabled by default.
                        If enabled this will add ``--help`` as argument
                        if no arguments are passed
:param hidden: hide this command from help outputs.

:param deprecated: issues a message indicating that
                         the command is deprecated.

.. versionchanged:: 8.1
    ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
    all formatting is done when outputting help text, not at init,
    and is done even if not using the ``@command`` decorator.

.. versionchanged:: 8.0
    Added a ``repr`` showing the command name.

.. versionchanged:: 7.1
    Added the ``no_args_is_help`` parameter.

.. versionchanged:: 2.0
    Added the ``context_settings`` parameter.

<h4 id="classes-command-ancestors-in-mro"><a href="#classes-command-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- click.core.Command
- click.core.BaseCommand

<h4 id="classes-command-descendants"><a href="#classes-command-descendants">Descendants</a></h4>

- alltheutils.cli.base.MultiCommand

<h4 id="classes-command-instance-variables"><a href="#classes-command-instance-variables">Instance variables</a></h4>

<h5 id="classes-command-instance-variables-callback"><a href="#classes-command-instance-variables-callback"><pre>callback</pre></a></h5>

the callback to execute when the command fires.  This might be
`None` in which case nothing happens.

<h5 id="classes-command-instance-variables-name"><a href="#classes-command-instance-variables-name"><pre>name</pre></a></h5>

the list of parameters for this command in the order they
should show up in the help page and execute.  Eager parameters
will automatically be handled before non eager ones.

<h4 id="classes-command-methods"><a href="#classes-command-methods">Methods</a></h4>

<h5 id="classes-command-methods-format_usage"><a href="#classes-command-methods-format_usage"><pre>format_usage</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.

<h5 id="classes-command-methods-get_help_option"><a href="#classes-command-methods-get_help_option"><pre>get_help_option</pre></a></h5>

```python
(self, ctx: click.core.Context) → click.core.Option | None
```

Returns the help option object.

<h3 id="classes-commandwrapper"><a href="#classes-commandwrapper"><pre>CommandWrapper</pre></a></h3>

```python
(command_config, group: alltheutils.cli.base.Group)
```

Returns wrappers for a click command evaluated from the given arguments.

Initialize object.

Args:
- group (`Group`): Command group of the command to be under.

<h4 id="classes-commandwrapper-methods"><a href="#classes-commandwrapper-methods">Methods</a></h4>

<h5 id="classes-commandwrapper-methods-arguments"><a href="#classes-commandwrapper-methods-arguments"><pre>arguments</pre></a></h5>

```python
(self) → Callable[[Callable[..., typing.Any]], Callable[..., typing.Any]]
```

The arguments wrapper.

Returns:
`Callable[[Callable[..., Any]], Callable[..., Any]]`

<h5 id="classes-commandwrapper-methods-command"><a href="#classes-commandwrapper-methods-command"><pre>command</pre></a></h5>

```python
(self) → Callable[[Callable[..., typing.Any]], Callable[..., typing.Any]]
```

The command wrapper.

Returns:
`Callable[[Callable[..., Any]], Callable[..., Any]]`

<h5 id="classes-commandwrapper-methods-kwargs_preprocessor"><a href="#classes-commandwrapper-methods-kwargs_preprocessor"><pre>kwargs_preprocessor</pre></a></h5>

```python
(self, func: Callable[..., typing.Any]) → Callable[..., typing.Any]
```

<h5 id="classes-commandwrapper-methods-option_type_help_example"><a href="#classes-commandwrapper-methods-option_type_help_example"><pre>option_type_help_example</pre></a></h5>

```python
(self, maxlen_type_string: int, maxlen_opts_help: int) → Callable[..., tuple[str, str, str]]
```

<h5 id="classes-commandwrapper-methods-options"><a href="#classes-commandwrapper-methods-options"><pre>options</pre></a></h5>

```python
(self) → Callable[[Callable[..., typing.Any]], Callable[..., typing.Any]]
```

The options wrapper.

My God in heaven, I'm agnostic, but please save me from all evil. Amen.

Returns:
`Callable[[Callable[..., Any]], Callable[..., Any]]`

<h5 id="classes-commandwrapper-methods-wrap"><a href="#classes-commandwrapper-methods-wrap"><pre>wrap</pre></a></h5>

```python
(self, func: Callable[..., typing.Any]) → Callable[..., typing.Any]
```

Wrap given function with corresponding click decorators.

Args:
- func (`Callable[..., Any]`): Function to be wrapped.

Returns:
`Callable[..., Any]`: Wrapped function.

<h3 id="classes-extinquirercontrol"><a href="#classes-extinquirercontrol"><pre>ExtInquirerControl</pre></a></h3>

```python
(choices: Sequence[str | questionary.prompts.common.Choice | Dict[str, Any]], default: str | questionary.prompts.common.Choice | Dict[str, Any] | None = None, pointer: str | None = '»', use_indicator: bool = True, use_shortcuts: bool = False, show_selected: bool = False, show_description: bool = True, use_arrow_keys: bool = True, initial_choice: str | questionary.prompts.common.Choice | Dict[str, Any] | None = None, **kwargs: Any)
```

Control that displays formatted text. This can be either plain text, an
:class:`~prompt_toolkit.formatted_text.HTML` object an
:class:`~prompt_toolkit.formatted_text.ANSI` object, a list of ``(style_str,
text)`` tuples or a callable that takes no argument and returns one of
those, depending on how you prefer to do the formatting. See
``prompt_toolkit.layout.formatted_text`` for more information.

(It's mostly optimized for rather small widgets, like toolbars, menus, etc...)

When this UI control has the focus, the cursor will be shown in the upper
left corner of this control by default. There are two ways for specifying
the cursor position:

- Pass a `get_cursor_position` function which returns a `Point` instance
  with the current cursor position.

- If the (formatted) text is passed as a list of ``(style, text)`` tuples
  and there is one that looks like ``('[SetCursorPosition]', '')``, then
  this will specify the cursor position.

Mouse support:

    The list of fragments can also contain tuples of three items, looking like:
    (style_str, text, handler). When mouse support is enabled and the user
    clicks on this fragment, then the given handler is called. That handler
    should accept two inputs: (Application, MouseEvent) and it should
    either handle the event or return `NotImplemented` in case we want the
    containing Window to handle this event.

:param focusable: `bool` or :class:`.Filter`: Tell whether this control is
    focusable.

:param text: Text or formatted text to be displayed.
:param style: Style string applied to the content. (If you want to style
    the whole :class:`~prompt_toolkit.layout.Window`, pass the style to the
    :class:`~prompt_toolkit.layout.Window` instead.)
:param key_bindings: a :class:`.KeyBindings` object.
:param get_cursor_position: A callable that returns the cursor position as
    a `Point` instance.

<h4 id="classes-extinquirercontrol-ancestors-in-mro"><a href="#classes-extinquirercontrol-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- questionary.prompts.common.InquirerControl
- prompt_toolkit.layout.controls.FormattedTextControl
- prompt_toolkit.layout.controls.UIControl

<h4 id="classes-extinquirercontrol-class-variables"><a href="#classes-extinquirercontrol-class-variables">Class variables</a></h4>

<h5 id="classes-extinquirercontrol-class-variables-answer_text"><a href="#classes-extinquirercontrol-class-variables-answer_text"><pre>answer_text</pre></a></h5>

<h3 id="classes-extquestion"><a href="#classes-extquestion"><pre>ExtQuestion</pre></a></h3>

```python
(application: Application[Any])
```

A question to be prompted.

This is an internal class. Questions should be created using the
predefined questions (e.g. text or password).

<h4 id="classes-extquestion-ancestors-in-mro"><a href="#classes-extquestion-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- questionary.question.Question

<h4 id="classes-extquestion-class-variables"><a href="#classes-extquestion-class-variables">Class variables</a></h4>

<h5 id="classes-extquestion-class-variables-kbi"><a href="#classes-extquestion-class-variables-kbi"><pre>kbi</pre></a></h5>

<h4 id="classes-extquestion-methods"><a href="#classes-extquestion-methods">Methods</a></h4>

<h5 id="classes-extquestion-methods-ask"><a href="#classes-extquestion-methods-ask"><pre>ask</pre></a></h5>

```python
(self, patch_stdout: bool | None = None, **kwargs: dict[str, typing.Any]) → tuple[bool, typing.Any]
```

Ask the question synchronously and return user response.

Args:
- patch_stdout (`bool`, optional): Ensure that the prompt renders correctly if other threads are printing to stdout. Defaults to `None`.

Returns:
`Any`: The answer from the question.

<h3 id="classes-group"><a href="#classes-group"><pre>Group</pre></a></h3>

```python
(name: str | None = None, commands: dict[str, alltheutils.cli.base.Command] | Sequence[alltheutils.cli.base.Command] | None = None, **attrs: Any)
```

Commands are the basic building block of command line interfaces in
Click.  A basic command handles command line parsing and might dispatch
more parsing to commands nested below it.

:param name: the name of the command to use unless a group overrides it.
:param context_settings: an optional dictionary with defaults that are
                         passed to the context object.
:param callback: the callback to invoke.  This is optional.
:param params: the parameters to register with this command.  This can
               be either :class:`Option` or :class:`Argument` objects.
:param help: the help string to use for this command.
:param epilog: like the help string but it's printed at the end of the
               help page after everything else.
:param short_help: the short help to use for this command.  This is
                   shown on the command listing of the parent command.
:param add_help_option: by default each command registers a ``--help``
                        option.  This can be disabled by this parameter.
:param no_args_is_help: this controls what happens if no arguments are
                        provided.  This option is disabled by default.
                        If enabled this will add ``--help`` as argument
                        if no arguments are passed
:param hidden: hide this command from help outputs.

:param deprecated: issues a message indicating that
                         the command is deprecated.

.. versionchanged:: 8.1
    ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
    all formatting is done when outputting help text, not at init,
    and is done even if not using the ``@command`` decorator.

.. versionchanged:: 8.0
    Added a ``repr`` showing the command name.

.. versionchanged:: 7.1
    Added the ``no_args_is_help`` parameter.

.. versionchanged:: 2.0
    Added the ``context_settings`` parameter.

<h4 id="classes-group-ancestors-in-mro"><a href="#classes-group-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.cli.base.MultiCommand
- alltheutils.cli.base.Command
- click.core.Command
- click.core.BaseCommand

<h4 id="classes-group-class-variables"><a href="#classes-group-class-variables">Class variables</a></h4>

<h5 id="classes-group-class-variables-command_class"><a href="#classes-group-class-variables-command_class"><pre>command_class</pre></a></h5>

```python
type[alltheutils.cli.base.Command] | None
```

<h5 id="classes-group-class-variables-group_class"><a href="#classes-group-class-variables-group_class"><pre>group_class</pre></a></h5>

```python
type[alltheutils.cli.base.Group] | type[type] | None
```

<h4 id="classes-group-instance-variables"><a href="#classes-group-instance-variables">Instance variables</a></h4>

<h5 id="classes-group-instance-variables-callback"><a href="#classes-group-instance-variables-callback"><pre>callback</pre></a></h5>

the callback to execute when the command fires.  This might be
`None` in which case nothing happens.

<h5 id="classes-group-instance-variables-commands"><a href="#classes-group-instance-variables-commands"><pre>commands</pre></a></h5>

The registered subcommands by their exported names.

<h5 id="classes-group-instance-variables-name"><a href="#classes-group-instance-variables-name"><pre>name</pre></a></h5>

the list of parameters for this command in the order they
should show up in the help page and execute.  Eager parameters
will automatically be handled before non eager ones.

<h4 id="classes-group-methods"><a href="#classes-group-methods">Methods</a></h4>

<h5 id="classes-group-methods-add_command"><a href="#classes-group-methods-add_command"><pre>add_command</pre></a></h5>

```python
(self, cmd: alltheutils.cli.base.Command, name: str | None = None) → None
```

<h5 id="classes-group-methods-collect_usage_pieces"><a href="#classes-group-methods-collect_usage_pieces"><pre>collect_usage_pieces</pre></a></h5>

```python
(self, ctx: click.core.Context) → list[str]
```

Returns all the pieces that go into the usage line and returns
it as a list of strings.

<h5 id="classes-group-methods-command"><a href="#classes-group-methods-command"><pre>command</pre></a></h5>

```python
(self, *args: Any, **kwargs: Any) → collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], alltheutils.cli.base.Command] | alltheutils.cli.base.Command
```

<h5 id="classes-group-methods-format_options"><a href="#classes-group-methods-format_options"><pre>format_options</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

Writes all the options into the formatter if they exist.

<h5 id="classes-group-methods-format_usage"><a href="#classes-group-methods-format_usage"><pre>format_usage</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.

<h5 id="classes-group-methods-get_command"><a href="#classes-group-methods-get_command"><pre>get_command</pre></a></h5>

```python
(self, ctx: click.core.Context, cmd_name: str) → alltheutils.cli.base.Command | None
```

<h5 id="classes-group-methods-get_help_option"><a href="#classes-group-methods-get_help_option"><pre>get_help_option</pre></a></h5>

```python
(self, ctx: click.core.Context) → click.core.Option | None
```

Returns the help option object.

<h5 id="classes-group-methods-group"><a href="#classes-group-methods-group"><pre>group</pre></a></h5>

```python
(self, *args: Any, **kwargs: Any) → Callable[[Callable[..., typing.Any]], alltheutils.cli.base.Group] | alltheutils.cli.base.Group
```

<h5 id="classes-group-methods-invoke"><a href="#classes-group-methods-invoke"><pre>invoke</pre></a></h5>

```python
(self, ctx: click.core.Context) → Any
```

Given a context, this invokes the attached callback (if it exists)
in the right way.

<h5 id="classes-group-methods-list_commands"><a href="#classes-group-methods-list_commands"><pre>list_commands</pre></a></h5>

```python
(self, ctx: click.core.Context) → list[str]
```

<h5 id="classes-group-methods-parse_args"><a href="#classes-group-methods-parse_args"><pre>parse_args</pre></a></h5>

```python
(self, ctx: click.core.Context, args: list[str]) → list[str]
```

Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.

<h5 id="classes-group-methods-shell_complete"><a href="#classes-group-methods-shell_complete"><pre>shell_complete</pre></a></h5>

```python
(self, ctx: click.core.Context, incomplete: str)
```

Return a list of completions for the incomplete value. Looks
at the names of options and chained multi-commands.

:param ctx: Invocation context for this command.
:param incomplete: Value being completed. May be empty.

.. versionadded:: 8.0

<h5 id="classes-group-methods-to_info_dict"><a href="#classes-group-methods-to_info_dict"><pre>to_info_dict</pre></a></h5>

```python
(self, ctx: click.core.Context) → dict[str, typing.Any]
```

Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

:param ctx: A :class:`Context` representing this command.

.. versionadded:: 8.0

<h3 id="classes-multicommand"><a href="#classes-multicommand"><pre>MultiCommand</pre></a></h3>

```python
(name: str | None = None, invoke_without_command: bool = False, no_args_is_help: bool | None = None, subcommand_metavar: str | None = None, chain: bool = False, result_callback: Callable[..., typing.Any] | None = None, **attrs: Any)
```

Commands are the basic building block of command line interfaces in
Click.  A basic command handles command line parsing and might dispatch
more parsing to commands nested below it.

:param name: the name of the command to use unless a group overrides it.
:param context_settings: an optional dictionary with defaults that are
                         passed to the context object.
:param callback: the callback to invoke.  This is optional.
:param params: the parameters to register with this command.  This can
               be either :class:`Option` or :class:`Argument` objects.
:param help: the help string to use for this command.
:param epilog: like the help string but it's printed at the end of the
               help page after everything else.
:param short_help: the short help to use for this command.  This is
                   shown on the command listing of the parent command.
:param add_help_option: by default each command registers a ``--help``
                        option.  This can be disabled by this parameter.
:param no_args_is_help: this controls what happens if no arguments are
                        provided.  This option is disabled by default.
                        If enabled this will add ``--help`` as argument
                        if no arguments are passed
:param hidden: hide this command from help outputs.

:param deprecated: issues a message indicating that
                         the command is deprecated.

.. versionchanged:: 8.1
    ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
    all formatting is done when outputting help text, not at init,
    and is done even if not using the ``@command`` decorator.

.. versionchanged:: 8.0
    Added a ``repr`` showing the command name.

.. versionchanged:: 7.1
    Added the ``no_args_is_help`` parameter.

.. versionchanged:: 2.0
    Added the ``context_settings`` parameter.

<h4 id="classes-multicommand-ancestors-in-mro"><a href="#classes-multicommand-ancestors-in-mro">Ancestors (in MRO)</a></h4>

- alltheutils.cli.base.Command
- click.core.Command
- click.core.BaseCommand

<h4 id="classes-multicommand-descendants"><a href="#classes-multicommand-descendants">Descendants</a></h4>

- alltheutils.cli.base.Group

<h4 id="classes-multicommand-class-variables"><a href="#classes-multicommand-class-variables">Class variables</a></h4>

<h5 id="classes-multicommand-class-variables-allow_extra_args"><a href="#classes-multicommand-class-variables-allow_extra_args"><pre>allow_extra_args</pre></a></h5>

<h5 id="classes-multicommand-class-variables-allow_interspersed_args"><a href="#classes-multicommand-class-variables-allow_interspersed_args"><pre>allow_interspersed_args</pre></a></h5>

<h4 id="classes-multicommand-instance-variables"><a href="#classes-multicommand-instance-variables">Instance variables</a></h4>

<h5 id="classes-multicommand-instance-variables-callback"><a href="#classes-multicommand-instance-variables-callback"><pre>callback</pre></a></h5>

the callback to execute when the command fires.  This might be
`None` in which case nothing happens.

<h5 id="classes-multicommand-instance-variables-name"><a href="#classes-multicommand-instance-variables-name"><pre>name</pre></a></h5>

the list of parameters for this command in the order they
should show up in the help page and execute.  Eager parameters
will automatically be handled before non eager ones.

<h4 id="classes-multicommand-methods"><a href="#classes-multicommand-methods">Methods</a></h4>

<h5 id="classes-multicommand-methods-collect_usage_pieces"><a href="#classes-multicommand-methods-collect_usage_pieces"><pre>collect_usage_pieces</pre></a></h5>

```python
(self, ctx: click.core.Context) → list[str]
```

Returns all the pieces that go into the usage line and returns
it as a list of strings.

<h5 id="classes-multicommand-methods-format_commands"><a href="#classes-multicommand-methods-format_commands"><pre>format_commands</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

<h5 id="classes-multicommand-methods-format_options"><a href="#classes-multicommand-methods-format_options"><pre>format_options</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

Writes all the options into the formatter if they exist.

<h5 id="classes-multicommand-methods-format_usage"><a href="#classes-multicommand-methods-format_usage"><pre>format_usage</pre></a></h5>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) → None
```

Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.

<h5 id="classes-multicommand-methods-get_command"><a href="#classes-multicommand-methods-get_command"><pre>get_command</pre></a></h5>

```python
(self, ctx: click.core.Context, cmd_name: str) → alltheutils.cli.base.Command | None
```

<h5 id="classes-multicommand-methods-get_help_option"><a href="#classes-multicommand-methods-get_help_option"><pre>get_help_option</pre></a></h5>

```python
(self, ctx: click.core.Context) → click.core.Option | None
```

Returns the help option object.

<h5 id="classes-multicommand-methods-invoke"><a href="#classes-multicommand-methods-invoke"><pre>invoke</pre></a></h5>

```python
(self, ctx: click.core.Context) → Any
```

Given a context, this invokes the attached callback (if it exists)
in the right way.

<h5 id="classes-multicommand-methods-list_commands"><a href="#classes-multicommand-methods-list_commands"><pre>list_commands</pre></a></h5>

```python
(self, ctx: click.core.Context) → list[str]
```

<h5 id="classes-multicommand-methods-parse_args"><a href="#classes-multicommand-methods-parse_args"><pre>parse_args</pre></a></h5>

```python
(self, ctx: click.core.Context, args: list[str]) → list[str]
```

Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.

<h5 id="classes-multicommand-methods-resolve_command"><a href="#classes-multicommand-methods-resolve_command"><pre>resolve_command</pre></a></h5>

```python
(self, ctx: click.core.Context, args: list[str]) → tuple[str | None, alltheutils.cli.base.Command | None, list[str]]
```

<h5 id="classes-multicommand-methods-result_callback"><a href="#classes-multicommand-methods-result_callback"><pre>result_callback</pre></a></h5>

```python
(self, replace: bool = False) → Callable[[~F], ~F]
```

<h5 id="classes-multicommand-methods-shell_complete"><a href="#classes-multicommand-methods-shell_complete"><pre>shell_complete</pre></a></h5>

```python
(self, ctx: click.core.Context, incomplete: str)
```

Return a list of completions for the incomplete value. Looks
at the names of options and chained multi-commands.

:param ctx: Invocation context for this command.
:param incomplete: Value being completed. May be empty.

.. versionadded:: 8.0

<h5 id="classes-multicommand-methods-to_info_dict"><a href="#classes-multicommand-methods-to_info_dict"><pre>to_info_dict</pre></a></h5>

```python
(self, ctx: click.core.Context) → dict[str, typing.Any]
```

Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

:param ctx: A :class:`Context` representing this command.

.. versionadded:: 8.0

---

[← Go back to `alltheutils.cli`](./index.md)
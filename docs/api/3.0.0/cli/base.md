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
(group: click.core.Group, command_config: dict[str, alltheutils.cli.dataclasses.CommandSchema]) → Callable[[Callable[..., typing.Any]], Callable[..., typing.Any]]
```

Wrapper for click commands.

Args:
- command_config (`dict[str, CommandSchema]`): Command configuration.
- group (`Group`): Command group of the command to be under.

Returns:
- `Callable[[Callable[..., Any]], Callable[..., Any]]`

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-commandwrapper"><a href="#classes-commandwrapper"><pre>CommandWrapper</pre></a></h3>

```python
(command_config: dict[str, alltheutils.cli.dataclasses.CommandSchema], group: click.core.Group)
```

Returns wrappers for a click command evaluated from the given arguments.

Initialize object.

Args:
- command_config (`dict[str, CommandSchema]`): Command config for initialization of the command.
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

Extended/Modified InquirerControl class.

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

Extended/Modified Question class.

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

---

[← Go back to `alltheutils.cli`](./index.md)
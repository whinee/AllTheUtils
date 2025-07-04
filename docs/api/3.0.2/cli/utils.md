<h1 id=""><a href="#">Module alltheutils.cli.utils</a></h1>

[← Go back to `alltheutils.cli`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-command_type_str_to_type"><a href="#functions-command_type_str_to_type"><pre>command_type_str_to_type</pre></a></h3>

```python
(commands: dict[str, typing.Any]) → Any
```

<h3 id="functions-parse_config_file_cli_config"><a href="#functions-parse_config_file_cli_config"><pre>parse_config_file_cli_config</pre></a></h3>

```python
(file_path: str, filters_before_conversion: list[collections.abc.Callable[[dict[str, typing.Any]], dict[str, typing.Any]]] | None = None) → alltheutils.cli.dataclasses.CLIConfig
```

<h3 id="functions-select"><a href="#functions-select"><pre>select</pre></a></h3>

```python
(message: str, choices: collections.abc.Sequence[str | questionary.prompts.common.Choice | dict[str, typing.Any]] | dict[str, typing.Any], default: typing.Any | None = None, instruction: str | None = None, answer_text: str | None = None, keyboard_interrupt_message: str | None = None, qmark: str | None = None, pointer: str | None = None, style: prompt_toolkit.styles.base.BaseStyle | None = None, show_selected: bool | None = None, ret_err: bool | None = None, **kwargs: dict[str, typing.Any]) → tuple[bool, typing.Any]
```

<h3 id="functions-str_to_type"><a href="#functions-str_to_type"><pre>str_to_type</pre></a></h3>

```python
(str_type: str) → Any
```

---

[← Go back to `alltheutils.cli`](./index.md)
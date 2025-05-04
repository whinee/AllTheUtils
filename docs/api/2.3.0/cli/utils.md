<h1 id=""><a href="#">Module alltheutils.cli.utils</a></h1>

[← Go back to `alltheutils.cli`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-parse_yaml_file_command_config"><a href="#functions-parse_yaml_file_command_config"><pre>parse_yaml_file_command_config</pre></a></h3>

```python
(file_path: str) → pydantic.root_model.RootModel[dict[str, CommandSchema]]
```

<h3 id="functions-select"><a href="#functions-select"><pre>select</pre></a></h3>

```python
(message: str, choices: collections.abc.Sequence[str | questionary.prompts.common.Choice | dict[str, typing.Any]] | dict[str, typing.Any], language_constant: dict[str, typing.Any], default: Any | None = None, instruction: str | None = None, qmark: str | None = None, pointer: str | None = None, style: prompt_toolkit.styles.base.BaseStyle | None = None, show_selected: bool | None = None, ret_err: bool | None = None, **kwargs: dict[str, typing.Any]) → tuple[bool, typing.Any]
```

---

[← Go back to `alltheutils.cli`](./index.md)
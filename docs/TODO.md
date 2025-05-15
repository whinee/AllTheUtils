<h1 align="center" style="font-weight: bold">
    TODO
</h1>

<!-- All tasks are completed! -->

Items are sorted by priority, with the most important item at the top and least important at the bottom.

## Permanent

- [ ] Unit testing for mission critical piece of code
- [ ] Seperate functions to different modules based on uses

## Temporary

- [ ] Custom version bumping CLI dev tool
- [ ] Translation file support for CLI
- [ ] In pdoc-generated markdown files, make a Table of Contents
- [ ] In pdoc-generated markdown files, determine whether a given mmarkdown file is the top level index file for that app's version, and if so, shall point back to the index where the user can choose the app's version and their corresponding documentation
- [ ] Use [typeguard](https://typeguard.readthedocs.io/en/stable/userguide.html) to type check function arguments and return values in runtime
- [ ] Add test coverage in README
- [ ] Replace `pyyaml` library dependency with `ruamel.yaml`

## Done

- [x] Migrate from `poetry` to `uv`
- [x] In pdoc-generated markdown files, convert markdown headings to HTML headings with links
- [x] Add PyPi project specific API token in the Github repository for automatic python package release
- [x] Fuck I forgot to do `alltheutils.utils.get_value_from_or_update_nested_dict` TODOs before bumping to 1.1.0 LMFAOOO
- [x] Remove deprecated functions in `alltheutils/utils.py` for removal in v2.0.0.

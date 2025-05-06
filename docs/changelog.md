<h1 align="center" style="font-weight: bold">
    Changelog
</h1>

This software uses [Semantic Versioning v2.0.0](https://semver.org/spec/v2.0.0.html). This changelog is based on [keepachangelog.com v1.1.0](https://keepachangelog.com/en/1.1.0/).

**Types of Changes**

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## 3.0.0 (Unreleased)

### Removed

- Classes, functions and modules deprecated in v2.0.0, v2.1.0, and v2.2.0

## Unreleased

### Added

- `alltheutils.exceptions.BumpVersionNoPrerelease`
- `alltheutils.exceptions.BumpVersionPartUnknown`
- `alltheutils.utils.bump_version`

## 2.3.0

### Added

- CLI utilities
- `alltheutils.exceptions.CLICommandNotFound`
- `alltheutils.instance_config`
- `alltheutils.utils.requires_instance_config`

### Changed

- Project installer to be `uv` instead of `poetry`

## 2.2.0

This is not funny anymore, guys. I'm so tired of deprecating shit due to the poor design choices I've made in the past :C

I've mostly deprecated stuff this time for the custom exceptions to be easily documented by pdoc3.

### Added

- Added `alltheutils.utils.deprecated_class` decorator for deprecating classes
- Added `alltheutils.exceptions.deprecated_class` decorators for deprecated base_exceptions classes. If you are an external API user, please use the `alltheutils.utils.deprecated_class` decorator instead.

### Changed

- Changed `alltheutils.config.ParserRegistry.get_parser` to throw `alltheutils.exceptions.ConfigFileExtensionNotSupported` instead of `alltheutils.exceptions.ConfigExceptions.ExtensionNotSupported`, and updated docstrings in the module to reflect said change
- Changed `alltheutils.utils.file_exists` to throw `alltheutils.exceptions.FileNotFound` instead of `alltheutils.exceptions.GeneralExceptions.ValidationError.FileNotFound`, and updated docstrings in said function to reflect said change
- Changed `alltheutils.utils.file_exists` to throw the new exceptions. Fuck! Just look at the deprecated classes in this version to see which changes what.

### Deprecated

- The following classes has been renamed to be more readable:
    - `alltheutils.exceptions.GeneralExceptions.ValidationError.FileNotFound` -> `alltheutils.exceptions.FileNotFound`
    - `alltheutils.exceptions.GeneralExceptions.ValidationError.Arguments` -> `alltheutils.exceptions.Arguments`
    - `alltheutils.exceptions.GeneralExceptions.ValidationError.Common` -> `alltheutils.exceptions.CommonValidationError`
    - `alltheutils.exceptions.GeneralExceptions.PrerequisiteNotFound` -> `alltheutils.exceptions.PrerequisiteNotFound`
    - `alltheutils.exceptions.CLIExceptions.TerminalTooThin` -> `alltheutils.exceptions.TerminalTooThin`
    - `alltheutils.exceptions.CLIExceptions.ValidationError.OptionRequired` -> `alltheutils.exceptions.CLIOptionRequired`
    - `alltheutils.exceptions.CLIExceptions.ValidationError.Common` -> `alltheutils.exceptions.CLICommonError`
    - `alltheutils.exceptions.ConfigExceptions.ExtensionNotSupported` -> `alltheutils.exceptions.ConfigFileExtensionNotSupported`
    - `alltheutils.exceptions.CFGExceptions.ExtensionNotSupported` -> `alltheutils.exceptions.ConfigFileExtensionNotSupported`
    - `alltheutils.exceptions.NestedDictExceptions.NonDictReplacementValue` -> `alltheutils.exceptions.NDNonDictReplacementValue`
    - `alltheutils.exceptions.NestedDictExceptions.ValueNotAList` -> `alltheutils.exceptions.NDValueNotAList`
    - `alltheutils.exceptions.NestedDictExceptions.ValueNotADict` -> `alltheutils.exceptions.NDValueNotADict`
    - `alltheutils.exceptions.NestedDictExceptions.ValueDoesNotExist` -> `alltheutils.exceptions.NDValueDoesNotExist`
    - `alltheutils.exceptions.NestedDictExceptions.ValueIsAListAndIndexIsOutOfRange` -> `alltheutils.exceptions.NDValueIsAListAndIndexIsOutOfRange`

## 2.1.0

### Added

- Added `alltheutils.base_exceptions.deprecated` and `alltheutils.cfg.deprecated` decorators for deprecated base_exceptions and cfg functions respectively. If you are an external API user, please use the `alltheutils.utils.deprecated` decorator instead.
- Added `alltheutils.base_exceptions.CustomBaseException` to be inherited by custom exceptions, instead of decorating them with `alltheutils.utils.custom_exception_str`.

### Changed

- Changed the custom exceptions in `alltheutils.exceptions` to inherit `alltheutils.base_exceptions.CustomBaseException` instead of decorating them with `alltheutils.utils.custom_exception_str`.
- Seperated multiprocessing utility functions from `alltheutils/utils.py` to `alltheutils/multi_processing.py`. See this version's deprecated functions for more details.
- Changed all of the logics in the functions inside `alltheutils.multi_processing` to better align with their original purpose, as the original ones, I believe, are quite broken 

### Deprecated

- The following modules has been renamed to be more readable:
    - `alltheutils.cfg` -> `alltheutils.config`

- The following classes has been renamed to be more readable:
    - `alltheutils.exceptions.CFGExceptions` -> `alltheutils.exceptions.ConfigExceptions`

- The following functions will be removed:
    - `alltheutils.utils.custom_exception_str`: Inherit the custom exception class from `alltheutils.base_exceptions.CustomBaseException` instead, alongside any inherited exception/s.

## 2.0.0

### Added

- Added the `alltheutils.base_exc.deprecated` decorator for deprecated base_exc function. If you are an external API user, please use the `alltheutils.utils.deprecated` decorator instead.

### Changed

- Changed the exceptions in `alltheutils.utils.get_value_from_or_update_nested_dict` to be custom and more descriptive
- Changed the parameter names of function `alltheutils.utils.if_none`

### Deprecated

- The following modules has been renamed to be more readable:
    - `alltheutils.base_exc` -> `alltheutils.base_exceptions`

- The following functions has been renamed to be more readable (note that the parameters' names might be changed):
    - `alltheutils.base_exc.c_exc` -> `alltheutils.base_exceptions.custom_exception`
    - `alltheutils.base_exc.c_exc_str` -> `alltheutils.base_exceptions.custom_exception_str`

### Removed

- Removed functions deprecated in v1.1.0
- Removed `alltheutils.exceptions.CDExceptions`

## 1.1.0

### Added

- Added `alltheutils.utils.deprecated` decorator for deprecating utils function
- Added `alltheutils.utils.get_value_from_or_update_nested_dict`
- Added an MIT License

### Deprecated

- The following functions has been renamed to be more readable (note that the parameters' names might be changed):
    - `alltheutils.utils.calc_hash` -> `calculate_sha256_hash`
    - `alltheutils.utils.cycle_2ls` -> `zip_extend`
    - `alltheutils.utils.dnn` -> `parent_dir_nth_times`
    - `alltheutils.utils.dnrp` -> `parent_dir_nth_times`
        - Use `alltheutils.utils.parent_dir_nth_times(os.path.realpath(file))` instead.
    - `alltheutils.utils.dpop` -> `dict_get_first_match`
    - `alltheutils.utils.dt_ts` -> `unix_timestamp_to_iso`
    - `alltheutils.utils.fn` -> `caller_relative_path`
    - `alltheutils.utils.inmd` -> `ensure_parent_dir`
    - `alltheutils.utils.ivnd` -> `if_none`
    - `alltheutils.utils.le` -> `literal_eval`
    - `alltheutils.utils.repl` -> `batch_replace`
    - `alltheutils.utils.rfnn` -> `first_not_none_in_ls`
    - `alltheutils.utils.squery` -> `search_query`
    - `alltheutils.utils.vls_str` -> `custom_version_ls_to_str`

## 1.0.1

### Fixed

- Fixed `alltheutils.utils.dt_ts` function to be python 3.10 compatible

## 1.0.0

### Removed

- Removed `alltheutils.utils.half_round`

## 0.0.0

Initial release of the package

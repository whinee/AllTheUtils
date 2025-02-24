# Changelog

This software uses [Semantic Versioning v2.0.0](https://semver.org/spec/v2.0.0.html). This changelog is based on [keepachangelog.com v1.1.0](https://keepachangelog.com/en/1.1.0/).

**Types of Changes**

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## 2.0.0 (Unreleased)

### Removed

- Functions deprecated in v1.1.0

## 1.1.0 (Unreleased)

### Added

- MIT License

### Deprecated

- The following functions and renamed them to be more readable (note that the parameters' names might be changed):
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
    - `alltheutils.utils.vls_str` -> `custom_version_ls_to_str`

## 1.0.1

### Fixed

- `alltheutils.utils.dt_ts` function to be python 3.10 compatible

## 1.0.0

### Removed

- method `half_round` from `alltheutils/utils.py` file

## 0.0.0

Initial release of the package
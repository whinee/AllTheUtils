# Bump Version

The table below illustrates the effect of the `poetry version` subcommands on the following version strings:

|subcommand|before|after|
|:---:|:---:|:---:|
|`major`|1.3.0|2.0.0|
|`minor`|2.1.4|2.2.0|
|`patch`|4.1.1|4.1.2|
|`premajor`|1.0.2|2.0.0a0|
|`preminor`|1.0.2|1.1.0a0|
|`prepatch`|1.0.2|1.0.3a0|
|`prerelease`|1.0.2|1.0.3a0|
|`prerelease`|1.0.3a0|1.0.3a1|
|`prerelease`|1.0.3b0|1.0.3b1|

The option `--next-phase` allows the increment of prerelease phase versions.

|subcommand|before|after|
|:---:|:---:|:---:|
|`prerelease –-next-phase`|1.0.3a0|1.0.3b0|
|`prerelease –-next-phase`|1.0.3b0|1.0.3rc0|
|`prerelease –-next-phase`|1.0.3rc0|1.0.3|

import pytest

from alltheutils.exceptions import BumpVersionNoPrerelease, BumpVersionPartUnknown
from alltheutils.utils import bump_version


def test_bump_major_normal():
    assert bump_version("2.2.0", "major") == "3.0.0"


def test_bump_minor_normal():
    assert bump_version("2.2.0", "minor") == "2.3.0"


def test_bump_patch_normal():
    assert bump_version("2.2.0", "patch") == "2.2.1"


def test_bump_prerelease_normal2alpha():
    assert bump_version("2.2.0", "prerelease") == "2.2.0-alpha.1"


def test_bump_prerelease_alpha2beta():
    assert bump_version("2.2.0-alpha.1", "prerelease") == "2.2.0-beta.1"


def test_bump_prerelease_beta2rc():
    assert bump_version("2.2.0-beta.1", "prerelease") == "2.2.0-rc.1"


def test_bump_prerelease_rc2normal():
    assert bump_version("2.2.0-rc.1", "prerelease") == "2.2.0"


def test_bump_prerelease_num():
    assert bump_version("2.2.0-alpha.1", "prerelease_num") == "2.2.0-alpha.2"


def test_bump_unknown_value():
    with pytest.raises(BumpVersionPartUnknown):
        bump_version("2.2.0", "huh?")

def test_bump_no_prerelease():
    with pytest.raises(BumpVersionNoPrerelease):
        bump_version("2.2.0", "prerelease_num")

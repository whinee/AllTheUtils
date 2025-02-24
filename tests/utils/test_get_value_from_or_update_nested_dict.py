import pytest

from alltheutils.utils import get_value_from_or_update_nested_dict


# ================================= Retrieve ===================================
def test_basic_retrieve():
    data = {"you": {"me": "huh?"}}
    assert get_value_from_or_update_nested_dict(data, "you.me") == "huh?"


def test_deep_retrieve():
    data = {"level1": {"level2": {"level3": 42}}}
    assert get_value_from_or_update_nested_dict(data, "level1.level2.level3") == 42


# TODO: differentiate between non-existent path and non-dict path
def test_error_on_retrieving_nonexistent_path():
    data = {"you": {"me": "huh?"}}
    with pytest.raises(KeyError):
        get_value_from_or_update_nested_dict(data, "you.nonexistent")


def test_retrieve_entire_dict_dot_address():
    data = {"unchanged": "yes"}
    assert get_value_from_or_update_nested_dict(data, ".") == {"unchanged": "yes"}


def test_retrieve_entire_dict_dict_empty_address():
    data = {"unchanged": "yes"}
    assert get_value_from_or_update_nested_dict(data, "") == {"unchanged": "yes"}


def test_retrieve_dict_with_integer_key():
    data = {"top": {1: "one"}}
    assert get_value_from_or_update_nested_dict(data, "top.int>1") == "one"


def test_retrieve_dict_with_explicitly_string_integer_key():
    data = {"top": {"1": "one"}}
    assert get_value_from_or_update_nested_dict(data, "top.str>1") == "one"


def test_retrieve_dict_with_implicitly_string_integer_key():
    data = {"top": {"1": "one"}}
    assert get_value_from_or_update_nested_dict(data, "top.1") == "one"


def test_retrieve_from_list_using_integer_key():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    assert get_value_from_or_update_nested_dict(data, "users.int>1.name") == "Bob"


def test_error_on_get_from_list_using_explicitly_string_integer_key():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, "users.str>1.name")

def test_error_on_get_from_list_using_implicitly_string_integer_key():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, "users.str>1.name")


# ================================== Update ====================================
def test_basic_update():
    data = {"you": {"me": "huh?"}}
    get_value_from_or_update_nested_dict(data, "you.me", "haha")
    assert data == {"you": {"me": "haha"}}


def test_deep_update():
    data = {"level1": {"level2": {"level3": "value"}}}
    get_value_from_or_update_nested_dict(data, "level1.level2.level3", 42)
    assert data == {"level1": {"level2": {"level3": 42}}}  # type: ignore[comparison-overlap]


def test_create_missing_path_on_updating_nonexistent_path():
    data = {"you": {}}  # type: ignore[var-annotated]
    get_value_from_or_update_nested_dict(data, "you.new.path", "created!")
    assert data == {"you": {"new": {"path": "created!"}}}


def test_replace_entire_dict_dot_address():
    data = {"old": "data"}
    get_value_from_or_update_nested_dict(data, ".", {"reset": True})
    assert data == {"reset": True}  # type: ignore[comparison-overlap]


def test_replace_entire_dict_empty_address():
    data = {"old": "data"}
    get_value_from_or_update_nested_dict(data, "", {"replaced": "yes"})
    assert data == {"replaced": "yes"}


def test_replace_entire_dict_with_non_dict():
    data = {"old": "data"}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, ".", "just a string")


# TODO: differentiate between non-existent path and non-dict path
def test_error_on_non_dict_path():
    data = {"you": {"me": "huh?"}}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, "you.me.key", "fail")


def test_update_dict_with_integer_key():
    data = {"top": {1: "one"}}
    get_value_from_or_update_nested_dict(data, "top.int>1", "updated")
    assert data == {"top": {1: "updated"}}


def test_update_dict_with_explicitly_string_integer_key():
    data = {"top": {"1": "one"}}
    get_value_from_or_update_nested_dict(data, "top.str>1", "updated")
    assert data == {"top": {"1": "updated"}}


def test_update_dict_with_implicitly_string_integer_key():
    data = {"top": {"1": "one"}}
    get_value_from_or_update_nested_dict(data, "top.1", "updated")
    assert data == {"top": {"1": "updated"}}


def test_error_on_update_nested_dict_with_list_using_implicitly_string_integer_key():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, "users.0.name", "Charlie")


def test_update_nested_dict_with_list_using_integer_key():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    get_value_from_or_update_nested_dict(data, "users.int>1.name", "Charlie")
    assert data == {"users": [{"name": "Alice"}, {"name": "Charlie"}]}


def test_update_root_dict_directly():
    data = {"a": 1, "b": 2}
    get_value_from_or_update_nested_dict(data, ".", {"x": 99, "y": 100})
    assert data == {"x": 99, "y": 100}


def test_create_path_with_int_key():
    data = {"top": {}}  # type: ignore[var-annotated]
    get_value_from_or_update_nested_dict(data, "top.1.new", "created!")
    assert data == {"top": {"1": {"new": "created!"}}}


def test_empty_dict_update():
    data = {}  # type: ignore[var-annotated]
    get_value_from_or_update_nested_dict(data, "new.path", "created!")
    assert data == {"new": {"path": "created!"}}


def test_replace_empty_dict_completely():
    data = {}  # type: ignore[var-annotated]
    get_value_from_or_update_nested_dict(data, ".", {"new_root": "yes"})
    assert data == {"new_root": "yes"}


def test_address_not_existing():
    data = {"exists": "yes"}
    get_value_from_or_update_nested_dict(data, "does.not.exist", "created!")
    assert data == {"exists": "yes", "does": {"not": {"exist": "created!"}}}


def test_non_dict_middle_element():
    data = {"top": "string_value"}
    with pytest.raises(TypeError):
        get_value_from_or_update_nested_dict(data, "top.sub.value", "fail")


def test_no_change_when_empty_dict_passed():
    data = {"unchanged": "yes"}
    get_value_from_or_update_nested_dict(data, ".", {})
    assert data == {"unchanged": "yes"}

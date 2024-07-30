from collections.abc import Callable, Iterable, Sequence
from typing import Any, TypeAlias

Args: TypeAlias = tuple[Any, ...]
CallableAny: TypeAlias = Callable[..., Any]
CallableAnyAny: TypeAlias = Callable[[Any], Any]
CustomDictType: TypeAlias = (
    dict[int, Any] | dict[str, Any] | dict[int | str, Any] | list[tuple[int | str, Any]]
)
IterAny: TypeAlias = Iterable[Any]
IterIterAny: TypeAlias = Iterable[Iterable[Any]]
Kwargs: TypeAlias = dict[str, Any]
ListAny: TypeAlias = list[Any]
Number = float | int
SequenceAny: TypeAlias = Sequence[Any]
TupleAny: TypeAlias = tuple[None] | tuple[Any] | tuple[Any, ...]
TupleStr: TypeAlias = tuple[str] | tuple[str, ...]

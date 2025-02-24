from collections.abc import Callable, Iterable, Sequence
from typing import Any, Optional, TypeAlias

Args: TypeAlias = tuple[Any, ...]
CallableAny: TypeAlias = Callable[..., Any]
CallableAnyAny: TypeAlias = Callable[[Any], Any]
IterAny: TypeAlias = Iterable[Any]
IterIterAny: TypeAlias = Iterable[Iterable[Any]]
Kwargs: TypeAlias = dict[str, Any]
ListAny: TypeAlias = list[Any]
ListOptionalAny: TypeAlias = list[Optional[Any]]
Number = float | int
# RecursiveDict: TypeAlias = (
#     (
#         dict[int, int]
#         |
#         (
#             dict[int, list[int]]
#             | dict[int, list[str]]
#             | dict[int, list["RecursiveDict"]]
#         )
#         | dict[int, "RecursiveDict"]
#         | dict[int, str]
#     ) | (
#         dict[str, int]
#         |
#         (
#             dict[str, list[int]]
#             | dict[str, list[str]]
#             | dict[str, list["RecursiveDict"]]
#         )
#         | dict[str, "RecursiveDict"]
#         | dict[str, str]
#     )
# )
RecursiveDict: TypeAlias = dict
SequenceAny: TypeAlias = Sequence[Any]
TupleAny: TypeAlias = tuple[None] | tuple[Any] | tuple[Any, ...]
TupleStr: TypeAlias = tuple[str] | tuple[str, ...]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryListParams", "Filters", "FiltersUnionMember0"]


class MemoryListParams(TypedDict, total=False):
    filters: Filters
    """Optional filters to apply to the search"""

    limit: str
    """Number of items per page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    page: str
    """Page number to fetch"""

    sort: Literal["createdAt", "updatedAt"]
    """Field to sort by"""


class FiltersUnionMember0(TypedDict, total=False):
    and_: Annotated[Iterable[object], PropertyInfo(alias="AND")]

    or_: Annotated[Iterable[object], PropertyInfo(alias="OR")]


Filters: TypeAlias = Union[FiltersUnionMember0, Dict[str, object]]

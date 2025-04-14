# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchExecuteParams", "Filters", "FiltersUnionMember0"]


class SearchExecuteParams(TypedDict, total=False):
    q: Required[str]
    """Search query string"""

    categories_filter: Annotated[
        List[Literal["technology", "science", "business", "health"]], PropertyInfo(alias="categoriesFilter")
    ]
    """Optional category filters"""

    filters: Filters
    """Optional filters to apply to the search"""

    limit: int
    """Maximum number of results to return"""


class FiltersUnionMember0(TypedDict, total=False):
    and_: Annotated[Iterable[object], PropertyInfo(alias="AND")]

    or_: Annotated[Iterable[object], PropertyInfo(alias="OR")]


Filters: TypeAlias = Union[FiltersUnionMember0, Dict[str, object]]

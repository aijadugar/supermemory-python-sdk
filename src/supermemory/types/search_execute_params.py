# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchExecuteParams"]


class SearchExecuteParams(TypedDict, total=False):
    q: Required[str]
    """Search query string"""

    doc_id: Annotated[str, PropertyInfo(alias="docId")]
    """Optional document ID to search within.

    You can use this to find chunks in a very large document.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["SearchFastResponse", "Result"]


class Result(BaseModel):
    id: str
    """ID of the matching item"""

    content: str
    """Matching content"""

    similarity: float
    """Similarity score"""


class SearchFastResponse(BaseModel):
    results: List[Result]
    """List of fast search results"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryGetResponse", "Doc"]


class Doc(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the memory was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the memory was last updated"""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata associated with the memory"""

    summary: Optional[str] = None
    """Summary of the memory content"""

    title: Optional[str] = None
    """Title of the memory"""


class MemoryGetResponse(BaseModel):
    doc: Doc
    """Memory document details"""

    status: Optional[Literal["queued", "extracting", "chunking", "embedding", "indexing", "done", "failed"]] = None
    """Current processing status of the memory"""

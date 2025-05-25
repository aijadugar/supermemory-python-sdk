# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryGetResponse", "Doc"]


class Doc(BaseModel):
    id: str
    """Unique identifier of the memory."""

    content: Optional[str] = None
    """The content to extract and process into a memory.

    This can be a URL to a website, a PDF, an image, or a video.

    Plaintext: Any plaintext format

    URL: A URL to a website, PDF, image, or video

    We automatically detect the content type from the url's response format.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    metadata: Union[str, float, bool, Dict[str, object], List[object], None] = None
    """Optional metadata for the memory.

    This is used to store additional information about the memory. You can use this
    to store any additional information you need about the memory. Metadata can be
    filtered through. Keys must be strings and are case sensitive. Values can be
    strings, numbers, or booleans. You cannot nest objects.
    """

    status: Literal["unknown", "queued", "extracting", "chunking", "embedding", "indexing", "done", "failed"]
    """Status of the memory"""

    summary: Optional[str] = None
    """Summary of the memory content"""

    title: Optional[str] = None
    """Title of the memory"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    url: Optional[str] = None
    """URL of the memory"""


class MemoryGetResponse(BaseModel):
    doc: Doc
    """Memory object"""

    status: str

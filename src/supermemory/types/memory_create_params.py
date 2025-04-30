# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryCreateParams"]


class MemoryCreateParams(TypedDict, total=False):
    content: Required[str]
    """The content to extract and process into a memory.

    This can be a URL to a website, a PDF, an image, or a video.

    Plaintext: Any plaintext format

    URL: A URL to a website, PDF, image, or video

    We automatically detect the content type from the url's response format.
    """

    id: str

    metadata: Dict[str, Union[str, float, bool]]
    """Optional metadata for the memory.

    This is used to store additional information about the memory. You can use this
    to store any additional information you need about the memory. Metadata can be
    filtered through. Keys must be strings and are case sensitive. Values can be
    strings, numbers, or booleans. You cannot nest objects.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Optional end user ID this memory belongs to.

    This is used to group memories by user. You should use the same ID stored in
    your external system where the user is stored
    """

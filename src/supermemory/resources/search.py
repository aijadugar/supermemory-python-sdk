# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import search_fast_params, search_execute_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_fast_response import SearchFastResponse
from ..types.search_execute_response import SearchExecuteResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/supermemory-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/supermemory-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def execute(
        self,
        *,
        q: str,
        categories_filter: List[Literal["technology", "science", "business", "health"]] | NotGiven = NOT_GIVEN,
        doc_id: str | NotGiven = NOT_GIVEN,
        filters: search_execute_params.Filters | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        only_matching_chunks: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchExecuteResponse:
        """
        Search through documents with metadata filtering

        Args:
          q: Search query string

          categories_filter: Optional category filters

          doc_id: Optional document ID to search within

          filters: Optional filters to apply to the search

          limit: Maximum number of results to return

          only_matching_chunks: If true, only return matching chunks without context

          user_id: End user ID this search is associated with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search",
            body=maybe_transform(
                {
                    "q": q,
                    "categories_filter": categories_filter,
                    "doc_id": doc_id,
                    "filters": filters,
                    "limit": limit,
                    "only_matching_chunks": only_matching_chunks,
                    "user_id": user_id,
                },
                search_execute_params.SearchExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchExecuteResponse,
        )

    def fast(
        self,
        *,
        q: str,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchFastResponse:
        """
        Fast, lossy search using quantized embeddings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fastsearch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    search_fast_params.SearchFastParams,
                ),
            ),
            cast_to=SearchFastResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/supermemory-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/supermemory-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def execute(
        self,
        *,
        q: str,
        categories_filter: List[Literal["technology", "science", "business", "health"]] | NotGiven = NOT_GIVEN,
        doc_id: str | NotGiven = NOT_GIVEN,
        filters: search_execute_params.Filters | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        only_matching_chunks: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchExecuteResponse:
        """
        Search through documents with metadata filtering

        Args:
          q: Search query string

          categories_filter: Optional category filters

          doc_id: Optional document ID to search within

          filters: Optional filters to apply to the search

          limit: Maximum number of results to return

          only_matching_chunks: If true, only return matching chunks without context

          user_id: End user ID this search is associated with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "categories_filter": categories_filter,
                    "doc_id": doc_id,
                    "filters": filters,
                    "limit": limit,
                    "only_matching_chunks": only_matching_chunks,
                    "user_id": user_id,
                },
                search_execute_params.SearchExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchExecuteResponse,
        )

    async def fast(
        self,
        *,
        q: str,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchFastResponse:
        """
        Fast, lossy search using quantized embeddings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fastsearch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    search_fast_params.SearchFastParams,
                ),
            ),
            cast_to=SearchFastResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.execute = to_raw_response_wrapper(
            search.execute,
        )
        self.fast = to_raw_response_wrapper(
            search.fast,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.execute = async_to_raw_response_wrapper(
            search.execute,
        )
        self.fast = async_to_raw_response_wrapper(
            search.fast,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.execute = to_streamed_response_wrapper(
            search.execute,
        )
        self.fast = to_streamed_response_wrapper(
            search.fast,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.execute = async_to_streamed_response_wrapper(
            search.execute,
        )
        self.fast = async_to_streamed_response_wrapper(
            search.fast,
        )

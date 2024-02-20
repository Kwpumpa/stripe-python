# pyright: strict, reportUnnecessaryTypeIgnoreComment=false
# reportUnnecessaryTypeIgnoreComment is set to false because some type ignores are required in some
# python versions but not the others
from typing_extensions import Self, Unpack

from typing import (
    Any,
    AsyncIterator,
    Iterator,
    List,
    Generic,
    TypeVar,
    cast,
    Mapping,
)
from stripe._api_requestor import (
    _APIRequestor,  # pyright: ignore[reportPrivateUsage]
)
from stripe._stripe_object import StripeObject
from stripe._request_options import RequestOptions, extract_options_from_dict

from urllib.parse import quote_plus
from stripe._list_object_base import ListObjectBase

T = TypeVar("T", bound=StripeObject)


class ListObject(ListObjectBase, Generic[T]):
    """
    Represents a list response from the Stripe API. Unlike ListObjectAsync, also contains sync versions of request-making methods like `.auto_paging_iter` and `.next_page`.
    """
    # Even though ListObjectAsync is the "async version" we cannot omit async methods from
    # ListObject and must include both, because this is the class that gets deserialized by default
    # when object: 'list_object'

    def list(self, **params: Mapping[str, Any]) -> Self:
        return cast(
            Self,
            self._request(
                "get",
                self._get_url_for_list(),
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    async def list_async(self, **params: Mapping[str, Any]) -> Self:
        return cast(
            Self,
            await self._request_async(
                "get",
                self._get_url_for_list(),
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    def create(self, **params: Mapping[str, Any]) -> T:
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .create on a list object for the collection of an object without a string "url" property'
            )
        return cast(
            T,
            self._request(
                "post",
                url,
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    def retrieve(self, id: str, **params: Mapping[str, Any]):
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .retrieve on a list object for the collection of an object without a string "url" property'
            )

        url = "%s/%s" % (self.get("url"), quote_plus(id))
        return cast(
            T,
            self._request(
                "get",
                url,
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    def auto_paging_iter(self) -> Iterator[T]:
        page = self

        while True:
            if (
                "ending_before" in self._retrieve_params
                and "starting_after" not in self._retrieve_params
            ):
                for item in reversed(page):
                    yield item
                page = page.previous_page()
            else:
                for item in page:
                    yield item
                page = page.next_page()

            if page.is_empty:
                break

    async def auto_paging_iter_async(self) -> AsyncIterator[T]:
        page = self

        while True:
            if (
                "ending_before" in self._retrieve_params
                and "starting_after" not in self._retrieve_params
            ):
                for item in reversed(page):
                    yield item
                page = await page.previous_page_async()
            else:
                for item in page:
                    yield item
                page = await page.next_page_async()

            if page.is_empty:
                break

    def next_page(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )
        return self.list(
            **self._get_filters_for_next_page(params),
        )

    async def next_page_async(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        return await self.list_async(**self._get_filters_for_next_page(params))

    def _get_filters_for_previous_page(
        self, params: RequestOptions
    ) -> Mapping[str, Any]:
        first_id = getattr(self.data[0], "id")
        if not first_id:
            raise ValueError(
                "Unexpected: element in .data of list object had no id"
            )

        params_with_filters = dict(self._retrieve_params)
        params_with_filters.update({"ending_before": first_id})
        params_with_filters.update(params)
        return params_with_filters

    def previous_page(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        result = self.list(
            **self._get_filters_for_previous_page(params),
        )
        return result

    async def previous_page_async(
        self, **params: Unpack[RequestOptions]
    ) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        result = await self.list_async(
            **self._get_filters_for_previous_page(params)
        )
        return result

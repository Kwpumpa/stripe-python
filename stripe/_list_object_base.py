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

T = TypeVar("T", bound=StripeObject)


class ListObjectBase(StripeObject, Generic[T]):
    OBJECT_NAME = "list"
    data: List[T]
    has_more: bool
    url: str

    def _get_url_for_list(self) -> str:
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .list on a list object without a string "url" property'
            )
        return url

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

    def __getitem__(self, k: str) -> T:
        if isinstance(k, str):  # pyright: ignore
            return super(ListObject, self).__getitem__(k)
        else:
            raise KeyError(
                "You tried to access the %s index, but ListObject types only "
                "support string keys. (HINT: List calls return an object with "
                "a 'data' (which is the data array). You likely want to call "
                ".data[%s])" % (repr(k), repr(k))
            )

    #  Pyright doesn't like this because ListObject inherits from StripeObject inherits from Dict[str, Any]
    #  and so it wants the type of __iter__ to agree with __iter__ from Dict[str, Any]
    #  But we are iterating through "data", which is a List[T].
    def __iter__(  # pyright: ignore
        self,
    ) -> Iterator[T]:
        return getattr(self, "data", []).__iter__()

    def __len__(self) -> int:
        return getattr(self, "data", []).__len__()

    def __reversed__(self) -> Iterator[T]:  # pyright: ignore (see above)
        return getattr(self, "data", []).__reversed__()

    @classmethod
    def _empty_list(
        cls,
        **params: Unpack[RequestOptions],
    ) -> Self:
        return cls._construct_from(
            values={"data": []},
            last_response=None,
            requestor=_APIRequestor._global_with_options(  # pyright: ignore[reportPrivateUsage]
                **params,
            ),
            api_mode="V1",
        )

    @property
    def is_empty(self) -> bool:
        return not self.data

    # Used by child classes for next_page
    def _get_filters_for_next_page(
        self, params: RequestOptions
    ) -> Mapping[str, Any]:

        last_id = getattr(self.data[-1], "id")
        if not last_id:
            raise ValueError(
                "Unexpected: element in .data of list object had no id"
            )

        params_with_filters = dict(self._retrieve_params)
        params_with_filters.update({"starting_after": last_id})
        params_with_filters.update(params)
        return params_with_filters

    # Used by child classes for previous_page
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

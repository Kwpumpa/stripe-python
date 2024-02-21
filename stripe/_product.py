# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._list_object_async import ListObjectAsync
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._search_result_object import SearchResultObject
from stripe._searchable_api_resource import SearchableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import (
    AsyncIterator,
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Union,
    cast,
    overload,
)
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._price import Price
    from stripe._tax_code import TaxCode
    from stripe.entitlements._feature import (
        Feature as EntitlementsFeatureResource,
    )


class Product(
    CreateableAPIResource["Product"],
    DeletableAPIResource["Product"],
    ListableAPIResource["Product"],
    SearchableAPIResource["Product"],
    UpdateableAPIResource["Product"],
):
    """
    Products describe the specific goods or services you offer to your customers.
    For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
    They can be used in conjunction with [Prices](https://stripe.com/docs/api#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription),
    [share a Payment Link](https://stripe.com/docs/payment-links),
    [accept payments with Checkout](https://stripe.com/docs/payments/accept-a-payment#create-product-prices-upfront),
    and more about [Products and Prices](https://stripe.com/docs/products-prices/overview)
    """

    OBJECT_NAME: ClassVar[Literal["product"]] = "product"

    class Feature(StripeObject):
        feature: Optional[ExpandableField["EntitlementsFeatureResource"]]
        """
        The ID of the [Feature](docs/api/entitlements/feature) object. This property is mutually-exclusive with `name`; either one must be specified, but not both.
        """
        name: Optional[str]
        """
        The feature's name. Up to 80 characters long.
        """

    class PackageDimensions(StripeObject):
        height: float
        """
        Height, in inches.
        """
        length: float
        """
        Length, in inches.
        """
        weight: float
        """
        Weight, in ounces.
        """
        width: float
        """
        Width, in inches.
        """

    class Provisioning(StripeObject):
        class GiftCard(StripeObject):
            class FixedAmount(StripeObject):
                amount: int
                """
                The initial amount with which the provisioned gift card will be created.
                """
                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """

            fixed_amount: Optional[FixedAmount]
            type: Literal["fixed_amount"]
            """
            The specific type of gift_card provisioning, only `fixed_amount` currently supported.
            """
            _inner_class_types = {"fixed_amount": FixedAmount}

        gift_card: Optional[GiftCard]
        type: Literal["gift_card"]
        """
        The type of provisioning, only `gift_card` currently supported.
        """
        _inner_class_types = {"gift_card": GiftCard}

    class CreateParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Whether the product is currently available for purchase. Defaults to `true`.
        """
        default_price_data: NotRequired["Product.CreateParamsDefaultPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product.
        """
        description: NotRequired["str"]
        """
        The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        features: NotRequired["List[Product.CreateParamsFeature]"]
        """
        A list of up to 15 features for this product. Entries using `name` are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
        """
        id: NotRequired["str"]
        """
        An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.
        """
        images: NotRequired["List[str]"]
        """
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: str
        """
        The product's name, meant to be displayable to the customer.
        """
        package_dimensions: NotRequired[
            "Product.CreateParamsPackageDimensions"
        ]
        """
        The dimensions of this product for shipping purposes.
        """
        provisioning: NotRequired["Product.CreateParamsProvisioning"]
        """
        Provisioning configuration for this product.
        """
        shippable: NotRequired["bool"]
        """
        Whether this product is shipped (i.e., physical goods).
        """
        statement_descriptor: NotRequired["str"]
        """
        An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

        This may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
         It must contain at least one letter.
        """
        tax_code: NotRequired["str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        type: NotRequired["Literal['good', 'service']"]
        """
        The type of the product. Defaults to `service` if not explicitly specified, enabling use of this product with Subscriptions and Plans. Set this parameter to `good` to use this product with Orders and SKUs. On API versions before `2018-02-05`, this field defaults to `good` for compatibility reasons.
        """
        unit_label: NotRequired["str"]
        """
        A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
        """
        url: NotRequired["str"]
        """
        A URL of a publicly-accessible webpage for this product.
        """

    class CreateParamsDefaultPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        currency_options: NotRequired[
            "Dict[str, Product.CreateParamsDefaultPriceDataCurrencyOptions]"
        ]
        """
        Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """
        recurring: NotRequired["Product.CreateParamsDefaultPriceDataRecurring"]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount` or `unit_amount_decimal` is required.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsDefaultPriceDataCurrencyOptions(TypedDict):
        custom_unit_amount: NotRequired[
            "Product.CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount"
        ]
        """
        When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        tiers: NotRequired[
            "List[Product.CreateParamsDefaultPriceDataCurrencyOptionsTier]"
        ]
        """
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsDefaultPriceDataCurrencyOptionsCustomUnitAmount(
        TypedDict,
    ):
        enabled: bool
        """
        Pass in `true` to enable `custom_unit_amount`, otherwise omit `custom_unit_amount`.
        """
        maximum: NotRequired["int"]
        """
        The maximum unit amount the customer can specify for this item.
        """
        minimum: NotRequired["int"]
        """
        The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.
        """
        preset: NotRequired["int"]
        """
        The starting unit amount which can be updated by the customer.
        """

    class CreateParamsDefaultPriceDataCurrencyOptionsTier(TypedDict):
        flat_amount: NotRequired["int"]
        """
        The flat billing amount for an entire tier, regardless of the number of units in the tier.
        """
        flat_amount_decimal: NotRequired["str"]
        """
        Same as `flat_amount`, but accepts a decimal value representing an integer in the minor units of the currency. Only one of `flat_amount` and `flat_amount_decimal` can be set.
        """
        unit_amount: NotRequired["int"]
        """
        The per unit billing amount for each individual unit for which this tier applies.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """
        up_to: Union[Literal["inf"], int]
        """
        Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use `inf` to define a fallback tier.
        """

    class CreateParamsDefaultPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class CreateParamsFeature(TypedDict):
        feature: NotRequired["str"]
        """
        The ID of the [Feature](docs/api/entitlements/feature) object. This property is mutually-exclusive with `name`; either one must be specified, but not both.
        """
        name: str
        """
        The feature's name. Up to 80 characters long.
        """

    class CreateParamsPackageDimensions(TypedDict):
        height: float
        """
        Height, in inches. Maximum precision is 2 decimal places.
        """
        length: float
        """
        Length, in inches. Maximum precision is 2 decimal places.
        """
        weight: float
        """
        Weight, in ounces. Maximum precision is 2 decimal places.
        """
        width: float
        """
        Width, in inches. Maximum precision is 2 decimal places.
        """

    class CreateParamsProvisioning(TypedDict):
        gift_card: NotRequired["Product.CreateParamsProvisioningGiftCard"]
        type: Literal["gift_card"]
        """
        The type of provisioning, only `gift_card` currently supported.
        """

    class CreateParamsProvisioningGiftCard(TypedDict):
        fixed_amount: NotRequired[
            "Product.CreateParamsProvisioningGiftCardFixedAmount"
        ]
        type: Literal["fixed_amount"]
        """
        The specific type of gift_card provisioning, only `fixed_amount` currently supported.
        """

    class CreateParamsProvisioningGiftCardFixedAmount(TypedDict):
        amount: int
        """
        The initial amount with which the provisioned gift card will be created.
        """
        currency: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Only return products that are active or inactive (e.g., pass `false` to list all inactive products).
        """
        created: NotRequired["Product.ListParamsCreated|int"]
        """
        Only return products that were created during the given date interval.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        ids: NotRequired["List[str]"]
        """
        Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before).
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        shippable: NotRequired["bool"]
        """
        Only return products that can be shipped (i.e., physical, not digital products).
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        type: NotRequired["Literal['good', 'service']"]
        """
        Only return products of this type.
        """
        url: NotRequired["str"]
        """
        Only return products with the given url.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ModifyParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Whether the product is available for purchase.
        """
        default_price: NotRequired["str"]
        """
        The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product.
        """
        description: NotRequired["Literal['']|str"]
        """
        The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        features: NotRequired["Literal['']|List[Product.ModifyParamsFeature]"]
        """
        A list of up to 15 features for this product. Entries using `name` are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
        """
        images: NotRequired["Literal['']|List[str]"]
        """
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired["str"]
        """
        The product's name, meant to be displayable to the customer.
        """
        package_dimensions: NotRequired[
            "Literal['']|Product.ModifyParamsPackageDimensions"
        ]
        """
        The dimensions of this product for shipping purposes.
        """
        shippable: NotRequired["bool"]
        """
        Whether this product is shipped (i.e., physical goods).
        """
        statement_descriptor: NotRequired["str"]
        """
        An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

        This may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
         It must contain at least one letter. May only be set if `type=service`.
        """
        tax_code: NotRequired["Literal['']|str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        unit_label: NotRequired["Literal['']|str"]
        """
        A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`.
        """
        url: NotRequired["Literal['']|str"]
        """
        A URL of a publicly-accessible webpage for this product.
        """

    class ModifyParamsFeature(TypedDict):
        feature: NotRequired["str"]
        """
        The ID of the [Feature](docs/api/entitlements/feature) object. This property is mutually-exclusive with `name`; either one must be specified, but not both.
        """
        name: str
        """
        The feature's name. Up to 80 characters long.
        """

    class ModifyParamsPackageDimensions(TypedDict):
        height: float
        """
        Height, in inches. Maximum precision is 2 decimal places.
        """
        length: float
        """
        Length, in inches. Maximum precision is 2 decimal places.
        """
        weight: float
        """
        Weight, in ounces. Maximum precision is 2 decimal places.
        """
        width: float
        """
        Width, in inches. Maximum precision is 2 decimal places.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SearchParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        page: NotRequired["str"]
        """
        A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
        """
        query: str
        """
        The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products).
        """

    active: bool
    """
    Whether the product is currently available for purchase.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    default_price: Optional[ExpandableField["Price"]]
    """
    The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product.
    """
    description: Optional[str]
    """
    The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    """
    features: List[Feature]
    """
    A list of up to 15 features for this product. Entries using `name` are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
    """
    id: str
    """
    Unique identifier for the object.
    """
    images: List[str]
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str
    """
    The product's name, meant to be displayable to the customer.
    """
    object: Literal["product"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    package_dimensions: Optional[PackageDimensions]
    """
    The dimensions of this product for shipping purposes.
    """
    provisioning: Optional[Provisioning]
    """
    Provisioning configuration for this product.
    """
    shippable: Optional[bool]
    """
    Whether this product is shipped (i.e., physical goods).
    """
    statement_descriptor: Optional[str]
    """
    Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used.
    """
    tax_code: Optional[ExpandableField["TaxCode"]]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    """
    type: Literal["good", "service"]
    """
    The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.
    """
    unit_label: Optional[str]
    """
    A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
    """
    updated: int
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
    url: Optional[str]
    """
    A URL of a publicly-accessible webpage for this product.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def create(cls, **params: Unpack["Product.CreateParams"]) -> "Product":
        """
        Creates a new product object.
        """
        return cast(
            "Product",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Product.CreateParams"]
    ) -> "Product":
        """
        Creates a new product object.
        """
        return cast(
            "Product",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Product",
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Product.DeleteParams"]) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Product",
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Product.DeleteParams"]
    ) -> "Product":
        """
        Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls, **params: Unpack["Product.ListParams"]
    ) -> ListObject["Product"]:
        """
        Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected ListObject from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Product.ListParams"]
    ) -> ListObjectAsync["Product"]:
        """
        Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObjectAsync):

            raise TypeError(
                "Expected ListObjectAsync from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Product.ModifyParams"]
    ) -> "Product":
        """
        Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Product",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Product.ModifyParams"]
    ) -> "Product":
        """
        Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Product",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Product.RetrieveParams"]
    ) -> "Product":
        """
        Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Product.RetrieveParams"]
    ) -> "Product":
        """
        Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ) -> SearchResultObject["Product"]:
        """
        Search for products you've previously created using Stripe's [Search Query Language](https://stripe.com/docs/search#search-query-language).
        Don't use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.
        """
        return cls._search(search_url="/v1/products/search", *args, **kwargs)

    @classmethod
    async def search_async(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ) -> SearchResultObject["Product"]:
        """
        Search for products you've previously created using Stripe's [Search Query Language](https://stripe.com/docs/search#search-query-language).
        Don't use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.
        """
        return await cls._search_async(
            search_url="/v1/products/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ) -> Iterator["Product"]:
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    async def search_auto_paging_iter_async(
        cls, *args, **kwargs: Unpack["Product.SearchParams"]
    ) -> AsyncIterator["Product"]:
        return (
            await cls.search_async(*args, **kwargs)
        ).auto_paging_iter_async()

    _inner_class_types = {
        "features": Feature,
        "package_dimensions": PackageDimensions,
        "provisioning": Provisioning,
    }

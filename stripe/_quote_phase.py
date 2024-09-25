# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._discount import Discount as DiscountResource
    from stripe._line_item import LineItem
    from stripe._tax_rate import TaxRate


class QuotePhase(ListableAPIResource["QuotePhase"]):
    """
    A quote phase describes the line items, coupons, and trialing status of a subscription for a predefined time period.
    """

    OBJECT_NAME: ClassVar[Literal["quote_phase"]] = "quote_phase"

    class InvoiceSettings(StripeObject):
        days_until_due: Optional[int]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                """
                The amount discounted.
                """
                discount: "DiscountResource"
                """
                A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
                It contains information about when the discount began, when it will end, and what it is applied to.

                Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
                """

            class Tax(StripeObject):
                amount: int
                """
                Amount of tax applied for this rate.
                """
                rate: "TaxRate"
                """
                Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

                Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
                """
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                """
                The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
                """
                taxable_amount: Optional[int]
                """
                The amount on which tax is calculated, in cents (or local equivalent).
                """

            discounts: List[Discount]
            """
            The aggregated discounts.
            """
            taxes: List[Tax]
            """
            The aggregated tax amounts by rate.
            """
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        """
        This is the sum of all the discounts.
        """
        amount_shipping: Optional[int]
        """
        This is the sum of all the shipping amounts.
        """
        amount_tax: int
        """
        This is the sum of all the tax amounts.
        """
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        quote: str
        """
        The ID of the quote whose phases will be retrieved.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount_subtotal: int
    """
    Total before any discounts or taxes are applied.
    """
    amount_total: int
    """
    Total after discounts and taxes are applied.
    """
    billing_cycle_anchor: Optional[Literal["reset"]]
    """
    If set to `reset`, the billing_cycle_anchor of the subscription is set to the start of the phase when entering the phase. If unset, then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    """
    collection_method: Optional[
        Literal["charge_automatically", "send_invoice"]
    ]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
    """
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    """
    The default tax rates to apply to the subscription during this phase of the quote.
    """
    discounts: List[ExpandableField["DiscountResource"]]
    """
    The stackable discounts that will be applied to the subscription on this phase. Subscription item discounts are applied before subscription discounts.
    """
    end_date: Optional[int]
    """
    The end of this phase of the quote
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_settings: Optional[InvoiceSettings]
    """
    The invoice settings applicable during this phase.
    """
    iterations: Optional[int]
    """
    Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`.
    """
    line_items: Optional[ListObject["LineItem"]]
    """
    A list of items the customer is being quoted for.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on the subscription schedule's phases when the quote is accepted.
    """
    object: Literal["quote_phase"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    proration_behavior: Literal["always_invoice", "create_prorations", "none"]
    """
    If the quote will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`.
    """
    total_details: TotalDetails
    trial: Optional[bool]
    """
    If set to true the entire phase is counted as a trial and the customer will not be charged for any recurring fees.
    """
    trial_end: Optional[int]
    """
    When the trial ends within the phase.
    """

    @classmethod
    def list(
        cls, **params: Unpack["QuotePhase.ListParams"]
    ) -> ListObject["QuotePhase"]:
        """
        Returns a list of quote phases.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["QuotePhase.ListParams"]
    ) -> ListObject["QuotePhase"]:
        """
        Returns a list of quote phases.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_line_items(
        cls,
        quote_phase: str,
        **params: Unpack["QuotePhase.ListLineItemsParams"],
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/quote_phases/{quote_phase}/line_items".format(
                    quote_phase=sanitize_id(quote_phase)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_line_items(
        quote_phase: str, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/quote_phases/{quote_phase}/line_items".format(
                    quote_phase=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_line_items_async(
        cls,
        quote_phase: str,
        **params: Unpack["QuotePhase.ListLineItemsParams"],
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await cls._static_request_async(
                "get",
                "/v1/quote_phases/{quote_phase}/line_items".format(
                    quote_phase=sanitize_id(quote_phase)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_line_items_async(
        quote_phase: str, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    async def list_line_items_async(
        self, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items_async")
    async def list_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuotePhase.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote phase, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await self._request_async(
                "get",
                "/v1/quote_phases/{quote_phase}/line_items".format(
                    quote_phase=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["QuotePhase.RetrieveParams"]
    ) -> "QuotePhase":
        """
        Retrieves the quote phase with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["QuotePhase.RetrieveParams"]
    ) -> "QuotePhase":
        """
        Retrieves the quote phase with the given ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "invoice_settings": InvoiceSettings,
        "total_details": TotalDetails,
    }

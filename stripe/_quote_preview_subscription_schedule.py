# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._coupon import Coupon
    from stripe._customer import Customer
    from stripe._discount import Discount as DiscountResource
    from stripe._invoice import Invoice
    from stripe._payment_method import PaymentMethod
    from stripe._plan import Plan
    from stripe._price import Price
    from stripe._promotion_code import PromotionCode
    from stripe._subscription import Subscription
    from stripe._tax_rate import TaxRate
    from stripe.test_helpers._test_clock import TestClock


class QuotePreviewSubscriptionSchedule(
    ListableAPIResource["QuotePreviewSubscriptionSchedule"],
):
    OBJECT_NAME: ClassVar[
        Literal["quote_preview_subscription_schedule"]
    ] = "quote_preview_subscription_schedule"

    class AppliesTo(StripeObject):
        new_reference: Optional[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: Optional[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CurrentPhase(StripeObject):
        end_date: int
        """
        The end of this phase of the subscription schedule.
        """
        start_date: int
        """
        The start of this phase of the subscription schedule.
        """

    class DefaultSettings(StripeObject):
        class AutomaticTax(StripeObject):
            class Liability(StripeObject):
                account: Optional[ExpandableField["Account"]]
                """
                The connected account being referenced when `type` is `account`.
                """
                type: Literal["account", "self"]
                """
                Type of the account referenced.
                """

            enabled: bool
            """
            Whether Stripe automatically computes tax on invoices created during this phase.
            """
            liability: Optional[Liability]
            """
            The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
            """
            _inner_class_types = {"liability": Liability}

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            """
            Monetary threshold that triggers the subscription to create an invoice
            """
            reset_billing_cycle_anchor: Optional[bool]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.
            """

        class InvoiceSettings(StripeObject):
            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                """
                The connected account being referenced when `type` is `account`.
                """
                type: Literal["account", "self"]
                """
                Type of the account referenced.
                """

            days_until_due: Optional[int]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
            """
            issuer: Issuer
            _inner_class_types = {"issuer": Issuer}

        class TransferData(StripeObject):
            amount_percent: Optional[float]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: ExpandableField["Account"]
            """
            The account where funds from the payment will be transferred to upon payment success.
            """

        application_fee_percent: Optional[float]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule.
        """
        automatic_tax: Optional[AutomaticTax]
        billing_cycle_anchor: Literal["automatic", "phase_start"]
        """
        Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: Optional[BillingThresholds]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period
        """
        collection_method: Optional[
            Literal["charge_automatically", "send_invoice"]
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
        """
        default_payment_method: Optional[ExpandableField["PaymentMethod"]]
        """
        ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        description: Optional[str]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        invoice_settings: InvoiceSettings
        on_behalf_of: Optional[ExpandableField["Account"]]
        """
        The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details.
        """
        transfer_data: Optional[TransferData]
        """
        The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices.
        """
        _inner_class_types = {
            "automatic_tax": AutomaticTax,
            "billing_thresholds": BillingThresholds,
            "invoice_settings": InvoiceSettings,
            "transfer_data": TransferData,
        }

    class Phase(StripeObject):
        class AddInvoiceItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    """
                    The discount end timestamp.
                    """
                    type: Literal["timestamp"]
                    """
                    The discount end type.
                    """

                coupon: Optional[ExpandableField["Coupon"]]
                """
                ID of the coupon to create a new discount for.
                """
                discount: Optional[ExpandableField["DiscountResource"]]
                """
                ID of an existing discount on the object (or one of its ancestors) to reuse.
                """
                discount_end: Optional[DiscountEnd]
                """
                Details to determine how long the discount should be applied for.
                """
                promotion_code: Optional[ExpandableField["PromotionCode"]]
                """
                ID of the promotion code to create a new discount for.
                """
                _inner_class_types = {"discount_end": DiscountEnd}

            discounts: Optional[List[Discount]]
            """
            The stackable discounts that will be applied to the item.
            """
            price: ExpandableField["Price"]
            """
            ID of the price used to generate the invoice item.
            """
            quantity: Optional[int]
            """
            The quantity of the invoice item.
            """
            tax_rates: Optional[List["TaxRate"]]
            """
            The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
            """
            _inner_class_types = {"discounts": Discount}

        class AutomaticTax(StripeObject):
            class Liability(StripeObject):
                account: Optional[ExpandableField["Account"]]
                """
                The connected account being referenced when `type` is `account`.
                """
                type: Literal["account", "self"]
                """
                Type of the account referenced.
                """

            enabled: bool
            """
            Whether Stripe automatically computes tax on invoices created during this phase.
            """
            liability: Optional[Liability]
            """
            The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
            """
            _inner_class_types = {"liability": Liability}

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            """
            Monetary threshold that triggers the subscription to create an invoice
            """
            reset_billing_cycle_anchor: Optional[bool]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`.
            """

        class Discount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                """
                The discount end timestamp.
                """
                type: Literal["timestamp"]
                """
                The discount end type.
                """

            coupon: Optional[ExpandableField["Coupon"]]
            """
            ID of the coupon to create a new discount for.
            """
            discount: Optional[ExpandableField["DiscountResource"]]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: Optional[DiscountEnd]
            """
            Details to determine how long the discount should be applied for.
            """
            promotion_code: Optional[ExpandableField["PromotionCode"]]
            """
            ID of the promotion code to create a new discount for.
            """
            _inner_class_types = {"discount_end": DiscountEnd}

        class InvoiceSettings(StripeObject):
            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                """
                The connected account being referenced when `type` is `account`.
                """
                type: Literal["account", "self"]
                """
                Type of the account referenced.
                """

            days_until_due: Optional[int]
            """
            Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
            """
            issuer: Optional[Issuer]
            """
            The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
            """
            _inner_class_types = {"issuer": Issuer}

        class Item(StripeObject):
            class BillingThresholds(StripeObject):
                usage_gte: Optional[int]
                """
                Usage threshold that triggers the subscription to create an invoice
                """

            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    """
                    The discount end timestamp.
                    """
                    type: Literal["timestamp"]
                    """
                    The discount end type.
                    """

                coupon: Optional[ExpandableField["Coupon"]]
                """
                ID of the coupon to create a new discount for.
                """
                discount: Optional[ExpandableField["DiscountResource"]]
                """
                ID of an existing discount on the object (or one of its ancestors) to reuse.
                """
                discount_end: Optional[DiscountEnd]
                """
                Details to determine how long the discount should be applied for.
                """
                promotion_code: Optional[ExpandableField["PromotionCode"]]
                """
                ID of the promotion code to create a new discount for.
                """
                _inner_class_types = {"discount_end": DiscountEnd}

            class Trial(StripeObject):
                converts_to: Optional[List[str]]
                """
                List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
                """
                type: Literal["free", "paid"]
                """
                Determines the type of trial for this item.
                """

            billing_thresholds: Optional[BillingThresholds]
            """
            Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period
            """
            discounts: Optional[List[Discount]]
            """
            The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered.
            """
            plan: ExpandableField["Plan"]
            """
            ID of the plan to which the customer should be subscribed.
            """
            price: ExpandableField["Price"]
            """
            ID of the price to which the customer should be subscribed.
            """
            quantity: Optional[int]
            """
            Quantity of the plan to which the customer should be subscribed.
            """
            tax_rates: Optional[List["TaxRate"]]
            """
            The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`.
            """
            trial: Optional[Trial]
            """
            Options that configure the trial on the subscription item.
            """
            _inner_class_types = {
                "billing_thresholds": BillingThresholds,
                "discounts": Discount,
                "trial": Trial,
            }

        class PauseCollection(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            """
            The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
            """

        class TransferData(StripeObject):
            amount_percent: Optional[float]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: ExpandableField["Account"]
            """
            The account where funds from the payment will be transferred to upon payment success.
            """

        class TrialSettings(StripeObject):
            class EndBehavior(StripeObject):
                prorate_up_front: Optional[Literal["defer", "include"]]
                """
                Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
                """

            end_behavior: Optional[EndBehavior]
            """
            Defines how the subscription should behave when a trial ends.
            """
            _inner_class_types = {"end_behavior": EndBehavior}

        add_invoice_items: List[AddInvoiceItem]
        """
        A list of prices and quantities that will generate invoice items appended to the next invoice for this phase.
        """
        application_fee_percent: Optional[float]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule.
        """
        automatic_tax: Optional[AutomaticTax]
        billing_cycle_anchor: Optional[Literal["automatic", "phase_start"]]
        """
        Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: Optional[BillingThresholds]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period
        """
        collection_method: Optional[
            Literal["charge_automatically", "send_invoice"]
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
        """
        coupon: Optional[ExpandableField["Coupon"]]
        """
        ID of the coupon to use during this phase of the subscription schedule.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        default_payment_method: Optional[ExpandableField["PaymentMethod"]]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        default_tax_rates: Optional[List["TaxRate"]]
        """
        The default tax rates to apply to the subscription during this phase of the subscription schedule.
        """
        description: Optional[str]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        discounts: Optional[List[Discount]]
        """
        The stackable discounts that will be applied to the subscription on this phase. Subscription item discounts are applied before subscription discounts.
        """
        end_date: int
        """
        The end of this phase of the subscription schedule.
        """
        invoice_settings: Optional[InvoiceSettings]
        """
        The invoice settings applicable during this phase.
        """
        items: List[Item]
        """
        Subscription items to configure the subscription to during this phase of the subscription schedule.
        """
        metadata: Optional[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered. Updating the underlying subscription's `metadata` directly will not affect the current phase's `metadata`.
        """
        on_behalf_of: Optional[ExpandableField["Account"]]
        """
        The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details.
        """
        pause_collection: Optional[PauseCollection]
        """
        If specified, payment collection for this subscription will be paused.
        """
        proration_behavior: Literal[
            "always_invoice", "create_prorations", "none"
        ]
        """
        If the subscription schedule will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`.
        """
        start_date: int
        """
        The start of this phase of the subscription schedule.
        """
        transfer_data: Optional[TransferData]
        """
        The account (if any) the associated subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices.
        """
        trial_continuation: Optional[Literal["continue", "none"]]
        """
        Specify behavior of the trial when crossing schedule phase boundaries
        """
        trial_end: Optional[int]
        """
        When the trial ends within the phase.
        """
        trial_settings: Optional[TrialSettings]
        """
        Settings related to any trials on the subscription during this phase.
        """
        _inner_class_types = {
            "add_invoice_items": AddInvoiceItem,
            "automatic_tax": AutomaticTax,
            "billing_thresholds": BillingThresholds,
            "discounts": Discount,
            "invoice_settings": InvoiceSettings,
            "items": Item,
            "pause_collection": PauseCollection,
            "transfer_data": TransferData,
            "trial_settings": TrialSettings,
        }

    class Prebilling(StripeObject):
        invoice: ExpandableField["Invoice"]
        """
        ID of the prebilling invoice.
        """
        period_end: int
        """
        The end of the last period for which the invoice pre-bills.
        """
        period_start: int
        """
        The start of the first period for which the invoice pre-bills.
        """
        update_behavior: Optional[Literal["prebill", "reset"]]
        """
        Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the schedule.
    """
    applies_to: AppliesTo
    billing_behavior: Optional[
        Literal["prorate_on_next_phase", "prorate_up_front"]
    ]
    """
    Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
    """
    canceled_at: Optional[int]
    """
    Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch.
    """
    completed_at: Optional[int]
    """
    Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    current_phase: Optional[CurrentPhase]
    """
    Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.
    """
    customer: ExpandableField["Customer"]
    """
    ID of the customer who owns the subscription schedule.
    """
    default_settings: DefaultSettings
    end_behavior: Literal["cancel", "none", "release", "renew"]
    """
    Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["quote_preview_subscription_schedule"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phases: List[Phase]
    """
    Configuration for the subscription schedule's phases.
    """
    prebilling: Optional[Prebilling]
    """
    Time period and invoice for a Subscription billed in advance.
    """
    released_at: Optional[int]
    """
    Time at which the subscription schedule was released. Measured in seconds since the Unix epoch.
    """
    released_subscription: Optional[str]
    """
    ID of the subscription once managed by the subscription schedule (if it is released).
    """
    status: Literal[
        "active", "canceled", "completed", "not_started", "released"
    ]
    """
    The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules).
    """
    subscription: Optional[ExpandableField["Subscription"]]
    """
    ID of the subscription managed by the subscription schedule.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this subscription schedule belongs to.
    """

    @classmethod
    def list(
        cls, **params: Unpack["QuotePreviewSubscriptionSchedule.ListParams"]
    ) -> ListObject["QuotePreviewSubscriptionSchedule"]:
        """
        Preview the schedules that would be generated by accepting the quote
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

    _inner_class_types = {
        "applies_to": AppliesTo,
        "current_phase": CurrentPhase,
        "default_settings": DefaultSettings,
        "phases": Phase,
        "prebilling": Prebilling,
    }

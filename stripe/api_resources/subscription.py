# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import (
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
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card as CardResource
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.source import Source
    from stripe.api_resources.subscription_item import SubscriptionItem
    from stripe.api_resources.subscription_schedule import SubscriptionSchedule
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Subscription(
    CreateableAPIResource["Subscription"],
    DeletableAPIResource["Subscription"],
    ListableAPIResource["Subscription"],
    SearchableAPIResource["Subscription"],
    UpdateableAPIResource["Subscription"],
):
    """
    Subscriptions allow you to charge a customer on a recurring basis.

    Related guide: [Creating subscriptions](https://stripe.com/docs/billing/subscriptions/creating)
    """

    OBJECT_NAME: ClassVar[Literal["subscription"]] = "subscription"

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
        Whether Stripe automatically computes tax on this subscription.
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

    class CancellationDetails(StripeObject):
        comment: Optional[str]
        """
        Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
        """
        feedback: Optional[
            Literal[
                "customer_service",
                "low_quality",
                "missing_features",
                "other",
                "switched_service",
                "too_complex",
                "too_expensive",
                "unused",
            ]
        ]
        """
        The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
        """
        reason: Optional[
            Literal[
                "cancellation_requested", "payment_disputed", "payment_failed"
            ]
        ]
        """
        Why this subscription was canceled.
        """

    class PauseCollection(StripeObject):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """
        resumes_at: Optional[int]
        """
        The time after which the subscription will resume collecting payments.
        """

    class PaymentSettings(StripeObject):
        class PaymentMethodOptions(StripeObject):
            class AcssDebit(StripeObject):
                class MandateOptions(StripeObject):
                    transaction_type: Optional[Literal["business", "personal"]]
                    """
                    Transaction type of the mandate.
                    """

                mandate_options: Optional[MandateOptions]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                """
                Bank account verification method.
                """
                _inner_class_types = {"mandate_options": MandateOptions}

            class Bancontact(StripeObject):
                preferred_language: Literal["de", "en", "fr", "nl"]
                """
                Preferred language of the Bancontact authorization page that the customer is redirected to.
                """

            class Card(StripeObject):
                class MandateOptions(StripeObject):
                    amount: Optional[int]
                    """
                    Amount to be charged for future payments.
                    """
                    amount_type: Optional[Literal["fixed", "maximum"]]
                    """
                    One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
                    """
                    description: Optional[str]
                    """
                    A description of the mandate or subscription that is meant to be displayed to the customer.
                    """

                mandate_options: Optional[MandateOptions]
                network: Optional[
                    Literal[
                        "amex",
                        "cartes_bancaires",
                        "diners",
                        "discover",
                        "eftpos_au",
                        "interac",
                        "jcb",
                        "mastercard",
                        "unionpay",
                        "unknown",
                        "visa",
                    ]
                ]
                """
                Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.
                """
                request_three_d_secure: Optional[Literal["any", "automatic"]]
                """
                We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
                """
                _inner_class_types = {"mandate_options": MandateOptions}

            class CustomerBalance(StripeObject):
                class BankTransfer(StripeObject):
                    class EuBankTransfer(StripeObject):
                        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
                        """
                        The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
                        """

                    eu_bank_transfer: Optional[EuBankTransfer]
                    type: Optional[str]
                    """
                    The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
                    """
                    _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

                bank_transfer: Optional[BankTransfer]
                funding_type: Optional[Literal["bank_transfer"]]
                """
                The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
                """
                _inner_class_types = {"bank_transfer": BankTransfer}

            class Konbini(StripeObject):
                pass

            class UsBankAccount(StripeObject):
                class FinancialConnections(StripeObject):
                    permissions: Optional[
                        List[
                            Literal[
                                "balances",
                                "ownership",
                                "payment_method",
                                "transactions",
                            ]
                        ]
                    ]
                    """
                    The list of permissions to request. The `payment_method` permission must be included.
                    """
                    prefetch: Optional[
                        List[
                            Literal[
                                "balances",
                                "inferred_balances",
                                "ownership",
                                "transactions",
                            ]
                        ]
                    ]
                    """
                    Data features requested to be retrieved upon account creation.
                    """

                financial_connections: Optional[FinancialConnections]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                """
                Bank account verification method.
                """
                _inner_class_types = {
                    "financial_connections": FinancialConnections,
                }

            acss_debit: Optional[AcssDebit]
            """
            This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to invoices created by the subscription.
            """
            bancontact: Optional[Bancontact]
            """
            This sub-hash contains details about the Bancontact payment method options to pass to invoices created by the subscription.
            """
            card: Optional[Card]
            """
            This sub-hash contains details about the Card payment method options to pass to invoices created by the subscription.
            """
            customer_balance: Optional[CustomerBalance]
            """
            This sub-hash contains details about the Bank transfer payment method options to pass to invoices created by the subscription.
            """
            konbini: Optional[Konbini]
            """
            This sub-hash contains details about the Konbini payment method options to pass to invoices created by the subscription.
            """
            us_bank_account: Optional[UsBankAccount]
            """
            This sub-hash contains details about the ACH direct debit payment method options to pass to invoices created by the subscription.
            """
            _inner_class_types = {
                "acss_debit": AcssDebit,
                "bancontact": Bancontact,
                "card": Card,
                "customer_balance": CustomerBalance,
                "konbini": Konbini,
                "us_bank_account": UsBankAccount,
            }

        payment_method_options: Optional[PaymentMethodOptions]
        """
        Payment-method-specific configuration to provide to invoices created by the subscription.
        """
        payment_method_types: Optional[
            List[
                Literal[
                    "ach_credit_transfer",
                    "ach_debit",
                    "acss_debit",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "konbini",
                    "link",
                    "paynow",
                    "paypal",
                    "promptpay",
                    "sepa_credit_transfer",
                    "sepa_debit",
                    "sofort",
                    "us_bank_account",
                    "wechat_pay",
                ]
            ]
        ]
        """
        The list of payment method types to provide to every invoice created by the subscription. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice's default payment method, the subscription's default payment method, the customer's default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
        """
        save_default_payment_method: Optional[
            Literal["off", "on_subscription"]
        ]
        """
        Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds.
        """
        _inner_class_types = {"payment_method_options": PaymentMethodOptions}

    class PendingInvoiceItemInterval(StripeObject):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
        """

    class PendingUpdate(StripeObject):
        billing_cycle_anchor: Optional[int]
        """
        If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.
        """
        expires_at: int
        """
        The point after which the changes reflected by this update will be discarded and no longer applied.
        """
        prebilling_iterations: Optional[int]
        """
        The number of iterations of prebilling to apply.
        """
        subscription_items: Optional[List["SubscriptionItem"]]
        """
        List of subscription items, each with an attached plan, that will be set if the update is applied.
        """
        trial_end: Optional[int]
        """
        Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied.
        """
        trial_from_plan: Optional[bool]
        """
        Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
        """

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
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]
            """
            Indicates how the subscription should change when the trial ends if the user did not provide a payment method.
            """

        end_behavior: EndBehavior
        """
        Defines how a subscription behaves when a free trial ends.
        """
        _inner_class_types = {"end_behavior": EndBehavior}

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            cancellation_details: NotRequired[
                "Subscription.CancelParamsCancellationDetails|None"
            ]
            """
            Details about why this subscription was cancelled
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_now: NotRequired["bool|None"]
            """
            Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items.
            """
            prorate: NotRequired["bool|None"]
            """
            Will generate a proration invoice item that credits remaining unused time until the subscription period end.
            """

        class CancelParamsCancellationDetails(TypedDict):
            comment: NotRequired["Literal['']|str|None"]
            """
            Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
            """
            feedback: NotRequired[
                "Literal['']|Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']|None"
            ]
            """
            The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
            """

        class CreateParams(RequestOptions):
            add_invoice_items: NotRequired[
                "List[Subscription.CreateParamsAddInvoiceItem]|None"
            ]
            """
            A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
            """
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "Subscription.CreateParamsAutomaticTax|None"
            ]
            """
            Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
            """
            backdate_start_date: NotRequired["int|None"]
            """
            For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
            """
            billing_cycle_anchor: NotRequired["int|None"]
            """
            A future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.
            """
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.CreateParamsBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            cancel_at: NotRequired["int|None"]
            """
            A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
            """
            cancel_at_period_end: NotRequired["bool|None"]
            """
            Boolean indicating whether this subscription should cancel at the end of the current period.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            """
            coupon: NotRequired["str|None"]
            """
            The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            customer: str
            """
            The identifier of the customer to subscribe.
            """
            days_until_due: NotRequired["int|None"]
            """
            Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            """
            default_source: NotRequired["str|None"]
            """
            ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
            """
            description: NotRequired["str|None"]
            """
            The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces.
            """
            discounts: NotRequired[
                "Literal['']|List[Subscription.CreateParamsDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_settings: NotRequired[
                "Subscription.CreateParamsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            items: NotRequired["List[Subscription.CreateParamsItem]|None"]
            """
            A list of up to 20 subscription items, each with an attached price.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            off_session: NotRequired["bool|None"]
            """
            Indicates if a customer is on or off-session while an invoice payment is attempted.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge, for each of the subscription's invoices.
            """
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            """
            Only applies to subscriptions with `collection_method=charge_automatically`.

            Use `allow_incomplete` to create subscriptions with `status=incomplete` if the first invoice cannot be paid. Creating subscriptions with this status allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

            Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the payment intent on the first invoice. This allows simpler management of scenarios where additional user actions are needed to pay a subscription's invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the payment intent is not confirmed within 23 hours subscriptions transition to `status=incomplete_expired`, which is a terminal state.

            Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not create a subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.

            `pending_if_incomplete` is only used with updates and cannot be passed when creating a subscription.

            Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first invoice status.
            """
            payment_settings: NotRequired[
                "Subscription.CreateParamsPaymentSettings|None"
            ]
            """
            Payment settings to pass to invoices created by the subscription.
            """
            pending_invoice_item_interval: NotRequired[
                "Literal['']|Subscription.CreateParamsPendingInvoiceItemInterval|None"
            ]
            """
            Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
            """
            prebilling: NotRequired["Subscription.CreateParamsPrebilling|None"]
            """
            If specified, the invoicing for the given billing cycle iterations will be processed now.
            """
            promotion_code: NotRequired["str|None"]
            """
            The API ID of a promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
            """
            transfer_data: NotRequired[
                "Subscription.CreateParamsTransferData|None"
            ]
            """
            If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
            """
            trial_end: NotRequired["Literal['now']|int|None"]
            """
            Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            """
            trial_from_plan: NotRequired["bool|None"]
            """
            Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            """
            trial_period_days: NotRequired["int|None"]
            """
            Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            """
            trial_settings: NotRequired[
                "Subscription.CreateParamsTrialSettings|None"
            ]
            """
            Settings related to subscription trials.
            """

        class CreateParamsTrialSettings(TypedDict):
            end_behavior: "Subscription.CreateParamsTrialSettingsEndBehavior"
            """
            Defines how the subscription should behave when the user's free trial ends.
            """

        class CreateParamsTrialSettingsEndBehavior(TypedDict):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]
            """
            Indicates how the subscription should change when the trial ends if the user did not provide a payment method.
            """

        class CreateParamsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class CreateParamsPrebilling(TypedDict):
            iterations: int
            """
            This is used to determine the number of billing cycles to prebill.
            """
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]
            """
            Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
            """

        class CreateParamsPendingInvoiceItemInterval(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class CreateParamsPaymentSettings(TypedDict):
            payment_method_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            """
            Payment-method-specific configuration to provide to invoices created by the subscription.
            """
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            """
            The list of payment method types (e.g. card) to provide to the invoice's PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice's default payment method, the subscription's default payment method, the customer's default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
            """
            save_default_payment_method: NotRequired[
                "Literal['off', 'on_subscription']|None"
            ]
            """
            Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            """
            This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice's PaymentIntent.
            """
            bancontact: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            """
            This sub-hash contains details about the Bancontact payment method options to pass to the invoice's PaymentIntent.
            """
            card: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            """
            This sub-hash contains details about the Card payment method options to pass to the invoice's PaymentIntent.
            """
            customer_balance: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            """
            This sub-hash contains details about the Bank transfer payment method options to pass to the invoice's PaymentIntent.
            """
            konbini: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            """
            This sub-hash contains details about the Konbini payment method options to pass to the invoice's PaymentIntent.
            """
            us_bank_account: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            This sub-hash contains details about the ACH direct debit payment method options to pass to the invoice's PaymentIntent.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            """
            Additional fields for Financial Connections Session creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            """
            The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
            """
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            """
            List of data features that you would like to retrieve upon account creation.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            """
            Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
            """
            funding_type: NotRequired["str|None"]
            """
            The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            """
            Configuration for eu_bank_transfer funding type.
            """
            type: NotRequired["str|None"]
            """
            The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str
            """
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions|None"
            ]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            """
            Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.
            """
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            """
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
            TypedDict,
        ):
            amount: NotRequired["int|None"]
            """
            Amount to be charged for future payments.
            """
            amount_type: NotRequired["Literal['fixed', 'maximum']|None"]
            """
            One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
            """
            description: NotRequired["str|None"]
            """
            A description of the mandate or subscription that is meant to be displayed to the customer.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            """
            Preferred language of the Bancontact authorization page that the customer is redirected to.
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]
            """
            Transaction type of the mandate.
            """

        class CreateParamsItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.CreateParamsItemBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
            """
            discounts: NotRequired[
                "Literal['']|List[Subscription.CreateParamsItemDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the subscription item.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            plan: NotRequired["str|None"]
            """
            Plan ID for this item, as a string.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "Subscription.CreateParamsItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            """
            trial: NotRequired["Subscription.CreateParamsItemTrial|None"]
            """
            Define options to configure the trial on the subscription item.
            """

        class CreateParamsItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            """
            List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
            """
            type: Literal["free", "paid"]
            """
            Determines the type of trial for this item.
            """

        class CreateParamsItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: "Subscription.CreateParamsItemPriceDataRecurring"
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class CreateParamsItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.CreateParamsItemDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class CreateParamsItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsItemDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class CreateParamsItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class CreateParamsItemBillingThresholds(TypedDict):
            usage_gte: int
            """
            Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
            """

        class CreateParamsInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "Subscription.CreateParamsInvoiceSettingsIssuer|None"
            ]
            """
            The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
            """

        class CreateParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced in the request.
            """

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.CreateParamsDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class CreateParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class CreateParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class CreateParamsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """
            liability: NotRequired[
                "Subscription.CreateParamsAutomaticTaxLiability|None"
            ]
            """
            The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
            """

        class CreateParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced in the request.
            """

        class CreateParamsAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[Subscription.CreateParamsAddInvoiceItemDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the item.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item. Defaults to 1.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
            """

        class CreateParamsAddInvoiceItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class CreateParamsAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class CreateParamsAddInvoiceItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class DeleteDiscountParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            automatic_tax: NotRequired[
                "Subscription.ListParamsAutomaticTax|None"
            ]
            """
            Filter subscriptions by their automatic tax settings.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.
            """
            created: NotRequired["Subscription.ListParamsCreated|int|None"]
            current_period_end: NotRequired[
                "Subscription.ListParamsCurrentPeriodEnd|int|None"
            ]
            current_period_start: NotRequired[
                "Subscription.ListParamsCurrentPeriodStart|int|None"
            ]
            customer: NotRequired["str|None"]
            """
            The ID of the customer whose subscriptions will be retrieved.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            plan: NotRequired["str|None"]
            """
            The ID of the plan whose subscriptions will be retrieved.
            """
            price: NotRequired["str|None"]
            """
            Filter for subscriptions that contain this recurring price ID.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['active', 'all', 'canceled', 'ended', 'incomplete', 'incomplete_expired', 'past_due', 'paused', 'trialing', 'unpaid']|None"
            ]
            """
            The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.
            """
            test_clock: NotRequired["str|None"]
            """
            Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set.
            """

        class ListParamsCurrentPeriodStart(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCurrentPeriodEnd(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """

        class ModifyParams(RequestOptions):
            add_invoice_items: NotRequired[
                "List[Subscription.ModifyParamsAddInvoiceItem]|None"
            ]
            """
            A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
            """
            application_fee_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            """
            automatic_tax: NotRequired[
                "Subscription.ModifyParamsAutomaticTax|None"
            ]
            """
            Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
            """
            billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|None"
            ]
            """
            Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.ModifyParamsBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
            """
            cancel_at: NotRequired["Literal['']|int|None"]
            """
            A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
            """
            cancel_at_period_end: NotRequired["bool|None"]
            """
            Boolean indicating whether this subscription should cancel at the end of the current period.
            """
            cancellation_details: NotRequired[
                "Subscription.ModifyParamsCancellationDetails|None"
            ]
            """
            Details about why this subscription was cancelled
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            """
            coupon: NotRequired["str|None"]
            """
            The ID of the coupon to apply to this subscription. A coupon applied to a subscription will only affect invoices created for that particular subscription.
            """
            days_until_due: NotRequired["int|None"]
            """
            Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            """
            default_source: NotRequired["Literal['']|str|None"]
            """
            ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces.
            """
            discounts: NotRequired[
                "Literal['']|List[Subscription.ModifyParamsDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_settings: NotRequired[
                "Subscription.ModifyParamsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            items: NotRequired["List[Subscription.ModifyParamsItem]|None"]
            """
            A list of up to 20 subscription items, each with an attached price.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            off_session: NotRequired["bool|None"]
            """
            Indicates if a customer is on or off-session while an invoice payment is attempted.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge, for each of the subscription's invoices.
            """
            pause_collection: NotRequired[
                "Literal['']|Subscription.ModifyParamsPauseCollection|None"
            ]
            """
            If specified, payment collection for this subscription will be paused.
            """
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            """
            Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

            Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription's invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

            Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

            Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
            """
            payment_settings: NotRequired[
                "Subscription.ModifyParamsPaymentSettings|None"
            ]
            """
            Payment settings to pass to invoices created by the subscription.
            """
            pending_invoice_item_interval: NotRequired[
                "Literal['']|Subscription.ModifyParamsPendingInvoiceItemInterval|None"
            ]
            """
            Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
            """
            prebilling: NotRequired["Subscription.ModifyParamsPrebilling|None"]
            """
            If specified, the invoicing for the given billing cycle iterations will be processed now.
            """
            promotion_code: NotRequired["str|None"]
            """
            The promotion code to apply to this subscription. A promotion code applied to a subscription will only affect invoices created for that particular subscription.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
            """
            proration_date: NotRequired["int|None"]
            """
            If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#upcoming_invoice) endpoint. It can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations.
            """
            transfer_data: NotRequired[
                "Literal['']|Subscription.ModifyParamsTransferData|None"
            ]
            """
            If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value.
            """
            trial_end: NotRequired["Literal['now']|int|None"]
            """
            Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`.
            """
            trial_from_plan: NotRequired["bool|None"]
            """
            Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            """
            trial_settings: NotRequired[
                "Subscription.ModifyParamsTrialSettings|None"
            ]
            """
            Settings related to subscription trials.
            """

        class ModifyParamsTrialSettings(TypedDict):
            end_behavior: "Subscription.ModifyParamsTrialSettingsEndBehavior"
            """
            Defines how the subscription should behave when the user's free trial ends.
            """

        class ModifyParamsTrialSettingsEndBehavior(TypedDict):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]
            """
            Indicates how the subscription should change when the trial ends if the user did not provide a payment method.
            """

        class ModifyParamsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class ModifyParamsPrebilling(TypedDict):
            iterations: int
            """
            This is used to determine the number of billing cycles to prebill.
            """
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]
            """
            Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
            """

        class ModifyParamsPendingInvoiceItemInterval(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class ModifyParamsPaymentSettings(TypedDict):
            payment_method_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            """
            Payment-method-specific configuration to provide to invoices created by the subscription.
            """
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            """
            The list of payment method types (e.g. card) to provide to the invoice's PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice's default payment method, the subscription's default payment method, the customer's default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
            """
            save_default_payment_method: NotRequired[
                "Literal['off', 'on_subscription']|None"
            ]
            """
            Either `off`, or `on_subscription`. With `on_subscription` Stripe updates `subscription.default_payment_method` when a subscription payment succeeds.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            """
            This sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice's PaymentIntent.
            """
            bancontact: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            """
            This sub-hash contains details about the Bancontact payment method options to pass to the invoice's PaymentIntent.
            """
            card: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            """
            This sub-hash contains details about the Card payment method options to pass to the invoice's PaymentIntent.
            """
            customer_balance: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            """
            This sub-hash contains details about the Bank transfer payment method options to pass to the invoice's PaymentIntent.
            """
            konbini: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            """
            This sub-hash contains details about the Konbini payment method options to pass to the invoice's PaymentIntent.
            """
            us_bank_account: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            This sub-hash contains details about the ACH direct debit payment method options to pass to the invoice's PaymentIntent.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            """
            Additional fields for Financial Connections Session creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            """
            The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
            """
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            """
            List of data features that you would like to retrieve upon account creation.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            """
            Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
            """
            funding_type: NotRequired["str|None"]
            """
            The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            """
            Configuration for eu_bank_transfer funding type.
            """
            type: NotRequired["str|None"]
            """
            The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str
            """
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions|None"
            ]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            """
            Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.
            """
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            """
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
            TypedDict,
        ):
            amount: NotRequired["int|None"]
            """
            Amount to be charged for future payments.
            """
            amount_type: NotRequired["Literal['fixed', 'maximum']|None"]
            """
            One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
            """
            description: NotRequired["str|None"]
            """
            A description of the mandate or subscription that is meant to be displayed to the customer.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            """
            Preferred language of the Bancontact authorization page that the customer is redirected to.
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]
            """
            Transaction type of the mandate.
            """

        class ModifyParamsPauseCollection(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            """
            The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
            """
            resumes_at: NotRequired["int|None"]
            """
            The time after which the subscription will resume collecting payments.
            """

        class ModifyParamsItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.ModifyParamsItemBillingThresholds|None"
            ]
            """
            Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
            """
            clear_usage: NotRequired["bool|None"]
            """
            Delete all usage for a given subscription item. Allowed only when `deleted` is set to `true` and the current plan's `usage_type` is `metered`.
            """
            deleted: NotRequired["bool|None"]
            """
            A flag that, if set to `true`, will delete the specified item.
            """
            discounts: NotRequired[
                "Literal['']|List[Subscription.ModifyParamsItemDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the subscription item.
            """
            id: NotRequired["str|None"]
            """
            Subscription item to update.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            plan: NotRequired["str|None"]
            """
            Plan ID for this item, as a string.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
            """
            price_data: NotRequired[
                "Subscription.ModifyParamsItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            """

        class ModifyParamsItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: "Subscription.ModifyParamsItemPriceDataRecurring"
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class ModifyParamsItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.ModifyParamsItemDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class ModifyParamsItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsItemDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class ModifyParamsItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class ModifyParamsItemBillingThresholds(TypedDict):
            usage_gte: int
            """
            Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
            """

        class ModifyParamsInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "Subscription.ModifyParamsInvoiceSettingsIssuer|None"
            ]
            """
            The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
            """

        class ModifyParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced in the request.
            """

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.ModifyParamsDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class ModifyParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class ModifyParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class ModifyParamsCancellationDetails(TypedDict):
            comment: NotRequired["Literal['']|str|None"]
            """
            Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
            """
            feedback: NotRequired[
                "Literal['']|Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']|None"
            ]
            """
            The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
            """

        class ModifyParamsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            """
            Monetary threshold that triggers the subscription to advance to a new billing period
            """
            reset_billing_cycle_anchor: NotRequired["bool|None"]
            """
            Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
            """

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool
            """
            Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
            """
            liability: NotRequired[
                "Subscription.ModifyParamsAutomaticTaxLiability|None"
            ]
            """
            The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
            """

        class ModifyParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced in the request.
            """

        class ModifyParamsAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[Subscription.ModifyParamsAddInvoiceItemDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the item.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemPriceData|None"
            ]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Quantity for this item. Defaults to 1.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
            """

        class ModifyParamsAddInvoiceItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemDiscountDiscountEnd|None"
            ]
            """
            Details to determine how long the discount should be applied for.
            """

        class ModifyParamsAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            """
            Time span for the redeemed discount.
            """
            timestamp: NotRequired["int|None"]
            """
            A precise Unix timestamp for the discount to end. Must be in the future.
            """
            type: Literal["duration", "timestamp"]
            """
            The type of calculation made to determine when the discount ends.
            """

        class ModifyParamsAddInvoiceItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        class ResumeParams(RequestOptions):
            billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|None"
            ]
            """
            Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). Setting the value to `unchanged` advances the subscription's billing cycle anchor to the period that surrounds the current time. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            """
            Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
            """
            proration_date: NotRequired["int|None"]
            """
            If set, the proration will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            page: NotRequired["str|None"]
            """
            A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            """
            query: str
            """
            The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions).
            """

    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the subscription.
    """
    application_fee_percent: Optional[float]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account.
    """
    automatic_tax: AutomaticTax
    billing_cycle_anchor: int
    """
    Determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.
    """
    billing_thresholds: Optional[BillingThresholds]
    """
    Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period
    """
    cancel_at: Optional[int]
    """
    A date in the future at which the subscription will automatically get canceled
    """
    cancel_at_period_end: bool
    """
    If the subscription has been canceled with the `at_period_end` flag set to `true`, `cancel_at_period_end` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period.
    """
    canceled_at: Optional[int]
    """
    If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state.
    """
    cancellation_details: Optional[CancellationDetails]
    """
    Details about why this subscription was cancelled
    """
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    current_period_end: int
    """
    End of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created.
    """
    current_period_start: int
    """
    Start of the current period that the subscription has been invoiced for.
    """
    customer: ExpandableField["Customer"]
    """
    ID of the customer who owns the subscription.
    """
    days_until_due: Optional[int]
    """
    Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`.
    """
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    """
    ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """
    default_source: Optional[
        ExpandableField[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
    ]
    """
    ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """
    default_tax_rates: Optional[List["TaxRate"]]
    """
    The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
    """
    description: Optional[str]
    """
    The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces.
    """
    discount: Optional["Discount"]
    """
    Describes the current discount applied to this subscription, if there is one. When billing, a discount applied to a subscription overrides a discount applied on a customer-wide basis.
    """
    discounts: Optional[List[ExpandableField["Discount"]]]
    """
    The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
    """
    ended_at: Optional[int]
    """
    If the subscription has ended, the date the subscription ended.
    """
    id: str
    """
    Unique identifier for the object.
    """
    items: ListObject["SubscriptionItem"]
    """
    List of subscription items, each with an attached price.
    """
    latest_invoice: Optional[ExpandableField["Invoice"]]
    """
    The most recent invoice this subscription has generated.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_pending_invoice_item_invoice: Optional[int]
    """
    Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`.
    """
    object: Literal["subscription"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account (if any) the charge was made on behalf of for charges associated with this subscription. See the Connect documentation for details.
    """
    pause_collection: Optional[PauseCollection]
    """
    If specified, payment collection for this subscription will be paused.
    """
    payment_settings: Optional[PaymentSettings]
    """
    Payment settings passed on to invoices created by the subscription.
    """
    pending_invoice_item_interval: Optional[PendingInvoiceItemInterval]
    """
    Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    """
    pending_setup_intent: Optional[ExpandableField["SetupIntent"]]
    """
    You can use this [SetupIntent](https://stripe.com/docs/api/setup_intents) to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication#scenario-2).
    """
    pending_update: Optional[PendingUpdate]
    """
    If specified, [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates) that will be applied to the subscription once the `latest_invoice` has been paid.
    """
    prebilling: Optional[Prebilling]
    """
    Time period and invoice for a Subscription billed in advance.
    """
    schedule: Optional[ExpandableField["SubscriptionSchedule"]]
    """
    The schedule attached to the subscription
    """
    start_date: int
    """
    Date when the subscription was first created. The date might differ from the `created` date due to backdating.
    """
    status: Literal[
        "active",
        "canceled",
        "incomplete",
        "incomplete_expired",
        "past_due",
        "paused",
        "trialing",
        "unpaid",
    ]
    """
    Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, or `unpaid`.

    For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this state can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` state. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal state, the open invoice will be voided and no further invoices will be generated.

    A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over.

    If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings).

    If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this subscription belongs to.
    """
    transfer_data: Optional[TransferData]
    """
    The account (if any) the subscription's payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription's invoices.
    """
    trial_end: Optional[int]
    """
    If the subscription has a trial, the end of that trial.
    """
    trial_settings: Optional[TrialSettings]
    """
    Settings related to subscription trials.
    """
    trial_start: Optional[int]
    """
    If the subscription has a trial, the beginning of that trial.
    """

    @classmethod
    def _cls_cancel(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            cls._static_request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}".format(
                    subscription_exposed_id=util.sanitize_id(
                        subscription_exposed_id
                    )
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def cancel(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            self._request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}".format(
                    subscription_exposed_id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.CreateParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
    ) -> "Discount":
        return cast(
            "Discount",
            cls._static_request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                    subscription_exposed_id=util.sanitize_id(
                        subscription_exposed_id
                    )
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def delete_discount(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
    ) -> "Discount":
        ...

    @overload
    def delete_discount(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
    ) -> "Discount":
        ...

    @class_method_variant("_cls_delete_discount")
    def delete_discount(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
    ) -> "Discount":
        return cast(
            "Discount",
            self._request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                    subscription_exposed_id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.ListParams"]
    ) -> ListObject["Subscription"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Subscription.ModifyParams"]
    ) -> "Subscription":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Subscription",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_resume(
        cls,
        subscription: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            cls._static_request(
                "post",
                "/v1/subscriptions/{subscription}/resume".format(
                    subscription=util.sanitize_id(subscription)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def resume(
        cls,
        subscription: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ) -> "Subscription":
        ...

    @overload
    def resume(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ) -> "Subscription":
        ...

    @class_method_variant("_cls_resume")
    def resume(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            self._request(
                "post",
                "/v1/subscriptions/{subscription}/resume".format(
                    subscription=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Subscription.RetrieveParams"]
    ) -> "Subscription":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Subscription.SearchParams"]
    ) -> SearchResultObject["Subscription"]:
        return cls._search(
            search_url="/v1/subscriptions/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Subscription.SearchParams"]
    ) -> Iterator["Subscription"]:
        return cls.search(*args, **kwargs).auto_paging_iter()

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "billing_thresholds": BillingThresholds,
        "cancellation_details": CancellationDetails,
        "pause_collection": PauseCollection,
        "payment_settings": PaymentSettings,
        "pending_invoice_item_interval": PendingInvoiceItemInterval,
        "pending_update": PendingUpdate,
        "prebilling": Prebilling,
        "transfer_data": TransferData,
        "trial_settings": TrialSettings,
    }

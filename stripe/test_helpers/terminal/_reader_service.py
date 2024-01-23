# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.terminal._reader import Reader
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ReaderService(StripeService):
    class PresentPaymentMethodParams(TypedDict):
        amount_tip: NotRequired["int"]
        """
        Simulated on-reader tip amount.
        """
        card_present: NotRequired[
            "ReaderService.PresentPaymentMethodParamsCardPresent"
        ]
        """
        Simulated data for the card_present payment method.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        interac_present: NotRequired[
            "ReaderService.PresentPaymentMethodParamsInteracPresent"
        ]
        """
        Simulated data for the interac_present payment method.
        """
        type: NotRequired["Literal['card_present', 'interac_present']"]
        """
        Simulated payment type.
        """

    class PresentPaymentMethodParamsCardPresent(TypedDict):
        number: NotRequired["str"]
        """
        The card number, as a string without any separators.
        """

    class PresentPaymentMethodParamsInteracPresent(TypedDict):
        number: NotRequired["str"]
        """
        Card Number
        """

    def present_payment_method(
        self,
        reader: str,
        params: "ReaderService.PresentPaymentMethodParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
        """
        return cast(
            Reader,
            self._requestor.request(
                "post",
                "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                    reader=_util.sanitize_id(reader),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

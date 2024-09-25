# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.invoice_payment package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.invoice_payment import InvoicePayment
    To:
      from stripe import InvoicePayment
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._invoice_payment import (  # noqa
        InvoicePayment,
    )

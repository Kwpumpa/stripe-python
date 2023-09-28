# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.price import Price
    from stripe.api_resources.product import Product


class LineItem(StripeObject):
    """
    A line item.
    """

    OBJECT_NAME = "item"
    amount_discount: int
    amount_subtotal: int
    amount_tax: int
    amount_total: int
    currency: str
    description: str
    discounts: Optional[List[StripeObject]]
    id: str
    object: Literal["item"]
    price: Optional["Price"]
    product: Optional[ExpandableField["Product"]]
    quantity: Optional[int]
    taxes: Optional[List[StripeObject]]

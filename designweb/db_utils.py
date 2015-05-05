__author__ = 'zys'
from designweb.models import *
from django.shortcuts import get_object_or_404

DB_FIELD_STATUS = 'payment_status'
DB_FIELD_IS_PAID = 'is_paid'


def delete_all_items_from_cart(cart_id):
    pass


def mark_all_items_from_order(order_id):
    pass


def update_all_cart_order_after_paid(user, order_id, payment_dict):
    cart = get_object_or_404(Cart, user=user)
    order = get_object_or_404(Order, pk=order_id)
    delete_all_items_from_cart(cart.pk)
    mark_all_items_from_order(order_id)
__author__ = 'zys'
from designweb.models import *
from django.shortcuts import get_object_or_404


def update_all_cart_order_after_paid(user, order_id, payment_dict):
    cart = get_object_or_404(Cart, user=user)
    order = get_object_or_404(Order, pk=order_id)
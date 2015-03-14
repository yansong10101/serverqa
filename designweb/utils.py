__author__ = 'zys'
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER, S3_URL
from django.shortcuts import get_object_or_404
from designweb.models import *


def is_order_list_contain_product(order_list, target):
    for item in order_list:
        if item.product.pk == target:
            return True


def is_cart_list_contain_order_detail(product_list, target):
    for item in product_list:
        if item.pk == target:
            return True


def get_display_dict(title, pass_dict={}):
    display_dict = {'title': title, 'categories': Category.objects.all(), 'storage_host': S3_URL, }
    if pass_dict != {}:
        return dict(list(pass_dict.items()) + list(display_dict.items()))
    return display_dict


def is_user_already_in_group(user, product):
    groups = MicroGroup.objects.filter(is_active=True, product=product)
    for group in groups:
        # remain_time = group.get_remain_time()
        # if remain_time.hour != 0 or remain_time.minute != 0 or remain_time.second != 0:
        remain_time = group.get_remain_time_by_seconds()
        if remain_time > 0:
            for member in group.members.all():
                if member == user:
                    return group
    return None


def is_product_in_user_cart(user, p_id):
    if user.is_authenticated():
        cart = get_object_or_404(Cart, user=user)
        if cart.products.filter(pk=p_id).exists():
            return True
    return False


def is_product_in_cart_details(user, product):
    if user.is_authenticated():
        cart = get_object_or_404(Cart, user=user)
        if cart.cart_details.filter(product=product).exists():
            return True
    return False


# functions for sending mail
def sending_mail_to_multiple(mail_to_list, mail_subject, mail_content):
    send_mail(mail_subject, mail_content, EMAIL_HOST_USER, mail_to_list, fail_silently=False)


def sending_mail_to_single(mail_to, mail_subject, mail_content):
    sending_mail_to_multiple([mail_to, ], mail_subject, mail_content)


def sending_mail_for_new_signup(mail_to):
    sending_mail_to_single(mail_to, 'welcome to use 1 dots', 'this is content for welcome!')
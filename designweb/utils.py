__author__ = 'zys'
from designweb.models import Category, MicroGroup


def is_order_list_contain_product(order_list, target):
    for item in order_list:
        if item.product.pk == target:
            return True


def get_display_dict(title):
    display_dict = {'title': title, 'categories': Category.objects.all()}
    return display_dict


def is_user_already_in_group(user, product):
    groups = MicroGroup.objects.filter(is_active=True, product=product)
    for group in groups:
        for member in group.members.all():
            if member == user:
                return group
    return None
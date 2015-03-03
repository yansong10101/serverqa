__author__ = 'zys'
from designweb.models import Category, MicroGroup


def is_order_list_contain_product(order_list, target):
    for item in order_list:
        if item.product.pk == target:
            return True


def get_display_dict(title, pass_dict={}):
    display_dict = {'title': title, 'categories': Category.objects.all()}
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
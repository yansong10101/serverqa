__author__ = 'zys'
from django.core.cache import cache
from designweb.models import MicroGroup, User
import random
import string
import operator


CODE_EXPIRED = 60 * 60 * 24  # hard code for 1 day
USER_CACHE_EXPIRED = 0  # 30 days or never
M_GROUP_CACHE_EXPIRED = 0  # 30 days or never


def is_in_cache(code):
    return cache.get(code) is not None


def update_micro_group_dict(micro_group):
    member_list = []
    for member in micro_group.members.all():
        member_list.append(member.pk)
    return {'member_list': member_list,
            'total_members': len(member_list),
            'remained_time': micro_group.get_remain_time_by_seconds(),
            'end_of_time': micro_group.get_end_time(),
            'bottom_line': micro_group.activate_line}


# coupon code section
def generate_coupon_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))


def set_coupon_code(group_id, expire_time=CODE_EXPIRED):
    coupon_code = generate_coupon_code()
    while is_in_cache(coupon_code):
        coupon_code = generate_coupon_code()
    coupon_dict = {'group_id': group_id}
    cache.set(coupon_code, coupon_dict, timeout=expire_time)


def verify_coupon_code(code, group_id):
    return is_in_cache(code) and group_id == cache.get(code)
# end of section


# MG timestamp cache utils section <timestamp>:<group_list>
def generate_timestamp_key(time_stamp):
    return time_stamp.strftime('%Y-%m-%d-%H')


def create_or_update_timestamp_cache_model(micro_group):
    group_dict = {'index': []}
    if micro_group is None or not isinstance(micro_group, MicroGroup):
        return group_dict
    cache_key = generate_timestamp_key(micro_group.get_end_time())
    # if timestamp key is in cache, then get it and update with passed-in group obj
    if is_in_cache(cache_key):
        group_dict = cache.get(cache_key)
        if micro_group.pk not in group_dict['index']:
            group_dict['index'].append(micro_group.pk)
    else:
        group_dict['index'].append(micro_group.pk)
    group_dict[micro_group.pk] = update_micro_group_dict(micro_group)
    cache.set(cache_key, group_dict, timeout=M_GROUP_CACHE_EXPIRED)


def remove_user_from_group_cache(end_of_time, group_id):
    cache_key = generate_timestamp_key(end_of_time)
    if is_in_cache(cache_key):
        group_dict = cache.get(cache_key)
        if group_id in group_dict['index']:
            group_dict['index'].remove(group_id)
            del group_dict[group_id]
        cache.set(cache_key, group_dict, timeout=M_GROUP_CACHE_EXPIRED)
# end of section


# MG info by user section <user_id>:<group_list>
def set_cache_user_key_prefix(user_id):
    return 'user_' + str(user_id)


def get_cache_user_id_from_key(user_key):
    return int(user_key.split('_')[1])


def create_or_update_user_cache_model(user, micro_group):
    user_dict = {'index': []}
    if not isinstance(user, User) or not user.is_authenticated():
        return user_dict
    cache_key = set_cache_user_key_prefix(user.pk)
    if is_in_cache(cache_key):
        user_dict = cache.get(cache_key)
        # assume user in the group
        if isinstance(micro_group, MicroGroup):
            if micro_group.pk not in user_dict['index']:
                user_dict['index'].append(micro_group.pk)
    else:
        user_dict['index'].append(micro_group.pk)
    user_dict[micro_group.pk] = update_micro_group_dict(micro_group)
    cache.set(cache_key, user_dict, timeout=USER_CACHE_EXPIRED)


def clean_user_group_cache(user):
    if not isinstance(user, User) or not user.is_authenticated():
        return
    user_cache_key = set_cache_user_key_prefix(user.pk)
    if is_in_cache(user_cache_key):
        user_cache = cache.get(user_cache_key)
        for item in user_cache['index']:
            group_dict = user_cache[item]
            # delete expired and uncompleted group
            if int(group_dict['remained_time']) <= 0 and group_dict['total_members'] < group_dict['bottom_line']:
                user_cache['index'].remove(item)
                del user_cache[item]
                remove_user_from_group_cache(group_dict['end_of_time'], item)
        cache.set(user_cache_key, user_cache, timeout=USER_CACHE_EXPIRED)
    else:
        return None


def fetch_user_group_cache(user):
    if not isinstance(user, User) or not user.is_authenticated():
        return None
    user_cache_key = set_cache_user_key_prefix(user.pk)
    if is_in_cache(user_cache_key):
        user_dict = cache.get(user_cache_key)
        sorted_list = []
        temp_dict = {}
        # sort user_dict with remained time to a list of tuple
        for item in user_dict:
            temp_dict[item] = user_dict[item]['remained_time']
        sorted_tuple_list = sorted(temp_dict.items(), key=operator.itemgetter(1))
        # covert sorted list of tuple to list of dict
        for item in sorted_tuple_list:
            sorted_list.append({item[0], user_dict[item[0]]})
        return sorted_list
    return None
# end of section


def update_caches_by_new_group(user, micro_group):
    create_or_update_timestamp_cache_model(micro_group)
    create_or_update_user_cache_model(user, micro_group)
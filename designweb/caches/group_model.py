__author__ = 'zys'
from designweb.models import MicroGroup
from datetime import datetime
import random
import string


class GroupCache():
    pass


def generate_coupon_code(group_id):
    time_now = datetime.now()
    print(time_now.year)
    print(time_now.month)
    print(time_now.day)
    print(time_now.hour)
    print(time_now.minute)
    coupon_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    print(coupon_code)
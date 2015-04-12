__author__ = 'zys'
import math

# e-you-bao shipping fee -- RMB | USD
# http://www.ems.com.cn/mainservice/ems/guo_ji_e_you_bao.html
USD_RATE = 6.25
POUND_TO_GRAM_RATE = 453.592

E_PER_ITEM_FEE = 7.00
E_PER_GRAM_FEE = 0.08
E_BASE_WEIGHT = 60
E_MAX_WEIGHT_PER_ITEM = 2000


def shipping_fee_calc(weight, item_num=1):
    shipping_fee = E_PER_ITEM_FEE * item_num + E_BASE_WEIGHT * E_PER_GRAM_FEE
    if weight > E_BASE_WEIGHT:
        shipping_fee = E_PER_ITEM_FEE * item_num + weight * E_PER_GRAM_FEE
    # return with USD conversion
    return float('{0:.2f}'.format(shipping_fee / USD_RATE))


def shipping_fee_multi_calc(list_items):
    total_packages = 0
    total_weight = 0
    for item in list_items:
        if item is not None:
            # convert from pound to gram
            weight = item['weight'] * POUND_TO_GRAM_RATE
            num_items = item['total']
            times_num = math.floor(E_MAX_WEIGHT_PER_ITEM / weight)
            if num_items <= times_num:
                total_packages += 1
            else:
                total_packages += math.ceil(num_items / times_num)
            total_weight += weight * num_items
            print(item['name'] + ' -- total pkg -- ' + str(total_packages) + ' -- total W -- ' + str(total_weight))
    return shipping_fee_calc(total_weight, total_packages)


def testing_shipping_calc():
    list_items = [
        {
            'name': 'testing item one',
            'weight': 1.00,
            'total': 1
        },
        {
            'name': 'testing item two',
            'weight': 2.50,
            'total': 2
        }
    ]
    print(shipping_fee_multi_calc(list_items))
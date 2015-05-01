__author__ = 'zys'
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER, S3_URL, S3_STORAGE
from django.shortcuts import get_object_or_404
from designweb.models import *
from designweb.forms import LoginForm, SignupForm
from boto.s3.connection import S3Connection
import mimetypes
import re
from designweb.session_secure import update_session_timeout


def get_display_dict(title, pass_dict={}):
    login_form = LoginForm()
    signup_form = SignupForm()
    display_dict = {'title': title,
                    'categories': Category.objects.all(),
                    'storage_host': S3_URL,
                    'login_form': login_form,
                    'signup_form': signup_form, }
    if pass_dict != {}:
        return dict(list(pass_dict.items()) + list(display_dict.items()))
    return display_dict


def is_order_list_contain_product(order_list, target):
    for item in order_list:
        if item.product.pk == target:
            return True


def is_cart_list_contain_order_detail(product_list, target):
    for item in product_list:
        if item.pk == target:
            return True


def is_user_already_in_group(user, product):
    groups = MicroGroup.objects.filter(is_active=True, product=product)
    for group in groups:
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


# fro order summary page shipping and billing info
def get_profile_address_or_empty(user):
    if user.is_authenticated():
        profile = user.user_profile
        if profile is not None and \
           profile.address1 != '' and \
           profile.city != '' and \
           profile.state != '' and \
           profile.zip != '':
            return profile
    return None


# update address info to database, from user input
def update_order_address_info(user_id, order_id, data):
    user = get_object_or_404(User, pk=user_id)
    order = get_object_or_404(Order, pk=order_id)
    order.shipping_address1 = data['shipping_address1']
    order.shipping_address2 = data['shipping_address2']
    order.shipping_city = data['shipping_city']
    order.shipping_state = data['shipping_state']
    order.shipping_zip = data['shipping_zip']
    order.shipping_phone1 = data['shipping_phone1']
    order.shipping_phone2 = data['shipping_phone2']
    order.billing_address1 = data['billing_address1']
    order.billing_address2 = data['billing_address2']
    order.billing_city = data['billing_city']
    order.billing_state = data['billing_state']
    order.billing_zip = data['billing_zip']
    order.billing_phone1 = data['billing_phone1']
    order.billing_phone2 = data['billing_phone2']
    try:
        order.save()
    except:
        return 'error to save shipping info into database'
    return None


# functions for sending mail
def sending_mail_to_multiple(mail_to_list, mail_subject, mail_content):
    send_mail(mail_subject, mail_content, EMAIL_HOST_USER, mail_to_list, fail_silently=False)


def sending_mail_to_single(mail_to, mail_subject, mail_content):
    sending_mail_to_multiple([mail_to, ], mail_subject, mail_content)


def sending_mail_for_new_signup(mail_to):
    sending_mail_to_single(mail_to, 'welcome to use 1 dots', 'this is content for welcome!')


# AWS S3 image buckets
def validate_and_separate_image_into_dict(image_list, product_dir):
    image_dict = {}
    big_list = []
    small_list = []
    for big_image in image_list:
        big_tokens = (str(big_image).split('.')[0]).split('_')
        if big_tokens[0] == 'b':
            for small_image in image_list:
                small_tokens = (str(small_image).split('.')[0]).split('_')
                if small_tokens[0] == 's' and big_tokens[2] == small_tokens[2]:
                    big_list.append(product_dir + big_image)
                    small_list.append(product_dir + small_image)
                    if big_tokens[2] == '1':
                        image_dict['main_image'] = product_dir + big_image
                    break
    image_dict['big_img'] = big_list
    image_dict['small_img'] = small_list
    return image_dict


def get_s3_bucket_image_by_product(product_code):
    from hookupdesign import settings
    conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    product_dir = 'test/static/products/' + str(product_code) + '/'
    rs = bucket.list(prefix=product_dir)
    image_list = []
    for item in rs:
        bucket_key = item.name
        if mimetypes.guess_type(bucket_key)[0]:  # check if is image file extension, assume only image or none
            image_list.append(re.sub(product_dir, '', bucket_key))
    return validate_and_separate_image_into_dict(image_list, S3_STORAGE + '/' + product_dir)


def get_s3_bucket_main_image_by_product(product_code):
    return get_s3_bucket_image_by_product(product_code)['main_image']
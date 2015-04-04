# from django.test import TestCase
# from designweb import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER, PAYMENT_SANDBOX
import paypalrestsdk
from paypalrestsdk import Payment
import logging
import apscheduler.schedulers.background as aps_background


# Create your tests here.
def db_read():
    user = User.get_full_name(User.objects.filter(username='yansong').first())
    return str(user)


def create_user():
    User.objects.create_user('testOne', email='test@gmail.com', password='testOne')


def mail_test():
    send_mail('Subject here',
              'Here is the message.',
              EMAIL_HOST_USER,
              ['yansong10101@gmail.com'],
              fail_silently=False)


def payment_test(hostname):
    logging.basicConfig(level=logging.INFO)
    print(hostname)

    api = paypalrestsdk.configure(PAYMENT_SANDBOX)

    # print(api.get_token_hash())

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://" + hostname + "/payment/approval/",
            "cancel_url": "http://" + hostname + "/admin"
        },
        "transactions": [
            {
                "amount":
                    {
                        "total": "14",
                        "currency": "USD"
                    },
                "description": "creating a payment"
            }
        ]
    })

    if payment.create():
        print("Payment[%s] created successfully" % payment.id)
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                print("Redirect for approval: %s" % redirect_url)


def payment_execute(payment_id, payer_id, token):

    api = paypalrestsdk.configure(PAYMENT_SANDBOX)

    payment = Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):  # return True or False
        print("Payment[%s] execute successfully" % payment.id)
    else:
        print(payment.error)


def scheduler_test():
    pass
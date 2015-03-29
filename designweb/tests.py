# from django.test import TestCase
# from designweb import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER
import paypalrestsdk


# Create your tests here.
def db_read():
    # user = models.UserProfile.user.objects.all()
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


def payment_test():
    paypalrestsdk.configure({
        'mode': 'sandbox',
        'client_id': 'AbQpRdq8rpVgUkfWBv7ItV7kbmhNizliedoHoj1BbKijMUZuJyVtYgyHVEiDHWLGYubYflq1v8JVl-6m',
        'client_secret': 'EIJs4rr71GXFI4gjEsQYLCIpXSbiXnKg2huwIfRpicsDcD7xSYa-y5_lSR5oTY3e0F_5PsDkYD-k-KK-',
    })
    my_api = paypalrestsdk.Api({
        'mode': 'sandbox',
        'client_id': 'AbQpRdq8rpVgUkfWBv7ItV7kbmhNizliedoHoj1BbKijMUZuJyVtYgyHVEiDHWLGYubYflq1v8JVl-6m',
        'client_secret': 'EIJs4rr71GXFI4gjEsQYLCIpXSbiXnKg2huwIfRpicsDcD7xSYa-y5_lSR5oTY3e0F_5PsDkYD-k-KK-',
    })
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "credit_card",
            "funding_instruments": [{
                "credit_card": {
                    "type": "visa",
                    "number": "4417119669820331",
                    "expire_month": "11",
                    "expire_year": "2018",
                    "cvv2": "874",
                    "first_name": "Joe",
                    "last_name": "Shopper", }}]},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "1.00",
                    "currency": "USD",
                    "quantity": 1, }]},
                "amount": {
                    "total": "1.00",
                    "currency": "USD", },
            "description": "This is the payment transaction description.", }]
        }, api=my_api)
    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)
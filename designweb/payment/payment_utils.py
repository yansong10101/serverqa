__author__ = 'zys'
from paypalrestsdk import Payment, configure
from hookupdesign.settings import PAYMENT_SANDBOX
import logging


def auth_payment():
    api = configure(PAYMENT_SANDBOX)


def get_payment_json(payment_method, host_root, transaction_object, card_info):
    request_json = {
        "intent": "sale",
        "payer": {
            "payment_method": payment_method
        },
        "transactions": [transaction_object, ]
    }
    if payment_method == 'paypal':
        request_json['redirect_urls'] = {
            "return_url": "http://" + host_root + "/payment/approval/",
            "cancel_url": "http://" + host_root + "/payment/failed/"
        }
    elif payment_method == 'credit_card':
        request_json['payer']['funding_instruments'] = [card_info, ]

    return request_json


def payment_process(payment_method, host_root):
    transaction_object = {}
    card_info = {}
    if payment_method == 'paypal':
        transaction_object = {
            "amount":
                {
                    "total": "2520.00",
                    "currency": "USD",
                    "details": {
                        "subtotal": "2500.00",
                        "tax": "10.00",
                        "shipping": "10.00"
                    },
                },
            "description": "creating a payment"
            }
    elif payment_method == 'credit_card':
        transaction_object = {
            "amount":
                {
                    "total": "25.55",
                    "currency": "USD",
                    "details": {
                        "subtotal": "25.00",
                        "tax": "0.05",
                        "shipping": "0.50"
                    }
                },
            "description": "This is the payment transaction description."
            }
        card_info = {
            "credit_card": {
                "type": "visa",
                "number": "4032035160291142",
                "expire_month": "03",
                "expire_year": "2020",
                "cvv2": "874",
                "first_name": "Joe",
                "last_name": "Shopper",
                "billing_address": {
                    "line1": "52 N Main ST",
                    "city": "Johnstown",
                    "state": "OH",
                    "postal_code": "43210",
                    "country_code": "US"
                }
            }
        }

    auth_payment()
    payment = Payment(get_payment_json(payment_method, host_root, transaction_object, card_info))
    is_approve = payment.create()

    payment_dict = {'payment_id': payment.id, 'payment_state': payment.state, 'redirect_url': None}

    if is_approve:
        print("Payment[%s] created successfully" % payment.id)
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                print("Redirect for approval: %s" % redirect_url)
                payment_dict['redirect_url'] = redirect_url
                return payment_dict
    else:
        print('payment cannot be approval, please check your payment info ...')
        return None
    print("Direct credit -- Payment[%s] execute successfully" % (payment.id))
    # for direct_credit return
    return payment_dict


def payment_execute(payment_id, payer_id, token):
    logging.basicConfig(level=logging.INFO)
    payment = Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):  # return True or False
        print("Paypal -- Payment[%s] execute successfully" % (payment.id))
        # for paypal payment return
        return {'payment_id': payment.id, 'payment_state': payment.state}
    else:
        print(payment.error)
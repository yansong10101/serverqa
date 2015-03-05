# from django.test import TestCase
# from designweb import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER


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
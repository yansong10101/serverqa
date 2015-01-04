# from django.test import TestCase
# from designweb import models
from django.contrib.auth.models import User


# Create your tests here.
def db_read():
    # user = models.UserProfile.user.objects.all()
    user = User.get_full_name(User.objects.filter(username='yansong').first())
    return str(user)


def create_user():
    User.objects.create_user('testOne', email='test@gmail.com', password='testOne')

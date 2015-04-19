# from django.test import TestCase
# from designweb import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hookupdesign.settings import EMAIL_HOST_USER


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


def scheduler_test():
    pass


def test_memcachier():
    from django.core.cache import cache
    c_list = ['item one', 'item two', 'item three', 'item four']
    cache.set('list', c_list)
    print(cache.get('list'))
    for item in cache.get('list'):
        print(item)

    c_dict = {'key 1': 'item 1', 'key 2': 'item 2',
              'key 3': {
                  'inner key': 'inner value',
                  'inner test': 'testing'
              }}
    cache.set('dict', c_dict)
    print(cache.get('dict'))

    print(cache.get('dict')['key 1'])
    print(cache.get('dict')['key 3']['inner key'])

    cache.delete('dict')

    print(cache.get('dict'))


def test_memcachier_2():
    from django.core.cache import cache
    cache.set('index', [1, 2, 3, 4])
    c_list = cache.get('index')
    c_list[0] = c_list[0] + 10
    print(c_list)
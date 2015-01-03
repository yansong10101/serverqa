from django.db import models
from django.contrib.auth.models import User


class test_db_query(models.QuerySet):
    def get_all(self):
        return self.filter(state='CA')


# Create your models here.
class test_db(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

    objects = models.Manager()
    cust_objects = test_db_query.as_manager()

    def __unicode__(self):
        return self.user_name


# User profile
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     is_designer = models.BooleanField(default=False)
#     designer_type = models.CharField(max_length=50, blank=True)
#     address1 = models.CharField(max_length=50, blank=True)
#     address2 = models.CharField(max_length=50, blank=True)
#     city = models.CharField(max_length=25, blank=True)
#     state = models.CharField(max_length=2, blank=True)
#     zip = models.CharField(max_length=8, blank=True)
#
#     def raw_data(self):
#         return {
#             'user': self.user.id,
#         }
#
#     def __unicode__(self):
#         return self.user.id
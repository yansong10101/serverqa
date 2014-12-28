from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class test_db(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
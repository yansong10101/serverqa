from django.db import models
from django.contrib.auth.models import User


class ManageTestDB(models.QuerySet):
    def get_all(self):
        return self.filter(state='CA')


# Create your models here.
class TestDB(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(default=00000, blank=True)

    objects = models.Manager()
    test_objects = ManageTestDB.as_manager()

    def __unicode__(self):
        return self.user_name


# User profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_designer = models.BooleanField(default=False)
    designer_type = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=8, blank=True)

    def raw_data(self):
        return {
            'user': self.user.id,
        }

    def has_address_info(self):
        # implement for detecting if this user has full address info for shipping
        pass

    def __unicode__(self):
        return self.user.id


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.category_name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, blank=True, max_digits=7)
    create_date = models.DateTimeField()
    description = models.TextField(blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_customize = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    shipping_msg = models.CharField(max_length=100, blank=True)
    important_msg = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.product_name


class ProductExtension(models.Model):
    product = models.OneToOneField(Product)
    price_range = models.DecimalField(decimal_places=2, blank=True, max_digits=7)
    special_price = models.DecimalField(decimal_places=2, blank=True, max_digits=7)
    message = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    feature = models.TextField(blank=True)
    size = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=25, blank=True)

    def __unicode__(self):
        return self.product.product_name
from django.db import models
from django.contrib.auth.models import User
from datetime import date


# User profile
class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default='', blank=True)
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

    def __str__(self):
        return self.user.id


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=20, unique=True, editable=False)
    price = models.DecimalField(decimal_places=2, blank=True, max_digits=7)
    designer = models.ForeignKey(User, related_name='products')
    category = models.ManyToManyField(Category)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    image_root = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    is_customize = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    number_in_stock = models.IntegerField(default=0)
    shipping_msg = models.CharField(max_length=100, blank=True)
    important_msg = models.CharField(max_length=100, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
            call twice save():
                first time to get pk value from database calculation
                second save() just use to update product_code value
        """
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        current_year = str(date.today().year)
        code_number = str(self.pk).zfill(7)
        self.product_code = current_year + code_number
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.product_name


class ProductExtension(models.Model):
    product = models.OneToOneField(Product, related_name='details')
    price_range = models.DecimalField(decimal_places=2, blank=True, max_digits=8)
    special_price = models.DecimalField(decimal_places=2, blank=True, max_digits=8)
    message = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    feature = models.TextField(blank=True)
    # product attributes
    size = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.product.product_name
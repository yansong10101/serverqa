from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta, time


# User profile
class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, primary_key=True, related_name='user_profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default='', blank=True)
    is_designer = models.BooleanField(default=False, blank=True)
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
        return self.user.first_name + ' ' + self.user.last_name


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=20, unique=True, editable=False)
    price = models.DecimalField(decimal_places=2, blank=True, max_digits=7, null=True)  # if null show 'please call' msg
    designer = models.ForeignKey(User, related_name='products')
    category = models.ManyToManyField(Category, blank=True, related_name='products')
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    image_root = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    is_customize = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    number_in_stock = models.IntegerField(default=0)
    shipping_msg = models.CharField(max_length=100, blank=True)
    important_msg = models.CharField(max_length=100, blank=True)
    group_duration = models.IntegerField(default=4)
    group_discount = models.DecimalField(decimal_places=3, blank=True, max_digits=4, default=0.90)  # ex, 10% off : 0.90
    general_discount = models.DecimalField(decimal_places=3, blank=True, max_digits=4, default=1.00)
    number_like = models.IntegerField(default=0)

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
    product = models.OneToOneField(Product, related_name='details', primary_key=True)
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


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders')
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    total_items = models.IntegerField(blank=True, default=1)
    is_paid = models.BooleanField(default=False)
    # total_pay = models.DecimalField(default=0.00, max_digits=)

    shipping_address1 = models.CharField(max_length=50, blank=True)
    shipping_address2 = models.CharField(max_length=50, blank=True)
    shipping_city = models.CharField(max_length=20, blank=True)
    shipping_state = models.CharField(max_length=2, blank=True)
    shipping_zip = models.CharField(max_length=8, blank=True)
    shipping_phone1 = models.CharField(max_length=15, blank=True)
    shipping_phone2 = models.CharField(max_length=15, blank=True)
    billing_address1 = models.CharField(max_length=50, blank=True)
    billing_address2 = models.CharField(max_length=50, blank=True)
    billing_city = models.CharField(max_length=20, blank=True)
    billing_state = models.CharField(max_length=2, blank=True)
    billing_zip = models.CharField(max_length=8, blank=True)
    billing_phone1 = models.CharField(max_length=15, blank=True)
    billing_phone2 = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.pk


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='details')
    product = models.ForeignKey(Product, related_name='products')  # , unique=True
    number_items = models.IntegerField(default=1, blank=True)
    shipping_company = models.CharField(max_length=50, blank=True)
    shipping_status = models.CharField(max_length=1, blank=True)
    tracking_code = models.CharField(max_length=50, blank=True)
    shipping_date = models.DateTimeField(blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.order.pk)


class WishList(models.Model):
    user = models.OneToOneField(User, related_name='wish_list', primary_key=True)
    products = models.ManyToManyField(Product, related_name='wish_lists', blank=True)
    number_items = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', primary_key=True)
    products = models.ManyToManyField(Product, related_name='carts', blank=True)
    number_items = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_details')
    product = models.ForeignKey(Product, related_name='product')
    number_in_cart = models.IntegerField(default=1)


class MicroGroup(models.Model):
    members = models.ManyToManyField(User, related_name='micro_groups')
    product = models.ForeignKey(Product, related_name='micro_groups')
    owner = models.ForeignKey(User, related_name='micro_group')
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    duration_time = models.IntegerField(default=4)
    group_price = models.DecimalField(decimal_places=2, blank=True, max_digits=7, null=True)
    group_discount = models.DecimalField(decimal_places=3, blank=True, max_digits=4, default=1.00)
    activate_line = models.IntegerField(default=4)

    def __str__(self):
        return self.owner.username + '-' + self.product.product_name

    def get_remain_time(self):
        time_now = datetime.now()
        end_time = self.created_date.replace(tzinfo=None) + timedelta(hours=self.duration_time)
        remain_time = end_time - time_now
        if remain_time.days < 0:
            return time(hour=0, minute=0, second=0)
        seconds = remain_time.seconds
        hour = seconds // 3600
        minute = (seconds % 3600) // 60
        second = (seconds % 60)
        remain_time = time(hour=hour, minute=minute, second=second)
        return remain_time

    def get_remain_time_by_seconds(self):
        time_now = datetime.now()
        end_time = self.created_date.replace(tzinfo=None) + timedelta(hours=self.duration_time)
        remain_time = end_time - time_now
        if remain_time.days < 0:
            return 0
        return remain_time.seconds
from django.contrib import admin
from designweb.models import UserProfile, TestDB, Product, ProductExtension, Category


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TestDB)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductExtension)
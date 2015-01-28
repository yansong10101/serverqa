from django.contrib import admin
from designweb.models import UserProfile, Product, ProductExtension, Category
from django.utils.translation import ugettext_lazy

admin.site.site_header = ugettext_lazy('1 dots admin')
admin.site.site_title = ugettext_lazy('One Dots')


class ExtensionProductInline(admin.StackedInline):
    model = ProductExtension


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'create_date', 'price', 'is_active', )
    list_filter = ('create_date', 'price', 'is_active', )
    ordering = ('-create_date', )

    inlines = [ExtensionProductInline, ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_date', )
    list_filter = ('created_date', )
    ordering = ('category_name', )


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
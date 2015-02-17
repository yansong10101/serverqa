from django.contrib.auth.models import User, Group
from rest_framework import serializers
from designweb.models import Product, Cart, WishList


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='design:product-detail')

    class Meta:
        model = Product
        fields = ('pk', 'url', 'product_name', 'product_code', 'image_root', 'is_active', )


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'product_name', 'product_code', 'price', 'description', 'is_customize', 'shipping_msg',
                  'important_msg', 'image_root', 'is_active', )


class CartSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedIdentityField(view_name='design:product-detail', many=True)

    class Meta:
        model = Cart
        fields = ('user', 'products', )


class WishListSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedIdentityField(view_name='design:product-detail', many=True)

    class Meta:
        model = WishList
        fields = ('user', 'products', )
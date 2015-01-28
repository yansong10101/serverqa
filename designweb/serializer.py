from django.contrib.auth.models import User, Group
from rest_framework import serializers
from designweb.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='design:product-detail')

    class Meta:
        model = Product
        fields = ('url', 'product_name', 'product_code', )
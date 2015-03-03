# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, related_name='cart')),
                ('number_items', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MicroGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('duration_time', models.IntegerField(default=4)),
                ('group_price', models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)),
                ('group_discount', models.DecimalField(max_digits=4, decimal_places=3, blank=True, default=1.0)),
                ('activate_line', models.IntegerField(default=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('total_items', models.IntegerField(blank=True, default=1)),
                ('is_paid', models.BooleanField(default=False)),
                ('shipping_address1', models.CharField(max_length=50, blank=True)),
                ('shipping_address2', models.CharField(max_length=50, blank=True)),
                ('shipping_city', models.CharField(max_length=20, blank=True)),
                ('shipping_state', models.CharField(max_length=2, blank=True)),
                ('shipping_zip', models.CharField(max_length=8, blank=True)),
                ('shipping_phone1', models.CharField(max_length=15, blank=True)),
                ('shipping_phone2', models.CharField(max_length=15, blank=True)),
                ('billing_address1', models.CharField(max_length=50, blank=True)),
                ('billing_address2', models.CharField(max_length=50, blank=True)),
                ('billing_city', models.CharField(max_length=20, blank=True)),
                ('billing_state', models.CharField(max_length=2, blank=True)),
                ('billing_zip', models.CharField(max_length=8, blank=True)),
                ('billing_phone1', models.CharField(max_length=15, blank=True)),
                ('billing_phone2', models.CharField(max_length=15, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number_items', models.IntegerField(blank=True, default=1)),
                ('shipping_company', models.CharField(max_length=50, blank=True)),
                ('shipping_status', models.CharField(max_length=1, blank=True)),
                ('tracking_code', models.CharField(max_length=50, blank=True)),
                ('shipping_date', models.DateTimeField(blank=True, null=True)),
                ('receive_date', models.DateTimeField(blank=True, null=True)),
                ('order', models.ForeignKey(to='designweb.Order', related_name='details')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_code', models.CharField(max_length=20, editable=False, unique=True)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image_root', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_customize', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('number_in_stock', models.IntegerField(default=0)),
                ('shipping_msg', models.CharField(max_length=100, blank=True)),
                ('important_msg', models.CharField(max_length=100, blank=True)),
                ('group_duration', models.IntegerField(default=4)),
                ('group_discount', models.DecimalField(max_digits=4, decimal_places=3, blank=True, default=1.0)),
                ('general_discount', models.DecimalField(max_digits=4, decimal_places=3, blank=True, default=1.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductExtension',
            fields=[
                ('product', models.OneToOneField(to='designweb.Product', serialize=False, primary_key=True, related_name='details')),
                ('price_range', models.DecimalField(max_digits=8, decimal_places=2, blank=True)),
                ('special_price', models.DecimalField(max_digits=8, decimal_places=2, blank=True)),
                ('message', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(blank=True)),
                ('feature', models.TextField(blank=True)),
                ('size', models.CharField(max_length=50, blank=True)),
                ('weight', models.CharField(max_length=20, blank=True)),
                ('color', models.CharField(max_length=25, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, related_name='user_profile')),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, blank=True, default='')),
                ('is_designer', models.BooleanField(default=False)),
                ('designer_type', models.CharField(max_length=50, blank=True)),
                ('address1', models.CharField(max_length=50, blank=True)),
                ('address2', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=25, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(max_length=8, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, related_name='wish_list')),
                ('number_items', models.IntegerField(default=1)),
                ('products', models.ManyToManyField(related_name='wish_lists', to='designweb.Product', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='designweb.Category', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='designer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='products'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(to='designweb.Product', related_name='products', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='orders'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microgroup',
            name='members',
            field=models.ManyToManyField(related_name='micro_groups', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microgroup',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='micro_group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='microgroup',
            name='product',
            field=models.ForeignKey(to='designweb.Product', related_name='micro_groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='carts', to='designweb.Product', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_code', models.CharField(editable=False, max_length=20, unique=True)),
                ('price', models.DecimalField(blank=True, max_digits=7, decimal_places=2)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('is_customize', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('shipping_msg', models.CharField(max_length=100, blank=True)),
                ('important_msg', models.CharField(max_length=100, blank=True)),
                ('category', models.ManyToManyField(to='designweb.Category')),
                ('designer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='products')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price_range', models.DecimalField(blank=True, max_digits=8, decimal_places=2)),
                ('special_price', models.DecimalField(blank=True, max_digits=8, decimal_places=2)),
                ('message', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(blank=True)),
                ('feature', models.TextField(blank=True)),
                ('size', models.CharField(max_length=50, blank=True)),
                ('weight', models.CharField(max_length=20, blank=True)),
                ('color', models.CharField(max_length=25, blank=True)),
                ('product', models.OneToOneField(related_name='details', to='designweb.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('gender', models.CharField(default='', max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True)),
                ('is_designer', models.BooleanField(default=False)),
                ('designer_type', models.CharField(max_length=50, blank=True)),
                ('address1', models.CharField(max_length=50, blank=True)),
                ('address2', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=25, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zip', models.CharField(max_length=8, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

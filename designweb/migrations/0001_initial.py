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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('product_code', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('create_date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_customize', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('shipping_msg', models.CharField(blank=True, max_length=100)),
                ('important_msg', models.CharField(blank=True, max_length=100)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('price_range', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('special_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('message', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('feature', models.TextField(blank=True)),
                ('size', models.CharField(blank=True, max_length=50)),
                ('weight', models.CharField(blank=True, max_length=20)),
                ('color', models.CharField(blank=True, max_length=25)),
                ('product', models.OneToOneField(to='designweb.Product', related_name='details')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, max_length=1, default='')),
                ('is_designer', models.BooleanField(default=False)),
                ('designer_type', models.CharField(blank=True, max_length=50)),
                ('address1', models.CharField(blank=True, max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=25)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=8)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

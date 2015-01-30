# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0004_auto_20150129_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 1, 29, 22, 29, 22, 629694, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(unique=True, editable=False, max_length=20),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0003_auto_20150128_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_created=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=20, unique=True),
            preserve_default=True,
        ),
    ]

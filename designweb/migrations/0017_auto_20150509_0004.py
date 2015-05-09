# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0016_auto_20150504_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prior_level',
            field=models.IntegerField(choices=[('high', 0), ('middle', 1), ('low', 2)], default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='designer',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='products'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='general_discount',
            field=models.DecimalField(decimal_places=3, max_digits=4, default=1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='group_discount',
            field=models.DecimalField(decimal_places=3, max_digits=4, default=1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productextension',
            name='price_range',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productextension',
            name='special_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0.0),
            preserve_default=True,
        ),
    ]

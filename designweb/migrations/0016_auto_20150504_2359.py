# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0015_auto_20150504_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='total_discount',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='total_shipping',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='total_tax',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]

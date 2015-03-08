# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0003_product_number_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group_discount',
            field=models.DecimalField(default=0.9, blank=True, decimal_places=3, max_digits=4),
            preserve_default=True,
        ),
    ]

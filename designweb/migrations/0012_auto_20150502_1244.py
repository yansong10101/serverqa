# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0011_productcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(blank=True, max_length=10, default='NotPaid'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productextension',
            name='weight',
            field=models.CharField(blank=True, max_length=20, default='1.00'),
            preserve_default=True,
        ),
    ]

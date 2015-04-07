# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0007_auto_20150328_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_resource',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_transaction_id',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='shipping_costs',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True),
            preserve_default=True,
        ),
    ]

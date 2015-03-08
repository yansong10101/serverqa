# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(related_name='products', to='designweb.Product'),
            preserve_default=True,
        ),
    ]

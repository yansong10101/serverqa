# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0014_cartdetail_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiver_first_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='receiver_last_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=True,
        ),
    ]

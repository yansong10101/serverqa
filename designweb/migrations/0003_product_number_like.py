# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0002_auto_20150306_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_like',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

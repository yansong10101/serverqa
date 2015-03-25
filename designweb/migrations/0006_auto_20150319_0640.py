# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0005_cartdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microgroup',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

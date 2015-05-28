# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0019_auto_20150513_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manually_set_prior_level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

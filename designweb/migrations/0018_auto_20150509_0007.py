# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0017_auto_20150509_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prior_level',
            field=models.IntegerField(choices=[(0, 'high'), (1, 'middle'), (2, 'low')], default=2),
            preserve_default=True,
        ),
    ]

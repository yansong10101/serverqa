# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0013_category_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='status',
            field=models.CharField(blank=True, max_length=15, choices=[('Active', 'Active'), ('Deleted', 'Deleted')]),
            preserve_default=True,
        ),
    ]

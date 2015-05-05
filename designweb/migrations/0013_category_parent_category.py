# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0012_auto_20150502_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.CharField(choices=[('Color', 'Color'), ('Category', 'Category'), ('Fashion', 'Fashion')], blank=True, max_length=25),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 19, 9, 23, 382700, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

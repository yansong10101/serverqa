# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designweb', '0009_order_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=70)),
                ('is_sent', models.BooleanField(default=False)),
                ('group', models.ForeignKey(to='designweb.MicroGroup', related_name='group_detail')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='group_detail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

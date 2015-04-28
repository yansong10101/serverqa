# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0010_groupdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('reviewer', models.CharField(max_length=50, default='stranger')),
                ('reviewer_id', models.IntegerField(default=0)),
                ('message', models.TextField(max_length=1000, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('photo_img', models.CharField(max_length=25, default='/stranger')),
                ('product', models.ForeignKey(to='designweb.Product', related_name='product_forum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

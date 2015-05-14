# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0018_auto_20150509_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetail',
            name='color',
            field=models.CharField(default='', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='size',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='weight',
            field=models.CharField(blank=True, default='1.00', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='color',
            field=models.CharField(default='', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='size',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='weight',
            field=models.CharField(blank=True, default='1.00', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productextension',
            name='color',
            field=models.CharField(blank=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productextension',
            name='size',
            field=models.CharField(blank=True, max_length=225),
            preserve_default=True,
        ),
    ]

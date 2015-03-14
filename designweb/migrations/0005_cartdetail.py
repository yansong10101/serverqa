# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designweb', '0004_auto_20150308_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('number_in_cart', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(related_name='cart_details', to='designweb.Cart')),
                ('product', models.ForeignKey(related_name='product', to='designweb.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

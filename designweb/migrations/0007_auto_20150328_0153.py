# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designweb', '0006_auto_20150319_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('total_number', models.IntegerField(default=0)),
                ('review_score', models.DecimalField(max_digits=2, decimal_places=1, default=5)),
                ('message', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reviewed_customer')),
                ('product', models.ForeignKey(to='designweb.Product', related_name='product_review')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='average_review_score',
            field=models.DecimalField(max_digits=2, decimal_places=1, default=5),
            preserve_default=True,
        ),
    ]

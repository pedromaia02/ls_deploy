# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 17:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_posts_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 6, 30, 17, 53, 48, 226000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20160907_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]

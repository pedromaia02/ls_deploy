# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_remove_posts_anexo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={},
        ),
        migrations.AddField(
            model_name='posts',
            name='anexo',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='posts',
            table=None,
        ),
    ]

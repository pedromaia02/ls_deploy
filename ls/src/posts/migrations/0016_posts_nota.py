# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_remove_posts_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='nota',
            field=models.FileField(blank=True, max_length=45, null=True, upload_to=b''),
        ),
    ]

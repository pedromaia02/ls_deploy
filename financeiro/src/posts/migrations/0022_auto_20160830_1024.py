# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_posts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'managed': True},
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='nota',
            new_name='anexo',
        ),
        migrations.AlterModelTable(
            name='posts',
            table='financeiros',
        ),
    ]

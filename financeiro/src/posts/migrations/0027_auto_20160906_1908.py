# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_remove_posts_anexo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='posts',
            table='posts',
        ),
    ]

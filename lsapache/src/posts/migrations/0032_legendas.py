# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_contratos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'legendas',
                'managed': False,
            },
        ),
    ]

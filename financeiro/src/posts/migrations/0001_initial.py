# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-25 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('content', models.CharField(blank=True, max_length=45, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'posts',
                'managed': False,
            },
        ),
    ]

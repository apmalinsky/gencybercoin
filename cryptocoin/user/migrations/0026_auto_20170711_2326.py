# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_code_infinite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='userdata',
        ),
        migrations.AddField(
            model_name='userdata',
            name='achievement',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20170712_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='social_engineer',
            new_name='team_number',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20170615_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cost_honory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='cost_permanent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='image_src',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
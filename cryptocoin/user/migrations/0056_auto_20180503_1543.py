# Generated by Django 2.0.3 on 2018-05-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_auto_20180503_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketitem',
            name='image_src',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='achievement',
        ),
        migrations.AddField(
            model_name='achievement',
            name='user_data',
            field=models.ManyToManyField(blank=True, to='user.UserData'),
        ),
    ]

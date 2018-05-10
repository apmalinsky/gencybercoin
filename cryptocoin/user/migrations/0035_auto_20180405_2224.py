# Generated by Django 2.0.3 on 2018-04-06 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_auto_20180405_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='school',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='school',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
        migrations.AlterField(
            model_name='marketitem',
            name='school',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
    ]
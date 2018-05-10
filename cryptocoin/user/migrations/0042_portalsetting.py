# Generated by Django 2.0.3 on 2018-04-11 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_auto_20180410_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(default='false', max_length=50)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School')),
            ],
        ),
    ]
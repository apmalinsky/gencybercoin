# Generated by Django 2.0.3 on 2018-04-10 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20180407_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cost_honory',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cost_permanent',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='image_src',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='username',
        ),
        migrations.AddField(
            model_name='cart',
            name='market_items',
            field=models.ManyToManyField(to='user.MarketItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_data',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserData'),
            preserve_default=False,
        ),
    ]

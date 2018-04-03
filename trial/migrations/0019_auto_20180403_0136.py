# Generated by Django 2.0.3 on 2018-04-02 22:36

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0018_auto_20180402_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='realization_time',
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='globalchecker',
            name='last_checked',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 2, 22, 35, 36, 62477, tzinfo=utc)),
        ),
    ]
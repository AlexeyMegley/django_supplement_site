# Generated by Django 2.0.3 on 2018-03-08 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0003_auto_20180308_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
    ]

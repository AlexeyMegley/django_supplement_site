# Generated by Django 2.0.3 on 2018-03-08 14:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('account_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.BooleanField()),
                ('realization_time', models.DateTimeField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('account_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='patient_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trial.Patient'),
        ),
        migrations.AddField(
            model_name='order',
            name='selling_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial.Selling'),
        ),
        migrations.AddField(
            model_name='account',
            name='role_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trial.Roles'),
        ),
        migrations.AddField(
            model_name='selling',
            name='doctor_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trial.Doctor'),
        ),
    ]
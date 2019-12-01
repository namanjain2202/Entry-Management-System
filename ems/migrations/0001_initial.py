# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateTimeField(auto_now=True, verbose_name=b'checkIn time')),
                ('checkOut', models.DateTimeField(auto_now=True, verbose_name=b'checkOut time')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ems.User'),
        ),
    ]

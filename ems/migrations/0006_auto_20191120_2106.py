# Generated by Django 2.2.7 on 2019-11-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0005_auto_20191120_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='checkIn',
            field=models.DateTimeField(verbose_name='checkIn time'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkOut',
            field=models.DateTimeField(verbose_name='checkOut time'),
        ),
    ]
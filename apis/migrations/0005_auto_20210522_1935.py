# Generated by Django 3.1.11 on 2021-05-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20210522_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer_id',
            field=models.CharField(max_length=200),
        ),
    ]
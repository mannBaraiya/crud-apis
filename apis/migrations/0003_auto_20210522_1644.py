# Generated by Django 3.1.11 on 2021-05-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20210522_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customer_id', models.EmailField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='KeyMapping',
        ),
    ]

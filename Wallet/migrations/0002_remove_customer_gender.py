# Generated by Django 4.0.6 on 2022-09-04 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Gender',
        ),
    ]

# Generated by Django 4.1 on 2022-09-04 16:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=12, null=True)),
                ('account_number', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=10, null=True)),
                ('address', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phonenumber', models.CharField(max_length=10, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('Gender', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('dateandTime', models.DateTimeField()),
                ('date_sent', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=10)),
                ('amount', models.BigIntegerField()),
                ('datetime', models.DateTimeField()),
                ('receipt_number', models.CharField(max_length=8)),
                ('description', models.TextField()),
                ('receipt_type', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(null=True)),
                ('balance', models.PositiveBigIntegerField(null=True)),
                ('transaction', models.IntegerField(null=True)),
                ('date_created', models.DateField(default=datetime.datetime.now, null=True)),
                ('pin', models.PositiveSmallIntegerField(null=True)),
                ('isActive', models.BooleanField(null=True)),
                ('currency', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.URLField(null=True)),
                ('dateandTime', models.DateTimeField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('bonus_credit', models.BooleanField(null=True)),
                ('transaction_reference', models.TextField(null=True)),
                ('transaction_amount', models.IntegerField(null=True)),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('transaction_cost', models.IntegerField()),
                ('currency', models.CharField(max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=20)),
                ('discount', models.IntegerField()),
                ('points', models.SmallIntegerField()),
                ('datetime', models.DateTimeField()),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_reward', to='Wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('payment_due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('loan_term', models.IntegerField(null=True)),
                ('loan_balance', models.IntegerField(null=True)),
                ('dateissue', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.BigIntegerField(null=True)),
                ('loan_purpose', models.CharField(max_length=100, null=True)),
                ('interest_rate', models.IntegerField()),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=15, null=True)),
                ('cardholder_number', models.BigIntegerField(null=True)),
                ('expiry_date', models.DateTimeField(null=True)),
                ('card_type', models.CharField(max_length=10, null=True)),
                ('dateIssued', models.DateField(null=True)),
                ('signature', models.CharField(max_length=5, null=True)),
                ('issuer', models.CharField(max_length=13, null=True)),
                ('CVVcode', models.CharField(max_length=8, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.customer')),
            ],
        ),
    ]
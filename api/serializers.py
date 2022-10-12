# from dataclasses import fields
# from pyexpat import model
from curses import meta
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Transaction, Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "age")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("customer", "balance", "date_created")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_name", "account_number", "balance")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("cardholder_name", "expiry_date", "dateIssued")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("origin", "bonus_credit", "transaction_amount")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("name", "loan_term", "loan_balance")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("first_name","amount","datetime")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("name", "message", "dateandTime")
   
            
            
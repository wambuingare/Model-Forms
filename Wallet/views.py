from ast import If
from atexit import register
from django.shortcuts import render
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm,WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form =CustomerRegistrationForm(register.POST)
        if form.is_valid():
            form.save();
        
    else:
        form = CustomerRegistrationForm()
        return render(request,"wallet/register_customer.html",{'form':form})

def list_customer(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customer_list.html",{'customers':customers})


def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(register.POST)
        if form.is_valid():
            form.save();

    else:
        form = WalletRegistrationForm()
        return render(request,"wallet/register_wallet.html",{'form':form})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{'wallets':wallets})
    
def register_account(request):
    if request.method=="POST":
       form = AccountRegistrationForm(register.POST)
       if form.is_valid():
            form.save();
    else:           
        form = AccountRegistrationForm()
        return render(request, "wallet/register_account.html",{'form':form})
    
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/account_list.html",{'accounts':accounts})

def register_transaction(request):
    if request.method=="POST":
        form = TransactionRegistrationForm(register.POST)
        if form.is_valid():
            form.save();
    else:   
        form = TransactionRegistrationForm()
        return render(request, "wallet/register_transaction.html",{'form':form})
    
def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{'transactions':transactions})

def register_card(request):
    if request.method=="POST":
            form=CardRegistrationForm(register.POST)
            if form.is_valid():
                form.save();
    else:        
        form = CardRegistrationForm()
        return render(request, "wallet/register_card.html",{'form':form})

def list_card(request):
    cards=Card.objects.all()
    return render(request,"wallet/card_list.html",{'cards':cards})

def register_thirdparty(request):
     if request.method=="POST":
            form=ThirdpartyRegistrationForm(register.POST)
            if form.is_valid():
                form.save();
     else:
        form = ThirdpartyRegistrationForm()
        return render(request, "wallet/register_thirdparty.html",{'form':form})

def list_thirdparty(request):
    thirdparties=ThirdParty.objects.all()
    return render(request,"wallet/thirdparty_list.html",{'thirdparties':thirdparties})

def register_notification(request):
      if request.method=="POST":
            form = NotificationRegistrationForm(register.POST) 
            if form.is_valid():
                form.save();
      else:  
       form = NotificationRegistrationForm()
       return render(request, "wallet/register_notification.html",{'form':form})

def list_notification(request):
    notifications=Notification.objects.all()
    return render(request,"wallet/notification_list.html",{'notifications':notifications})

def register_receipt(request):
      if request.method=="POST":
           form = ReceiptRegistrationForm(register.POST)
           if form.is_valid():
             form.save();
      else:
       form = ReceiptRegistrationForm()
       return render(request, "wallet/register_receipt.html",{'form':form})

def list_receipt(request):
    receipts=Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{'receipts':receipts})

def register_loan(request):
    if request.method=="POST":
       form = LoanRegistrationForm(register.POST)
       if form.is_valid():
        form.save();

    else:
     form = LoanRegistrationForm()
     return render(request, "wallet/register_loan.html",{'form':form})

def list_loan(request):
    loans=Loan.objects.all()
    return render(request,"wallet/loan_list.html",{'loans':loans})

def register_reward(request):
    if request.method=="POST":
       form = RewardRegistrationForm(register.POST)
       if form.is_valid():
        form.save();

    else:
     form = RewardRegistrationForm()
     return render(request, "wallet/register_reward.html",{'form':form})

def list_reward(request):
    rewards=Reward.objects.all()
    return render(request,"wallet/reward_list.html",{'rewards':rewards})


  

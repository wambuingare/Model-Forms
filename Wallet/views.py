
from django.shortcuts import redirect, render
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm,WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save();
        
    else:
        form = CustomerRegistrationForm()
        return render(request,"wallet/register_customer.html",{'form':form})

def list_customer(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customer_list.html",{'customers':customers})


def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{'customers':customer})
 

def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
           form.save()
           return redirect("wallet/customer_profile",id=customer)
    else:
          form=CardRegistrationForm(instance=Customer)
          return render(request,"edit_profile.html",{"form":form})
              
def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save();

    else:
        form = WalletRegistrationForm()
        return render(request,"wallet/register_wallet.html",{'form':form})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{'wallets':wallets})
    

def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request,"wallet/wallet_profile.html",{'wallets':wallet})
 

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=wallet)
        if form.is_valid():
           form.save()
           return redirect("wallet/wallet_profile",id=wallet)
    else:
          form=CardRegistrationForm(instance=Wallet)
          return render(request,"edit_wallet.html",{"form":form})
              
def register_account(request):
    if request.method=="POST":
       form = AccountRegistrationForm(request.POST)
       if form.is_valid():
            form.save();
    else:           
        form = AccountRegistrationForm()
        return render(request, "wallet/register_account.html",{'form':form})
    
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/account_list.html",{'accounts':accounts})


def account_profile(request,id):
    account = Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{'accounts':account})
 

def edit_profile(request,id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
           form.save()
           return redirect("wallet/account_profile",id=account)
    else:
          form=CardRegistrationForm(instance=Account)
          return render(request,"edit_profile.html",{"form":form})
              
def register_transaction(request):
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save();
    else:   
        form = TransactionRegistrationForm()
        return render(request, "wallet/register_transaction.html",{'form':form})
    
def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{'transactions':transactions})

def transaction_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{'transactions':transactions})
 

def edit_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
           form.save()
           return redirect("wallet/transaction_profile",id=transaction)
    else:
          form=CardRegistrationForm(instance=Transaction)
          return render(request,"edit_profile.html",{"form":form})
              
def register_card(request):
    if request.method=="POST":
            form=CardRegistrationForm(request.POST)
            if form.is_valid():
                form.save();
    else:        
        form = CardRegistrationForm()
        return render(request, "wallet/register_card.html",{'form':form})

def list_card(request):
    cards=Card.objects.all()
    return render(request,"wallet/card_list.html",{'cards':cards})


def card_profile(request,id):
    card = Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{'cards':card})
 

def edit_profile(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
           form.save()
           return redirect("wallet/card_profile",id=card)
    else:
          form=CardRegistrationForm(instance=Card)
          return render(request,"edit_profile.html",{"form":form})


def register_thirdparty(request):
     if request.method=="POST":
            form=ThirdpartyRegistrationForm(request.POST)
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
            form = NotificationRegistrationForm(request.POST) 
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
           form = ReceiptRegistrationForm(request.POST)
           if form.is_valid():
             form.save();
      else:
       form = ReceiptRegistrationForm()
       return render(request, "wallet/register_receipt.html",{'form':form})

def list_receipt(request):
    receipts=Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{'receipts':receipts})


def receipt_profile(request,id):
    receipt = Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html",{'receipts':receipts})
 

def edit_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
           form.save()
           return redirect("wallet/receipt_profile",id=receipt)
    else:
          form=CardRegistrationForm(instance=Receipt)
          return render(request,"edit_profile.html",{"form":form})
              
def register_loan(request):
    if request.method=="POST":
       form = LoanRegistrationForm(request.POST)
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
       form = RewardRegistrationForm(request.POST)
       if form.is_valid():
        form.save();

    else:
     form = RewardRegistrationForm()
     return render(request, "wallet/register_reward.html",{'form':form})

def list_reward(request):
    rewards=Reward.objects.all()
    return render(request,"wallet/reward_list.html",{'rewards':rewards})


  

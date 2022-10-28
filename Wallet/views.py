from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet, models 
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm, forms

# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save();
        
    else:
        form =CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})

def list_customer(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customer_list.html",{'customer':customers})


def customer_profile(request, id):
    customer= models.Customer.objects.get(id=id)
    return render(request,"customer_profile.html",{'customer':customer})
 

def edit_profile(request,id):
    customer=models.Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
           form.save()
           return redirect("customer_profile",id=customer.id)
    else:
          form=CustomerRegistrationForm(instance=customer)
          return render(request,"edit_profile.html",{"form":form})
              
def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save();

    else:
        form = WalletRegistrationForm()
        return render(request,"register_wallet.html",{'form':form})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{'wallet':wallets})
    

def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request,"wallet_profile.html",{'wallet':wallet})
 

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=wallet)
        if form.is_valid():
           form.save()
           return redirect("edit_wallet",id=wallet.id)
    else:
          form=WalletRegistrationForm(instance=wallet)
          return render(request,"edit_wallet.html",{"form":form})
              
def register_account(request):
    if request.method=="POST":
       form = AccountRegistrationForm(request.POST)
       if form.is_valid():
            form.save();
    else:           
        form = AccountRegistrationForm(request.POST,instance=Account)
        return render(request, "register_account.html",{'form':form})
    
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/account_list.html",{'accounts':accounts})

def account_profile(request,id):
    accounts = Account.objects.get(id=id)
    return render(request,"account_profile.html",{'account':accounts})


def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
           form.save()
           return redirect("account_profile",id=account.id)
    else:
          form=AccountRegistrationForm(instance=account)
          return render(request,"edit_account.html",{"form":form})
              
def register_transaction(request):
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save();
    else:   
        form = TransactionRegistrationForm()
        return render(request, "register_transaction.html",{'form':form})
    
def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{'transaction':transactions})

def transaction_profile(request,id):
    transaction = Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{'transaction':transaction})
 
def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
           form.save()
           return redirect("wallet/transaction_profile",id=transaction.id)
    else:
          form=TransactionRegistrationForm(instance=transaction)
          return render(request,"edit_notification.html",{"form":form})
              
def register_card(request):
    if request.method=="POST":
            form=CardRegistrationForm(request.POST)
            if form.is_valid():
                form.save();
    else:        
        form = CardRegistrationForm()
        return render(request, "register_card.html",{'form':form})

def list_card(request):
    cards=Card.objects.all()
    return render(request,"wallet/card_list.html",{'cards':cards})


def card_profile(request,id):
    card = models.Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{'card':card})
 

def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
           form.save()
           return redirect("wallet/card_profile",id=card)
    else:
          form=CardRegistrationForm(instance=Card)
          return render(request,"edit_card.html",{"form":form})


def register_thirdparty(request):
     if request.method=="POST":
            form=ThirdpartyRegistrationForm(request.POST)
            if form.is_valid():
                form.save();
     else:
        form = ThirdpartyRegistrationForm()
        return render(request, "register_thirdparty.html",{'form':form})

def list_thirdparty(request):
    thirdparties=ThirdParty.objects.all()
    return render(request,"wallet/thirdparty_list.html",{'thirdparty':thirdparties})

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
    return render(request,"wallet/notification_list.html",{'notification':notifications})

def notification_profile(request,id):
    notification = models.Notification.objects.get(id=id)
    return render(request,"wallet/notification_profile.html",{'notification':notification})

def edit_notification(request,id):
    notification=Notification.objects.get(id=id)
    if request.method=="POST":
        form=NotificationRegistrationForm(request.POST,instance=notification)
        if form.is_valid():
           form.save()
           return redirect("wallet/notification_profile",id=notification)
    else:
          form=NotificationRegistrationForm(instance=Notification)
          return render(request,"edit_notification.html",{"form":form})

def register_receipt(request):
      if request.method=="POST":
           form = ReceiptRegistrationForm(request.POST)
           if form.is_valid():
             form.save();
      else:
       form = ReceiptRegistrationForm()
       return render(request, "wallet/register_receipt.html",{'form':form})

def list_receipt(request):
    receipt=Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{'receipt':receipt})

def receipt_profile(request,id):
    receipt = Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html",{'receipt':receipt})
 
def edit_receipt(request,id):
    receipt=Receipt.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
           form.save()
           return redirect("wallet/receipt_profile",id=receipt)
    else:
          form=ReceiptRegistrationForm(instance=receipt)
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
    return render(request,"wallet/loan_list.html",{'loan':loans})

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

class AccountDepositView(views.APIView):
    def post(self, request, format=None):       
      account_id = request.data["account_id"]
      amount = request.data["amount"]
      
      account = Account.objects.get(id=account_id)
      return Response("Account Not Found", status=404)
      
      message, status = account.deposit(amount)
      return Response(message, status=status)



  


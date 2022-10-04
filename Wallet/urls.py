from .views import customer_profile, edit_profile, list_account, list_card, list_customer, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction,register_wallet
from django.urls import path
from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
  


# from .views import register_customer


urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("customers/",list_customer,name ="customer_list"),
    path("wallet/",register_wallet,name="wallet"),
    path("wallets/",list_wallet,name="wallet_list"),
    path("account/",register_account,name="account"),
    path("accounts/",list_account,name="account_list"),
    path("transaction/",register_transaction,name="transaction"),
    path("transactions/",list_transaction,name="transaction_list"),
    path("card/",register_card,name="card"),
    path("cards/",list_card,name="card_list"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("thirdparties/",list_thirdparty,name="thirdparty_list"),
    path("notification/",register_notification,name="notification"),
    path("notifications/",list_notification,name="notification_list"),
    path("receipt/",register_receipt,name="receipt"),
    path("receipts/",list_receipt,name="receipt_list"),
    path("loan/",register_loan,name="loan"),
    path("loans/",list_loan,name="loan_list"),
    path("reward/",register_reward,name="reward"),
    path("rewards/",list_reward,name="reward_list"),

    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("customers/edit/<init:id/",edit_profile,name="edit_profile"),
    path('admin/', admin.site.urls),  


  
]

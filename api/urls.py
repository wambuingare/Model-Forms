from django.db import router
from django.urls import path, include
from rest_framework import routers

from Wallet.models import Transaction
from Wallet.views import AccountDepositView
from .views import AccountViewSet, CardViewSet, CustomerViewSet, LoanViewSet, NotificationViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"wallets",WalletViewSet)
router.register(r"accounts",AccountViewSet)
router.register(r"cards",CardViewSet)
router.register(r"transactions",TransactionViewSet)
router.register(r"loans",LoanViewSet)
router.register(r"receipts",ReceiptViewSet)
router.register(r"notifications",NotificationViewSet)


urlpatterns = [
    path("",include(router.urls)),


    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),


]



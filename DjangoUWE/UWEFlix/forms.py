from django.forms import ModelForm
from .models import ManageAccount

class ManageAccountsForm(ModelForm):
    class Meta:
        model = ManageAccount
        fields = ('clubName', 'acc_name', 'acc_cardNumber', 'acc_cardExpiryMonth', 'acc_cardExpiryYear', 'acc_discountRate')
from django.forms import ModelForm
from .models import Order
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['customer','Delivery_name','street','address','Card_number','comments']

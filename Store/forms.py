from django import forms
from Store.models import Store,productStore
from product.models import Product
class StoreForm(forms.ModelForm):
    last_modification=forms.DateField(widget=forms.DateInput(attrs={'class':"form-control", 'type':"date"}))
    class Meta:
        model=Store
        fields=['name','last_modification','logo']
        widgets={
            'name': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Enter username ', 'required': True, } ),
        }
class productStoreForm(forms.ModelForm):
    product=forms.ModelChoiceField(queryset=Product.objects.all(),widget=forms.Select( attrs={ 'class': 'form-control', 'required': True, } ))
    store=forms.ModelChoiceField(queryset=Store.objects.all(),widget=forms.Select( attrs={ 'class': 'form-control', 'required': True, } ))
    
    class Meta:
        model=productStore
        fields=['product','store']
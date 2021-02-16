from django import forms
from .models import Product
from django.forms import ImageField

from Category.models import Category,subCategory
from string import Template
from django.utils.safestring import mark_safe

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))
class ProductForm(forms.ModelForm):
    # photo = ImageField(widget=PictureWidget)
    sub_category=forms.ModelChoiceField(queryset=subCategory.objects.all(),widget=forms.Select( attrs={ 'class': 'form-control', 'required': True, } ))
    last_modification=forms.DateField(widget=forms.DateInput(attrs={'class':"form-control", 'type':"date"}))
    class Meta:
        model=Product
        fields=['name','model','quntity','price','last_modification','weight','sub_category','RecieveCard_number','image']
        widgets={
            'name': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Enter name ', 'required': True, } ),
            'model':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter model ', 'required': True, } ),
            'quntity':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter quntity ','type':'number', 'required': True, } ),
            'price':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter price ','type':'number', 'required': True, } ),
            'weight':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter  weight','type':'number', 'required': True, } ),
            'RecieveCard_number':forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter receipt card number','type':'number', 'required': True, } ),
            
        }

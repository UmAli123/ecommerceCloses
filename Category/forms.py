from django import forms
from .models import subCategory,Category
class CategoryForm(forms.ModelForm):
    category_name =forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control col-12', 'placeholder': 'category name ', 'required': True, }))
    laste_Modified=forms.DateField(widget=forms.DateInput(attrs={'class':"form-control", 'type':"date",'value':"2021-02-19"}))
    class Meta:
        model=Category
        fields=['category_name','laste_Modified']
       

class subCategoryForms(forms.ModelForm):
    sub_name =forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control col-12', 'placeholder': 'category name ', 'required': True, }))
    class Meta:
        model =subCategory
        fields=['sub_name',]
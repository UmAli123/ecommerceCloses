from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserCloses

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter Your Email', 'required': True, }))
    phone_no =forms.CharField(max_length=13,widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter Your Phone ', 'required': True, }))
    # phone_no = forms.RegexField(regex=r'^\+((2499)|(2491))\d{8}$',max_length=13,
    # error_messages = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name', 'required': True,}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True,}))
    class Meta:
        model = UserCloses
        fields = ['username', 'email','phone_no','password1', 'password2','user_type']
        widgets = { 
            'username': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Enter username ', 'required': True, } ),
            'user_type':forms.Select( attrs={ 'class': 'form-control', 'required': True, } ),
            'password1':forms.PasswordInput(attrs={'class': 'form-control', 'required': True,})
            
               
                }

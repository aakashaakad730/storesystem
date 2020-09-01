
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProductModel


class UserForm(UserCreationForm):
    password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=['username','first_name','last_name','email']


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'cost_price':forms.NumberInput(attrs={'class':'form-control'}),
            'MRP':forms.NumberInput(attrs={'class':'form-control'}),
            
        }
        
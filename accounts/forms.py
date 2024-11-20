from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomerUser
    fields = ['username', 'email', 'password1', 'password2', 'bio', 'avatar', 'phone']

class CustormUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomerUser
    fields = ['username', 'email', 'bio', 'avatar', 'phone']
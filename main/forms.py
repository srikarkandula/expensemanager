from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('name','amount','reason','important','month')
        widgets = {'month':forms.DateInput()}

class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username','email','password1','password2']

class NewIncomeForm(forms.ModelForm):
    class Meta:
        model = Incomes
        fields = ('name','amount','reason','important','month')
        widgets = {'month':forms.DateInput()}



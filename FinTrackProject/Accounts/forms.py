from django import forms
from .models import Profile
from Main.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class AddBankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount 
        fields = ('name', 'currency',)
    
class AddCreditCardForm(forms.ModelForm):
    class Meta: 
        model = CreditCard
        fields = ('name', 'spending_limit', 'due_day')


class AddIncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory 
        fields = ('name',)


class AddIncomeSourceForm(forms.ModelForm):
    class Meta: 
        model = IncomeSource
        fields = ('name', 'category')


class AddIncomingPaymentForm(forms.ModelForm):
    class Meta: 
        model = IncomingPayment
        fields = ('description', 'amount', 'date_time', 'income_source', 'bank_account')


class AddSpendCategoryForm(forms.ModelForm):
    class Meta: 
        model = SpendCategory
        fields = ('name', 'monthly_budget')


class AddMerchantForm(forms.ModelForm):
    class Meta: 
        model = Merchant 
        fields = ('name',)
    

class AddOutgoingPaymentForm(forms.ModelForm):
    class Meta: 
        model = OutgoingPayment
        fields = ('description', 'amount', 'date_time', 'spend_category', 'bank_account', 'credit_card', 'merchant')

class AddNewBankBalanceForm(forms.ModelForm):
    class Meta:
        model = IncomingPayment
        fields = ('amount',)
        labels = {
            'amount':'Current Balance',
        }

class AddNewCreditBalanceForm(forms.ModelForm):
    class Meta:
        model = OutgoingPayment
        fields = ('amount',)
        labels = {
            'amount':'Current Balance Due',
        }
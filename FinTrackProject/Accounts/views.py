from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import *
from .models import Profile
from Main.models import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money
# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Profile successfully created")
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        return render(request, 'registration/signup.html', {'form': form})



def profile(request):
    if request.method == 'POST':
        form1 = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        form2 = EditUserForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('profile')
    else:
        form1 = EditProfileForm(instance=request.user.profile)
        form2 = EditUserForm(instance=request.user)


    total_dollars = 0
    total_shekels = 0
    for account in request.user.profile.bank_accounts.all():
        if account.balance_currency != 'USD':
            converted = convert_money(account.balance, 'USD')
            total_dollars += converted
        
        else:
            total_dollars += account.balance
    
    for account in request.user.profile.bank_accounts.all():
        if account.balance_currency != 'ILS':
            converted = convert_money(account.balance, 'ILS')
            total_shekels += converted
        
        else:
            total_shekels += account.balance

    total_due_dollars = 0
    total_due_shekels = 0
    for card in request.user.profile.credit_cards.all():
        if card.balance_due_currency != 'USD':
            converted = convert_money(card.balance_due, 'USD')
            total_due_dollars += converted
        
        else:
            total_due_dollars += card.balance_due
    
    for card in request.user.profile.credit_cards.all():
        if card.balance_due_currency != 'ILS':
            converted = convert_money(card.balance_due, 'ILS')
            total_due_shekels += converted
        
        else:
            total_due_shekels += card.balance_due

    total_limit_dollars = 0
    total_limit_shekels = 0
    for card in request.user.profile.credit_cards.all():
        if card.spending_limit_currency != 'USD':
            converted = convert_money(card.spending_limit, 'USD')
            total_limit_dollars += converted
        
        else:
            total_limit_dollars += card.spending_limit
    
    for card in request.user.profile.credit_cards.all():
        if card.spending_limit_currency != 'ILS':
            converted = convert_money(card.spending_limit, 'ILS')
            total_limit_shekels += converted
        
        else:
            total_limit_shekels += card.spending_limit

          
    content = {
        'form1': form1, 
        'form2': form2, 
        'total_dollars': total_dollars,
        'total_shekels': total_shekels,
        'total_due_dollars': total_due_dollars,
        'total_due_shekels': total_due_shekels,
        'total_limit_dollars': total_limit_dollars,
        'total_limit_shekels': total_limit_shekels
        }
    return render(request, 'profile.html', content)








def addBankAccount(request):
    if request.method == 'POST':
        form = AddBankAccountForm(request.POST)
        if form.is_valid():
            new_bank = form.save(commit=False)
            new_bank.profile = request.user.profile
            new_bank.save()
            messages.success(request, "Bank Account Added")
            return redirect('profile')

    else:
        form = AddBankAccountForm()
        return render(request, 'add_form.html', {'form': form, 'title':'Bank Account'})

def addCreditCard(request):
    form = AddCreditCardForm()
    if request.method == 'POST':
        form = AddCreditCardForm(request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.profile = request.user.profile
            new_card.save()
            messages.success(request, "Credit Card Added")
            return redirect('profile')

    else:
        
        return render(request, 'add_form.html', {'form': form, 'title': 'Credit Card'})


def addIncomeCategory(request):
    form = AddIncomeCategoryForm()
    if request.method == 'POST':
        form = AddIncomeCategoryForm(request.POST)
        if form.is_valid():
            new_income_category = form.save(commit=False)
            new_income_category.profile = request.user.profile
            new_income_category.save()
            messages.success(request, "Income Category Added")
            return redirect('profile')
        
    else:
        
        return render(request, 'add_form.html', {'form': form, 'title': 'Income Category'})









def addMerchant(request):
    form = AddMerchantForm()
    if request.method == 'POST':
        form = AddMerchantForm(request.POST)
        if form.is_valid():
            new_merchant = form.save(commit=False)
            new_merchant.profile = request.user.profile
            new_merchant.save()
            messages.success(request, "Merchant Added")
            return redirect('profile')
       
    else:
        return render(request, 'add_form.html', {'form': form, 'title': 'Merchant'})
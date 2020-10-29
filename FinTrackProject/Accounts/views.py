from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from datetime import datetime
from .forms import *
from .models import Profile
from Main.models import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money
import plotly.graph_objects as go
from plotly.offline import plot

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


    # total_dollars = 0
    # total_shekels = 0
    # for account in request.user.profile.bank_accounts.all():
    #     if account.balance_currency != 'USD':
    #         converted = convert_money(account.balance, 'USD')
    #         total_dollars += converted
        
    #     else:
    #         total_dollars += account.balance
    
    # for account in request.user.profile.bank_accounts.all():
    #     if account.balance_currency != 'ILS':
    #         converted = convert_money(account.balance, 'ILS')
    #         total_shekels += converted
        
    #     else:
    #         total_shekels += account.balance

    # total_due_dollars = 0
    # total_due_shekels = 0
    # for card in request.user.profile.credit_cards.all():
    #     if card.balance_due_currency != 'USD':
    #         converted = convert_money(card.balance_due, 'USD')
    #         total_due_dollars += converted
        
    #     else:
    #         total_due_dollars += card.balance_due
    
    # for card in request.user.profile.credit_cards.all():
    #     if card.balance_due_currency != 'ILS':
    #         converted = convert_money(card.balance_due, 'ILS')
    #         total_due_shekels += converted
        
    #     else:
    #         total_due_shekels += card.balance_due

    # total_limit_dollars = 0
    # total_limit_shekels = 0
    # for card in request.user.profile.credit_cards.all():
    #     if card.spending_limit_currency != 'USD':
    #         converted = convert_money(card.spending_limit, 'USD')
    #         total_limit_dollars += converted
        
    #     else:
    #         total_limit_dollars += card.spending_limit
    
    # for card in request.user.profile.credit_cards.all():
    #     if card.spending_limit_currency != 'ILS':
    #         converted = convert_money(card.spending_limit, 'ILS')
    #         total_limit_shekels += converted
        
    #     else:
    #         total_limit_shekels += card.spending_limit

    labels = [category.name for category in request.user.profile.month_spending_by_category()]
    values = [category.total_spending for category in request.user.profile.month_spending_by_category()]

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])      
    plt_div = plot(fig, output_type='div', include_plotlyjs=False)
    content = {
        'form1': form1, 
        'form2': form2, 
        'plt_div': plt_div
        # 'total_dollars': total_dollars,
        # 'total_shekels': total_shekels,
        # 'total_due_dollars': total_due_dollars,
        # 'total_due_shekels': total_due_shekels,
        # 'total_limit_dollars': total_limit_dollars,
        # 'total_limit_shekels': total_limit_shekels
        }
    return render(request, 'profile.html', content)








def addBankAccount(request):
    if request.method == 'POST':
        form1 = AddBankAccountForm(request.POST)
        form2 = AddNewBankBalanceForm(request.POST)
        if form1.is_valid():
            new_bank = form1.save(commit=False)
            new_bank.profile = request.user.profile
            new_bank.save()
            messages.success(request, "Bank Account Added")

        if form2.is_valid():
            new_inc_payment = form2.save(commit=False)
            new_inc_payment.profile = request.user.profile
            new_inc_payment.description = "starting bank account balance"
            new_inc_payment.date_time = datetime.now() 
            new_inc_payment.income_source = IncomeSource.objects.get(name='Starting Balance')
            new_inc_payment.income_category = IncomeCategory.objects.get(id=11)
            new_inc_payment.bank_account = new_bank
            new_inc_payment.save()
            
            return redirect('profile')

    else:
        form1 = AddBankAccountForm()
        form2 = AddNewBankBalanceForm()
        return render(request, 'add_2_forms.html', {'form1': form1, 'form2': form2, 'title':'Bank Account'})

def addCreditCard(request):
    form1 = AddCreditCardForm()
    form2 = AddNewCreditBalanceForm()
    if request.method == 'POST':
        form1 = AddCreditCardForm(request.POST)
        form2 = AddNewCreditBalanceForm(request.POST)
        if form1.is_valid():
            new_card = form1.save(commit=False)
            new_card.profile = request.user.profile
            new_card.save()
            messages.success(request, "Credit Card Added")

        if form2.is_valid():
            new_out_payment = form2.save(commit=False)
            new_out_payment.profile = request.user.profile
            new_out_payment.description = "starting credit card balance due"
            new_out_payment.date_time = datetime.now() 
            new_out_payment.credit_card = new_card
            new_out_payment.save()    
            
            return redirect('profile')

    else:
        
        return render(request, 'add_2_forms.html', {'form1': form1, 'form2': form2, 'title':'Credit Card'})


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

def addIncomeSource(request):
    form = AddIncomeSourceForm()
    if request.method == 'POST':
        form = AddIncomeSourceForm(request.POST)
        if form.is_valid():
            new_income_source = form.save(commit=False)
            new_income_source.profile = request.user.profile
            new_income_source.save()
            messages.success(request, "Income Source Added")
            return redirect('profile')
        
    else:
        
        return render(request, 'add_form.html', {'form': form, 'title': 'Income Source'})



def addSpendingCategory(request):
    form = AddSpendCategoryForm()
    if request.method == 'POST':
        form = AddSpendCategoryForm(request.POST)
        if form.is_valid():
            new_spending_category = form.save(commit=False)
            new_spending_category.profile = request.user.profile
            new_spending_category.save()
            messages.success(request, "Spending category added")
            return redirect('profile')
       
    else:
        return render(request, 'add_form.html', {'form': form, 'title': 'Spending Category'})




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


def addIncomingPayment(request):
    form = AddIncomingPaymentForm()
    form.fields['bank_account'].queryset = BankAccount.objects.filter(profile=request.user.profile)
    if request.method == 'POST':
        form = AddIncomingPaymentForm(request.POST)
        if form.is_valid():
            new_inc_pmnt = form.save(commit=False)
            new_inc_pmnt.profile = request.user.profile
            new_inc_pmnt.save()
            messages.success(request, "Incoming Payment Added")
            return redirect('profile')
       
    else:
        return render(request, 'add_form.html', {'form': form, 'title': 'Incoming Payment'})


def addOutgoingPayment(request):
    form = AddOutgoingPaymentForm()
    form.fields['bank_account'].queryset = request.user.profile.bank_accounts.all()
    form.fields['credit_card'].queryset = request.user.profile.credit_cards.all()
    
    if request.method == 'POST':
        form = AddOutgoingPaymentForm(request.POST)
        if form.is_valid():
            new_inc_pmnt = form.save(commit=False)
            new_inc_pmnt.profile = request.user.profile
            new_inc_pmnt.save()
            messages.success(request, "Outgoing Payment Added")
            return redirect('profile')
       
    else:
        return render(request, 'add_form.html', {'form': form, 'title': 'Outgoing Payment'})
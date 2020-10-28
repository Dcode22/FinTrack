from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Accounts.models import Profile
from djmoney.models.fields import MoneyField
from djmoney.money import Money

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)
    # value??
    profile_favorites = models.ManyToManyField(Profile)
    # profile_primary = models.ManyToOneRel(Profile)
    def __str__(self):
        return f"{self.name} - ({self.long_name})"


class BankAccount(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='bank_accounts')
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    # balance = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    def __str__(self):
        return f"{self.name}"

class CreditCard(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='credit_cards')
    name = models.CharField(max_length=50)
    # balance_due = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    spending_limit = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    due_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(28)])
    def __str__(self):
        return f"{self.name}"
class IncomeCategory(models.Model):
    name = models.CharField(max_length=50)
    profiles = models.ManyToManyField(Profile, related_name='income_categories', blank=True)
    def __str__(self):
        return f"{self.name}"
class IncomeSource(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='income_sources')
    name = models.CharField(max_length=50)
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True, related_name='income_sources')
    def __str__(self):
        return f"{self.name}"
class Payment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description =  models.CharField(max_length=200, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    date_time = models.DateTimeField()
    # currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    class Meta:
        abstract = True 

class IncomingPayment(Payment):
    income_source = models.ForeignKey(IncomeSource, on_delete=models.PROTECT, related_name='income_payments')
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='income_payments')
    

# class Recurrence(models.Model):
#     incoming_payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
#     is_active = models.BooleanField(default=True)


class SpendCategory(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='spending_categories')
    monthly_budget = MoneyField(max_digits=10, decimal_places=2, null=True, blank=True, default_currency='USD')
    def __str__(self):
        return self.name
class Merchant(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='merchants')
    spend_category = models.ForeignKey(SpendCategory, on_delete=models.PROTECT, related_name='merchants', null=True)
    def __str__(self):
        return self.name

class OutgoingPayment(Payment):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.PROTECT, null=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, null=True)
    spend_category = models.ForeignKey(SpendCategory, on_delete=models.PROTECT, related_name='outgoing_payments', null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT)

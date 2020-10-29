from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import *
from django.db.models import Sum



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/avatar.png", upload_to="profile_pics")
    def __str__(self):
        return f"{self.user.get_full_name()}"

    
    def month_outgoing_payments(self, date=datetime.now()):
        return self.outgoing_payments.filter(date_time__month=date.month, date_time__year=date.year)
         
    
    def month_spending_by_category(self):
        
        return self.spending_categories.annotate(total_spending=Sum("outgoing_payments__amount_dollars"))
    

@receiver(post_save, sender=User)
def createProfile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
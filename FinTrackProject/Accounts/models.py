from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/avatar.png", upload_to="profile_pics")
    def __str__(self):
        return f"{self.user.get_full_name()}"
@receiver(post_save, sender=User)
def createProfile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
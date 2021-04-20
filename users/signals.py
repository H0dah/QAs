from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        print("profile", instance.username, "created")
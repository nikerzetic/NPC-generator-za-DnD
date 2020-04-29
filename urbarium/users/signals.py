# A signal that fires when an abject is saved
# (that signal will be when the user is created)
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a User is created, the sender (User) sends a signal (post_save)
# reciever (create_profile) recieves the signal
# post_save sends instance and created arguments
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kvargs):
    # if the user is created than create a profile for this user
    if created:
        Profile.objects.create(user=instance)


# We have to save the profile that we created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kvargs):
    instance.profile.save()

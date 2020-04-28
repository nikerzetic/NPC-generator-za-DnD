from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # This model has a one to one reltionship with the User model
    # One User has one Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
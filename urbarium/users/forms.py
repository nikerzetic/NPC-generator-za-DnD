from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# A form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Fields that we want to add to UserCreationForm:
    email = forms.EmailField()

    # This class gives us a space for configurations for a specific model
    class Meta:
        # the model that will be affected:
        # when we do form.save() it will be saved into this User model
        model = User
        # fields that we want in the form
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

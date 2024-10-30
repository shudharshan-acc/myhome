from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from .models import CustomUser
# # from.models import users

class UserRegisterationForm(UserCreationForm):
    class meta:
        model = User
        fields = '__all__'

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("mobile","address")
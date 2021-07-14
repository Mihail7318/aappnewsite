from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userprofile.models import CustomUser, CustomUseris

class CustomUserCreationForm(UserCreationForm):

    class MPTTMeta:
        order_insertion_by = ['region']

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name')


class CustomUserisCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUseris
        fields = ('username', 'email', 'first_name')

class CustomUserisChangeForm(UserChangeForm):

    class Meta:
        model = CustomUseris
        fields = ('username', 'email', 'first_name')
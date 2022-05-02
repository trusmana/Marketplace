from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from .models import AccountsUser,Profile


###Menu Form Admin
class AccountUserCreationForm(UserCreationForm):
    class Meta:
        model = AccountsUser
        fields = ('email',)

class AccountUserChangeForm(UserChangeForm):
    class Meta:
        model = AccountsUser
        fields = ('email',)
###Menu Form Admin

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField()

    class Meta:
        model = AccountsUser
        fields = ['username','email', 'password1', 'password2']

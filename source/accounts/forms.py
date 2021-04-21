from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UsernameField

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not first_name and not last_name:
            raise forms.ValidationError('Please fill in these fields')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    #dont add fields here
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    #dont add fields here
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length = 100)


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

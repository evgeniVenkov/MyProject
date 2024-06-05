from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(UserCreationForm):
    username = forms.CharField(
        label='UserName',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), )


    class Meta:
        model = User
        fields = ['email','username', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='UserName',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    class Meta:
        model = User
        fields = ['username','email']



class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Фото',
        required=False,
        widget= forms.FileInput
    )
    class Meta:
        model = Profile
        fields = ['img']
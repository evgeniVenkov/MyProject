from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class profileForm(forms.ModelForm):
    username = forms.CharField(
        label= "Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label="Емайл",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Емайл"}),
    )
    class Meta:
        model = User
        fields = ['username', 'email']

class UserForm(UserCreationForm):
    username = forms.CharField(
        label="Имя Пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя Пользователя'}),
    )
    email = forms.EmailField(
        label='Емайл',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Емайл'}),

    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label="Повторный пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
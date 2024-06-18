from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import links

class profileForm(forms.ModelForm):
    username = forms.CharField(
        label= "Имя пользователя",
        widget=forms.TextInput()
    )

    email = forms.EmailField(
        label="Емайл",
        widget=forms.TextInput(),
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

    def __init__(self, *args, **kargs):
        super(UserForm, self).__init__(*args, **kargs)
        del self.fields['password2']

class linksForm(forms.ModelForm):
    slug = forms.SlugField(label="Длинная ссылка",max_length=100)
    link = forms.CharField(label="Короткая ссылка",max_length=250)
    class Meta:
        model = links
        fields = ['slug', 'link', 'user']
        widgets = {'user': forms.HiddenInput()}
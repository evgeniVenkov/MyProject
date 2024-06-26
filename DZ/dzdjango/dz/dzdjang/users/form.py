from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Posts,Pochta



class UserForm(UserCreationForm):
    username = forms.CharField(
        label = "Имя Пользователя",
        widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Имя Пользователя'}),
    )
    email = forms.EmailField(
        label='Емайл',
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Емайл'}),

    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs= {'class': 'form-control','placeholder':'Пароль'})
    )
    password2 = forms.CharField(
        label="Повторный пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя Пользователя",
        widget= forms.TextInput( attrs= {'class':'form-control', 'placeholder': "Имя Пользователя"}),
    )

    email = forms.EmailField(
        label= "Емайл",
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Емайл"}),

    )
    class Meta:
        model = User
        fields = ['username','email']
class ProfileForm(forms.ModelForm):
    img = forms.ImageField(
        label= "Фото Пользователя",
        required=False,
        widget= forms.FileInput

    )
    soglasie = forms.BooleanField(
        label="Согласие на отпарвку уведомлений на почту"
    )
    pol = forms.ChoiceField(
        choices= (('male','Мужской'),('female','Женский')),
        label= "Выбирите пол"
    )
    class Meta:
        model = Profile
        fields = ['img', 'soglasie','pol']
class PostsForm(forms.ModelForm):

    title = forms.CharField(
        label="Название статьи"
    )
    content = forms.CharField(
        label='Статья'
    )
    date = forms.DateField(
        label='Дата создания'
    )
    Avtor= forms.CharField(
        label="Автор"
    )
    class Meta:
        model = Posts
        fields = ['title','content','date','Avtor']
class PochtaForm(forms.ModelForm):
    tema = forms.CharField(label='Тема письма')
    mail = forms.CharField(label="Почта отправителя")
    text = forms.CharField(label="Текст сообщения")
    class Meta:
        model = Pochta
        fields = ['tema','mail','text']
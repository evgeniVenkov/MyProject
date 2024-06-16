from django import forms
from .models import Course, Comment, Lesson


class CourseForm(forms.ModelForm):
    slug = forms.SlugField(label='Уникальное название',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Название курса',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(label='Описание курса',
                           widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Картинка',
                             required=False,
                             widget= forms.FileInput,)

    class Meta:
        model = Course
        fields = ['slug', 'title', 'desc', 'image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'user', 'lesson']

        widgets = {'user': forms.HiddenInput(),'lesson': forms.HiddenInput(), 'text': forms.Textarea(attrs={ 'placeholder':'текст коментария'}) }
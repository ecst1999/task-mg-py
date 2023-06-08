
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Task, Note

PRIORITY_CHOICES = [
    ('high', 'High'),
    ('low', 'Low'),
    ('medium', 'Medium')
]


# - Registera a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content', 'location', 'deadline', 'icon', 'priority', 'files', 'category', 'status']
        exclude = ['user',]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }, choices=PRIORITY_CHOICES),
            'files': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags', 'comment', 'files',]
        exclude = ['user',]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'files': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
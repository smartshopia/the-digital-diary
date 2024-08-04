from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tinymce.widgets import TinyMCE
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'short_description']
  
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
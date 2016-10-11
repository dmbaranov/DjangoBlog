from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    #text = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Comment
        exclude = ['post', 'author']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'author']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


class UploadImage(forms.Form):
    file = forms.FileField(label='Select an avatar')
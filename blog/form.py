from django import forms
from .models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'author']


class NewPostForm(forms.ModelForm):
    OPTIONS = tuple(Tag.objects.all().values_list('title'))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Post
        exclude = ['author']


class UploadImage(forms.Form):
    file = forms.FileField(label='Select an avatar')
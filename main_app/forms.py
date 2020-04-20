from django import forms
from .models import Post, comments


class PostCreator(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'picture', 'picture_2')


class CommentForm(forms.ModelForm):
    guild = forms.CharField(
        max_length=50,
        widget=forms.TextInput({'placeholder': '#guild_name::nickname'}),
        required=True)

    class Meta:
        model = comments
        fields = ('guild', 'content')

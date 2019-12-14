from django import forms
from django.contrib.auth.models import User

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    # photo = forms.ImageField(label='Photo', required=True)
    # description = forms.CharField(max_length=200, label='Description',  required=True, widget=forms.Textarea)

    class Meta:
        model = Photo
        exclude = ['created_at', 'author', 'likes', 'like_users']

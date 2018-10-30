from django import forms
from django.views.generic.edit import UpdateView
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body']

class UpdateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body']
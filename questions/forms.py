from django import forms
from django.db import models
class QuestionForm(forms.ModelForm):
    question = forms.CharField(max_length=300,widget=
            forms.Textarea())
    answer = forms.CharField(max_length=50,widget=
            forms.Textarea())

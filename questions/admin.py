from django.contrib import admin
from questions.models import *
from questions.forms import QuestionForm
from django import forms

class QuestionsAdmin(admin.ModelAdmin):
    form = QuestionForm
admin.site.register(Questions,QuestionsAdmin)

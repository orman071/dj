# -*- coding: utf-8 -*-

from django import forms
from qa.models import Question, Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
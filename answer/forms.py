from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm) : 
    class Meta:
        model = Answer
        fields = ['title','body','image']

# 미디어 변경 부분(form)
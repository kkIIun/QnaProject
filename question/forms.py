from django import forms
from .models import Question 

class QuestionForm(forms.ModelForm) : 
    class Meta:
        model = Question
        fields = ['title','body','professor_name','subject_name','image']


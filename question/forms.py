from django import forms
from .models import Question 

class QuestionForm(forms.ModelForm) : 
    class Meta:
        model = Question
        fields = ['title','body','image','professor_name','subject_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': "질문 제목을 입력해주세요"}),
            'body': forms.Textarea(attrs={'class': 'form-control ','placeholder':"궁금한 내용을 질문해 주세요."}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'professor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        # 'form-control my-5 p-5'
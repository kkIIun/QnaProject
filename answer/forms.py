from django import forms
from .models import Answer 

class AnswerForm(forms.ModelForm) : 
    class Meta:
        model = Answer
        fields = ['title','body','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': "답변 제목을 입력해주세요"}),
            'body': forms.Textarea(attrs={'class': 'form-control ','placeholder':"답변해주세요!"}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}), 
        }


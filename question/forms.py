from django import forms
from .models import Question 

class QuestionForm(forms.ModelForm) : 
    class Meta:
        model = Question
        fields = ['title','body','image','professor_name','subject_name']

        # def __init__( self, *args, **kwargs ):
        # super( MyForm, self ).__init__( *args, **kwargs )
        # self.field[ 'my_field' ].widget.attrs.update( {
        #     'class': 'form-control',
        #     'id': 'form-id',
        #     'placeholder': 'Do not use numbers.' } )
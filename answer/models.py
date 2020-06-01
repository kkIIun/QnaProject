from django.db import models
from account.models import CustomUserModel
# Create your models here.
from django.db import models
from question.models import *
# Create your models here.

class Answer(models.Model): 
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="answer/", blank=True, null=True) # 이미지 받는 필드  # media/answer/파일이름 -> 이렇게 저장 된다
    
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    selected = models.BooleanField(null=False, default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
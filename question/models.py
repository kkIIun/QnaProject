from django.db import models
from account.models import CustomUserModel


# from ..answer.models import Answer

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="question/", blank=True, null=True) # 이미지 받는 필드  # media/blog/파일이름 -> 이렇게 저장 된다
    professor_name = models.CharField(max_length=200,null=True)
    subject_name = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

    # answer = models.ForeignKey(Answer, on_delete= models.CASCADE)
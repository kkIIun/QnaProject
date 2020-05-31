from django.db import models

# from ..answer.models import Answer

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

    image = models.ImageField(upload_to="answer/", blank=True, null=True)   # 미디어 변경 부분(form)

    professor_name = models.CharField(max_length=200,null=True)
    subject_name = models.CharField(max_length=200,null=True)
    # answer = models.ForeignKey(Answer, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
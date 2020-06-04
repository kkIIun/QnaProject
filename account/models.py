from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER = (
        ('M','남자'),
        ('W','여자'),
    )
    
    birthday = models.DateField(blank = True, null = True) # 둘다 True인 경우 -> 로그인에 상관이 없는 경우
    gender = models.CharField(max_length=2,blank = True, null = True,choices=GENDER)
    point = models.IntegerField(null = True,default=0)
    grade = models.IntegerField(null = True,default=0)
    last_signed_at = models.DateField(blank = True, null = True)

    def get_grade(self):
        if  self.grade < 10 : return 'Bronze'
        elif self.grade < 100 : return 'Silver'
        elif self.grade < 1000 : return 'Gold'
        elif self.grade < 10000 : return 'Platinum'
        elif self.grade < 100000 : return 'Diamond'
        elif self.grade < 1000000 : return 'Challenger'

    def get_img(self):
        if  self.grade < 10 : return 'static/image/브론즈.png'
        elif self.grade < 100 : return 'static/image/실버.png'
        elif self.grade < 1000 : return 'static/image/골드.png'
        elif self.grade < 10000 : return 'static/image/플레티넘.png'
        elif self.grade < 100000 : return 'static/image/다이아.png'
        elif self.grade < 1000000 : return 'static/image/챌린져.png'



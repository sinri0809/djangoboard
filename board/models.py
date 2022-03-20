from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    # User모델을 ForeignKey로 적용,
    # on_delete= 삭제 조건. author이 삭제되면, Question 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # 수정을 한다면, 수정날짜를 데이터에 포함.
    modify_date = models.DateTimeField(null=True, blank=True)
    

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # on_delete= 모델 삭제 조건, question이 삭제되면 Answer 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    modify_date = models.DateTimeField(null=True, blank=True)

    

from django.contrib import admin
from .models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin): # 관리자 페이지, question 객체에 검색기능을 추가할 수 있다.
    search_fields = ['subject']


admin.site.register(Question)

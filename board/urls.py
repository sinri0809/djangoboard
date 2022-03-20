from django.urls import path
from board import views


app_name = 'board' # appname을 지정해주면 동일한 name속성에도 구분할 수 있다.

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    # question Create Update Delete
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>', views.question_delete, name='question_delete'),
    # answer Create Update Delete
    path('answer/create/<int:answer_id>/', views.answer_create, name="answer_create"),
    # path('answer/modify/<int:answer_id>/', views.answer_modify, name="answer_modify"),
    # path('answer/delete/<int:answer_id>/', views.answer_delete, name="answer_delete"),
]

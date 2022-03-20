from django import forms
from board.models import Question, Answer # model이랑 연결


class QuestionForm(forms.ModelForm): # froms.ModelForm을 상속했다.
    class Meta: # 필수 inner 클래스
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        # 추가 설정 - tag와 class, 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'from-control', 'rows': 10})
        # }
        # 추가 설정  label
        labels = {
            'subject': '질문 제목',
            'content': '질문 내용'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용'
        }

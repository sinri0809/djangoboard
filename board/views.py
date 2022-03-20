from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from itertools import islice
from math import ceil


# Create your views here.
def index(request):
    """
    board 목록 출력
    :param request:
    :return:
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date') # -가 붙어있으면 역방향이다.
    # question_list = get_object_or_404(Question).order_by('-create_date')
    question_count = question_list.count
    
    paginator = Paginator(question_list, 10) # 페이지당 10개 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
        'question_list': page_obj,
        'question_count': question_count
    }
    return render(request, 'board/question_list.html', context)


def temp_pagination(question_count, question_list):
    # pagination
    total_page = ceil(question_count / 5)
    cur_page = 1
    cur_list = islice(question_list, (cur_page-1)*5 + 1, cur_page*5)


def detail(request, question_id):
    """
    baord 질문 내용 출력
    :param request:
    :param id:
    :return:
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) # 404 에러로 핸들링하기
    context = {
        'question': question
    }
    
    return render(request, 'board/question_detail.html', context)
    # return HttpResponse(f'board/{id} 페이지입니다.')


@login_required(login_url='user:login')
def answer_create(request, question_id):
    """
    board 질문의 답변 생성
    @login_required: answer model에 author는 auth.model의 User을 참조한다.
    
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    
    # 1. answer_set 이용하기
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    
    # 2. Answer class(model) 이용하기
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    
    # 3. form API 이용하기
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)


@login_required(login_url='user:login')
def question_create(request):
    """
    Question 질문 등록
    :param request:
    :param question_id:
    :return:
    """
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # request.POST에는 form태그에서 작성한 속성과 값이 자동으로 저장되어 객체가 생성된다.

        if form.is_valid(): # form이 유효한지 확인한다.
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
        
    else: # 초기에 a링크로 질문하기를 클릭하면 GET방식으로 페이지에 들어오기때문에
        # GET request를 대비한 코드를 작성해야한다.
        form = QuestionForm()
        
    context = {'form': form}
    
    return render(request, 'board/question_form.html', context)


@login_required(login_url='user:login')
def question_modify(request, question_id):
    """
    질문 수정하기
    :param request:
    :param question_id: Question model의 question_id
    :return: render
    """
    question = get_object_or_404(Question, pk=question_id)
    
    # user가 다를 때는 수정을 못하게 막는다.
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('board:detail', question_id=question.id)
    
    if request.method == "POST":
        # instance= :지정시 form이 instance로 채워진다.
        # 즉, instance로 채우고 request.POST로 다시 덮어쓰는 것임
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('board:detail', question_id=question.id)
        
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'question': question
    }
    
    return render(request, 'board/question_modify.html', context)


@login_required(login_url='user:login')
def question_delete(request, question_id):
    """
    질문 삭제하기
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    
    # 작성자만 삭제 가능
    if request.user != question.author:
        print('삭제 권한 없음')
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect('board:detail', question_id=question_id)
    
    # 삭제
    question.delete()
    
    return redirect('board:index')
    

@login_required(login_url='user:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user != answer.author:
        messages.error(request, '권한이 없습니다')
        return redirect('board:detail', question_id=answer.question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('board:detail', answer.question.id)
        
    else:
        form = AnswerForm()
   
    context = {
        'form': form,
        'answer': answer
    }
    
    # return redirect('board:detail', answer.question.id)
    # return render(request, 'board/question_detail.html', context)
    
    

@login_required(login_url='user:login')
def answer_delete(request, answer_id):
    
    
    return HttpResponse('답글 삭제페이지 입니다')
    


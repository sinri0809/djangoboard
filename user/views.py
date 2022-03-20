from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse('hello user')


def signup(request):
    """
    회원가입, 계정생성 page
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserForm(request.POST) # 입력한 데이터로 사용자 생성
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            # authenticate 사용자 인증
            user = authenticate(username=username, password=raw_password)
            # login 로그인
            login(request, user)
            
            return redirect('board:index')
    
    else: # GET
        form = UserForm() # 계정 생성 화면 렌더링
    
    context = {'form': form}
    return render(request, 'user/signup.html', context)

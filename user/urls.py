from django.urls import path
from .views import index, signup
from django.contrib.auth import views as auth_view


app_name = 'user'

urlpatterns = [
    path('', index, name="index"),
    # path('login/', login, name="login"),
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html"), name="login"), # contrib API에 이미 있는 로그인 창이 있다.
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name="signup")
]

# print(auth_view.LoginView.as_view)

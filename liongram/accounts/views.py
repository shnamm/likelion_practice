from django.shortcuts import render, redirect
from .forms import UserCreateForm, SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    #GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = UserCreateForm
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        #POST 요청 시 데이터 확인 후 회원 생성

        if SignUpForm.is_valid():
            #회원가입 처리
            form = SignUpForm(request.POST)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password2 = form.cleaned_data['password2']
        else:
            return redirect('accounts:signup')

def login_view(request):
    #GET POST 분리
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        #데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비지니스 로직 처리
            login(request, form.user_cache)
            # 응답
            return redirect('index')
            pass
        else:
            return render(request, 'account.login.html', {'form': form})

def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        # 비지니스 로직 처리 - 로그아웃
        logout(request)
    #응답
    return redirect('index')

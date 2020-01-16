from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect

from member.forms import LoginForm, SignupForm

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:post-list')
    else:
        form = LoginForm()

    login_base_url = 'https://nid.naver.com/oauth2.0/authorize'
    login_params = {
        'response_type': 'code',
        'client_id': 'vlffjTerqGRY684xV6_O',
        'redirect_uri': 'http://localhost:8000/members/naver-login/',
        'state': 'RANDOM_STATE',
    }
    login_url = '{base}?{params}'.format(
        base=login_base_url,
        params='&'.join([f'{key}={value}' for key, value in login_params.items()])
    )
    context = {
        'form': form,
        'login_url': login_url,

    }
    return render(request, 'members/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post-list')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('signup')



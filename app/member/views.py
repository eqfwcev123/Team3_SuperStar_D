from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect

from member.forms import LoginForm, SignupForm

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('vote:vote-list')
    else:
        form = LoginForm()

    context = {
        'form': form,

    }
    return render(request, 'member/login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('vote:vote-list')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vote:vote-list')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'member/index.html', context)


def logout_view(request):
    logout(request)
    return redirect('member:login')

from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from member.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사용자 이름',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('username / password가 올바르지 않습니다.')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)


class SignupForm(forms.Form):
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'placeholder': '이메일 주소',
                'class': "form-control",
            }
        )
    )
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': '성명',
                'class': "form-control",
            }
        )
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용자 이름',
                'class': "form-control",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호',
                'class': "form-control",
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('이미 사용 중인 email입니다.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('이미 사용 중인 username입니다.')
        return username

    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            name=self.cleaned_data['name'],
            password=self.cleaned_data['password'],
        )

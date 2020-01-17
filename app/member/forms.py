from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from member.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
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
                'placeholder': '아이디',
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
    team_name = forms.ChoiceField(
        label='팀선택',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }),
        choices=[(1, 'Team1'),
                 (2, 'Team2'),
                 (3, 'Team3'),
                 (4, 'Team4'),
                 (5, 'Team5'),
                 (6, 'Staff'), ]
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('이미 사용 중인 username입니다.')
        return username

    def clean_name(self):
        name = self.cleaned_data['name']
        for team in settings.FASTCAMPUS:
            print(team)
            if name in team:
                if User.objects.filter(name=name).exists():
                    raise ValidationError('이미 가입된 이름입니다')
                return name
        raise ValidationError('사용할수 없는 이름입니다. 실명으로 다시 입력해 주세요')

    def save(self):
        return User.objects.create_user(
            team_name=self.cleaned_data['team_name'],
            username=self.cleaned_data['username'],
            name=self.cleaned_data['name'],
            password=self.cleaned_data['password'],
        )

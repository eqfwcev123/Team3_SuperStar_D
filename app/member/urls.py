from django.urls import path

from member.views import login_view, logout_view

app_name = 'member'
urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]

from django.urls import path

from vote.views import vote_list_view, vote_detail_view

app_name = 'vote'
urlpatterns = [
    path('list/', vote_list_view, name='vote-list'),
    path('detail/<int:pk>/', vote_detail_view, name="vote-detail")
]

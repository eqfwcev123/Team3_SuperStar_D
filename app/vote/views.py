from django.shortcuts import render

# Create your views here.
from vote.models import Team


def vote_list_view(request):
    team = Team.objects.exclude(name="Staff")
    context = {
        'team_list': team
    }
    return render(request, 'vote/vote_list.html', context)


def vote_detail_view(request, pk):
    if request.method == 'POST':
        pass
    else:
        context = {
            'pk': pk - 1,
        }
        return render(request, 'vote/vote_detail.html',context)

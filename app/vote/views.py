from django.shortcuts import render, redirect

# Create your views here.
from vote.forms import QuestionForm
from vote.models import Team


def vote_list_view(request):
    team = Team.objects.exclude(name="스탶")
    context = {
        'team_list': team
    }
    return render(request, 'vote/vote_list.html', context)


def vote_detail_view(request, pk):
    if request.method == 'POST':
        user = request.user
        need = request.POST['need']
        fresh = request.POST['fresh']
        interest = request.POST['interest']
        complete = request.POST['complete']
        team = Team.objects.get(pk=pk)
        team.relation_set.create(user=user, need=need, fresh=fresh, interest=interest, complete=complete)
        return redirect('vote:vote-list')
    else:
        question_form = QuestionForm()
    context = {
        'pk': pk,
        'form': question_form,
    }
    return render(request, 'vote/vote_detail.html', context)


def stat(request):
    # filter(relation__fresh__isnull=False)
    total = 0

    for team in Team.objects.exclude(pk=6):
        for index, item in enumerate(team.relation_set.values('fresh','team_id')):
            print(index, item['fresh'], item['team_id'])
            # print(f'팀{i}fresh 는 {item["fresh"]}')
            # total += item['fresh']


    # context = {
    #     'team_list': team_list
    # }
    return render(request, 'vote/stat.html')

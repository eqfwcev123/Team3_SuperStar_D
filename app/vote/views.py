from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.
from vote.forms import QuestionForm
from vote.models import Team, Relation


def vote_list_view(request):
    team = Team.objects.exclude(pk=6).exclude(pk=request.user.team_name)
    num_list = []
    for tmp in team:
        for item in tmp.relation_set.values():
            if item['user_id'] == request.user.pk:
                num_list.append(item['team_id'])
    num_list = list(set(num_list))

    for num in num_list:
        team = team.exclude(pk=num)
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
    teams = Team.objects.exclude(pk=6)
    score_list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    fname = ['참신함', '완성도', '흥미도', '필요성', '평균']
    for team in Team.objects.exclude(pk=6):
        index = 0
        for index, item in enumerate(team.relation_set.values()):
            score_list[item['team_id']][0] += item['fresh']
            score_list[item['team_id']][1] += item['complete']
            score_list[item['team_id']][2] += item['interest']
            score_list[item['team_id']][3] += item['need']
        count = index + 1
        score_list[item['team_id']][0] = round((score_list[item['team_id']][0] / count), 2)
        score_list[item['team_id']][1] = round((score_list[item['team_id']][1] / count), 2)
        score_list[item['team_id']][2] = round((score_list[item['team_id']][2] / count), 2)
        score_list[item['team_id']][3] = round((score_list[item['team_id']][3] / count), 2)
        score_list[item['team_id']][4] = round(((score_list[item['team_id']][0] + score_list[item['team_id']][1] +
                                                 score_list[item['team_id']][2] + score_list[item['team_id']][3]) / 4),
                                               2)
        score_list[0][item['team_id'] - 1] = count

    context = {
        't1_f': score_list[1][0], 't1_c': score_list[1][1], 't1_i': score_list[1][2], 't1_n': score_list[1][3],
        't1_t': score_list[1][4], 't1_cnt': score_list[0][0],
        't2_f': score_list[2][0], 't2_c': score_list[2][1], 't2_i': score_list[2][2], 't2_n': score_list[2][3],
        't2_t': score_list[2][4], 't2_cnt': score_list[0][1],
        't3_f': score_list[3][0], 't3_c': score_list[3][1], 't3_i': score_list[3][2], 't3_n': score_list[3][3],
        't3_t': score_list[3][4], 't3_cnt': score_list[0][2],

        't4_f': score_list[4][0], 't4_c': score_list[4][1], 't4_i': score_list[4][2], 't4_n': score_list[4][3],
        't4_t': score_list[4][4], 't4_cnt': score_list[0][3],

        't5_f': score_list[5][0], 't5_c': score_list[5][1], 't5_i': score_list[5][2], 't5_n': score_list[5][3],
        't5_t': score_list[5][4], 't5_cnt': score_list[0][4],
    }
    return render(request, 'vote/stat.html', context)


def logout_view(request):
    logout(request)
    return redirect('member:login')
from django.db import models

from member.models import User


class Team(models.Model):
    name = models.CharField('팀 이름', max_length=30)
    user = models.ManyToManyField(User, through='Relation')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Relation(models.Model):
    SCORE_CHOICES = [
        (0, '0점'),
        (1, '1점'),
        (2, '2점'),
        (3, '3점'),
        (4, '4점'),
        (5, '5점'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    fresh = models.IntegerField(choices=SCORE_CHOICES)
    complete = models.IntegerField(choices=SCORE_CHOICES)
    interest = models.IntegerField(choices=SCORE_CHOICES)
    need = models.IntegerField(choices=SCORE_CHOICES)

    def __str__(self):
        return f'{self.team}, {self.user}'

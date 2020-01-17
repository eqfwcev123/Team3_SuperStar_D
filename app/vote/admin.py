from django.contrib import admin

# Register your models here.
from vote.models import Relation, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('team', 'user')
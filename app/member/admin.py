from django.contrib import admin

from member.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_name')
    list_display_links = ('name', 'team_name')

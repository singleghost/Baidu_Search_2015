from django.contrib import admin
from register.models import *

class TeamAdmin(admin.ModelAdmin):
    ordering = ('-score','time',)

class Team_memberAdmin(admin.ModelAdmin):
    list_display = ('name','sex','phone_number','phone_number_short','team')
    filter_horizontal =('Team',)

admin.site.register(Team)
admin.site.register(Team_member)

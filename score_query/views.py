from django.shortcuts import render_to_response
from register.models import Team

def query(request):
    team_list = Team.objects.all()
    return render_to_response("query.html", {"team_list":team_list})

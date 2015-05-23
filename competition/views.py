#coding=utf-8
from django.shortcuts import render_to_response
from django.http import JsonResponse
from questions.models import Questions
from register.models import Team
from django.views.decorators.csrf import csrf_exempt


def compete(request):
    qt_list = Questions.objects.all()[:]
    return render_to_response('competition.html',{'qt_list':qt_list})
@csrf_exempt
def verify(request, ans, num):
    num = int(num)
    trueAns = Questions.objects.all()[num].answer
    print "recept answer is "+ans
    print trueAns
    print num
    if ans == trueAns:
        flag = 1
        team_name = request.user.username
        team = Team.objects.get(account=team_name)
        team.score+=4
        if team.score >=60:
            pass
    #答对了一定数目的题目会给出图片题的提示
    else:
        flag = 0

    return JsonResponse({"flag":flag},)

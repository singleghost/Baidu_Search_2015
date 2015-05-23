#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from register.models import Team,Team_member
from register.forms import RegisterForm
#from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail

@csrf_exempt
def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #hash the password
            hashed_pass = make_password(cd['password'])
            team_info =Team(name = cd['team_name'],
                            account = cd['account'],
                            password = hashed_pass,
                            )
            team_info.save()
            mem1_info = Team_member(name = cd['m1_name'],
                                    sex =cd['m1_sex'],
                                    phone_number=cd['m1_phone_number'],
                                    phone_number_short=cd.get('m1_phone_number_short') if cd.get('m1_phone_number_short','') else 111111,
                                    team = team_info,
                                    )

            mem2_info = Team_member(name = cd['m2_name'],
                                    sex =cd['m2_sex'],
                                    phone_number=cd['m2_phone_number'],
                                    phone_number_short=cd.get('m2_phone_number_short') if cd.get('m2_phone_number_short','') else 111111,
                                    team = team_info,
                                    )
            mem3_info = Team_member(name = cd['m3_name'],
                                    sex =cd['m3_sex'],
                                    phone_number=cd['m3_phone_number'],
                                    phone_number_short=cd.get('m3_phone_number_short') if cd.get('m3_phone_number_short','') else 111111,
                                    team=team_info,
                                    )

            mem1_info.save()
            mem2_info.save()
            mem3_info.save()
            #参赛队伍信息
            user_info = User(username = cd['account'],
                            password = hashed_pass,
                            is_staff =False,
                            is_active = True,
                            is_superuser = False,
                            )
            user_info.save()
            #给参赛队伍发送一封包含账号密码的邮件
            message = u'''这是一封认证邮件\n您的队伍已经成功报名参赛\n
                队伍账号为   %s\n登录密码为   %s\n此账号和密码用来在比赛的
                时候登录 请勿遗忘''' % (cd['account'], cd['password'])
            #send_mail('欢迎报名百度搜索大赛',message,'3140104773@zju.edu.cn',
             #       [cd['email']], fail_silently=False)
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegisterForm()
    return render_to_response('register_form.html',{'form':form},)

def success(request):
    return HttpResponse('Successful!')

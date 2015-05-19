#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from register.models import Team,Team_member
from register.forms import RegisterForm
#from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

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
                                    profession=cd.get('m1_profession',''),
                                    student_ID=cd['m1_student_id'],
                                    team = team_info,
                                    )

            mem2_info = Team_member(name = cd['m2_name'],
                                    sex =cd['m2_sex'],
                                    phone_number=cd['m2_phone_number'],
                                    phone_number_short=cd.get('m2_phone_number_short') if cd.get('m2_phone_number_short','') else 111111,
                                    profession=cd.get('m2_profession',''),
                                    student_ID=cd['m2_student_id'],
                                    team = team_info,
                                    )
            mem3_info = Team_member(name = cd['m3_name'],
                                    sex =cd['m3_sex'],
                                    phone_number=cd['m3_phone_number'],
                                    phone_number_short=cd.get('m3_phone_number_short') if cd.get('m3_phone_number_short','') else 111111,
                                    profession=cd.get('m3_profession',''),
                                    student_ID=cd['m3_student_id'],
                                    team=team_info,
                                    )

            mem1_info.save()
            mem2_info.save()
            mem3_info.save()
            user_info = User(username = cd['account'],
                            password = hashed_pass,
                            is_staff =False,
                            is_active = True,
                            is_superuser = False,
                            )
            user_info.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegisterForm()
    return render_to_response('register_form.html',{'form':form})

def success(request):
    return HttpResponse('Successful!')

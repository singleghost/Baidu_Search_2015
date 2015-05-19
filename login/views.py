from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    account = request.POST.get('account','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=account,password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/competition/')
    else:
        return render_to_response('home.html')

def logout_view(request):
    auth.logout(request)
    return render_to_response('home.html')

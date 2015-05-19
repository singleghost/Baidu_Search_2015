from django.shortcuts import render_to_response

def compete(request):
    return render_to_response('competition.html')

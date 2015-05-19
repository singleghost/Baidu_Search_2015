"""baidu_search_2015 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from register.views import register,success
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from login.views import login_view, logout_view
#from score_query.views import show_query_res
#from home.views import showpage
from competition.views import compete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^home/$', showpage),
    url(r'^register/$', register),
 #   url(r'^score_query/$', show_query_res),
  #  url(r'^competition/$', compete),
    url(r'^register/success/$', success),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'),
        name ='home'),
    url(r'^home/about/$',TemplateView.as_view(template_name="about.html")),
    url(r'^home/rule/$',TemplateView.as_view(template_name="rule.html")),
    url(r'^login-in/$', login_view),
    url(r'^competition/$',compete ),
]

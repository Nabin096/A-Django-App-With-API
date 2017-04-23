from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "login"

urlpatterns = [

    url(r'^$',views.register,name='register'),
    url(r'^(?P<status>[0-9]+)/$',views.dashboard,name='dashboard'),
    url(r'^logout/$',views.logout,name='logout'),

]

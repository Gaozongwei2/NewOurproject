
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from . import views
app_name = "user"
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'login/',views.login, name="login"),
    url(r'regist/',views.regist, name="regist"),
    url(r'test/',views.test, name="test"),
    url(r'getusermessage/(?P<id>\w+)/$',views.getusermessage, name="getusermessage"),
    url(r'getmymessage/(?P<id>\w+)/$',views.getmymessage, name="getmymessage"),
    url(r'myfocusnum/(?P<id>\w+)/$',views.myfocusnum, name="myfocusnum"),
    url(r'myfocus/(?P<id>\w+)/$',views.myfocus, name="myfocus"),
    url(r'updateusermessage/',views.updateusermessage, name="updateusermessage"),
    url(r'searchsecrit/(?P<id>\w+)/$',views.searchsecrit, name="searchsecrit"),
    url(r'addtravelnotes/',views.addtravelnotes, name="addtravelnotes"),
    url(r'updatecollect/',views.updatecollect, name="updatecollect"),


    url(r'hotcity/',views.hotcity, name="hotcity"),

]

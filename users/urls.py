
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
    url(r'unfocus/(?P<uid>\w+)/(?P<uid_id>\w+)/$',views.unfocus, name="unfocus"),
    # 查询用户关注
    url(r'focus/(?P<uid>\w+)/$', views.focus, name="focus"),
    # 取消用户关注
    url(r'unfocus/(?P<uid>\w+)/(?P<uid_id>\w+)/$', views.unfocus, name="unfocus"),
    # 查询用户收藏攻略
    url(r'colstrategy/(?P<uid>\w+)/$', views.colstrategy, name="colstrategy"),
    # 查看用户收藏游记
    url(r'coltravelnote/(?P<uid>\w+)/$', views.coltravelnote, name="coltravelnote"),
    # 取消用户收藏攻略
    url(r'uncolstrategy/(?P<cstrid>\w+)/(?P<uid>\w+)/$', views.uncolstrategy, name="uncolstrategy"),

    # 查询用户游记
    url(r'usertravelnotes/(?P<uid>\w+)/$', views.usertravelnotes, name="usertravelnotes"),
    # 查询用户攻略
    url(r'userstrategy/(?P<uid>\w+)/$', views.userstrategy, name="userstrategy"),

    url('searchbysome/(?P<index>\w+)/$', views.searchbysome, name="searchbysome"),

    # 推荐地点
    url('searcharea/(?P<city>\w+)/$', views.searcharea, name="searcharea"),
]

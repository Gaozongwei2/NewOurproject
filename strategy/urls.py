
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name = "strategy"
urlpatterns = [
    # 游记展示
    url(r'show/', views.show, name="show"),
    # 编写游记
    url(r'edit/', views.edit, name="edit"),

    url('insertdetail/', views.insertdetail, name="insertdetail"),

    # url('searchbyuserid/(?P<userid>\w+)/$', views.searchbyuserid, name="searchbyuserid"),
    url('insertdetail/', views.insertdetail, name="insertdetail"),
    # 展示全部攻略
    url(r'showall/', views.showall, name="showall"),
    # 根据搜索结果展示
    url(r'showall/', views.showall, name="showall"),
#     查询用户自己的攻略
    url(r'searchbyuserid/',views.searchbyuserid,name="searchbyuserid"),
#     详情展示
    url(r'showdetail/(?P<postid>\d+)/$', views.showdetail, name="showdetail"),
    # 地点 用户名 title
    url(r'searchbysome/(?P<index>\w+)/(?P<scondition>\w+)/$', views.searchbysome, name="searchbysome"),

    # 新建攻略
    url(r'add/', views.add, name="add"),
    #  更新攻略
    url(r'update/(?P<postid>\d+)/$', views.update, name="update"),
    #  删除攻略
    url(r'delete/', views.delete, name="delete"),

    # 查询攻略的评论
    url(r'scommit/(?P<userid>\w+)/$', views.scommit, name="scommit"),

# 2018.10.24
    url('searchbysome/(?P<index>\w+)/$', views.searchbysome, name="searchbysome"),

    # 查询用户是否已经点赞过某个攻略
    url('hasgood/(?P<sid>\w+)/(?P<userid>\w+)/$', views.hasgood, name="hasgood"),
    # 更新攻略点赞状态
    url('updategood/(?P<sid>\w+)/(?P<userid>\w+)/$', views.updategood, name="updategood"),

]

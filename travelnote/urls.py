
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name = "travelnote"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^$',views.index, name="index"),
    # url('login/',views.login, name="login"),
    url('searchall/',views.searchall, name="searchall"),
    url('searchbyuserid/(?P<userid>\w+)/$',views.searchbyuserid, name="searchbyuserid"),
    # 根据游记查看用户去过哪些地方
    url(r'gonecity/(?P<userid>\w+)/$', views.gonecity, name="gonecity"),

    # 查询游记的评论
    url(r'tcommit/(?P<userid>\w+)/$', views.tcommit, name="tcommit"),
    url('searchbysome/(?P<index>\w+)/$',views.searchbysome, name="searchbysome"),

]

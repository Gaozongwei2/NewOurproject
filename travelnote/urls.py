
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name = "travelnote"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^$',views.index, name="index"),
    # url('login/',views.login, name="login"),
    # 查询所有的游记
    url('searchall/',views.searchall, name="searchall"),
    # 根据id查询游记
    url('searchbyuserid/(?P<userid>\w+)/$',views.searchbyuserid, name="searchbyuserid"),
    # 根据游记查看用户去过哪些地方
    url(r'gonecity/(?P<userid>\w+)/$', views.gonecity, name="gonecity"),
    # 查询游记的评论
    url(r'tcommit/(?P<userid>\w+)/$', views.tcommit, name="tcommit"),
    # 普通搜索功能
    url('searchbysome/(?P<index>\w+)/$',views.searchbysome, name="searchbysome"),
    # 查询用户是否已经点赞过某个游记
    url('hasgood/(?P<tid>\w+)/(?P<userid>\w+)/$', views.hasgood, name="hasgood"),
    # 更新游记点赞状态
    url('updategood/(?P<tid>\w+)/(?P<userid>\w+)/$', views.updategood, name="updategood"),
    # 根据游记id查询具体的游记内容
    url('detailcontent/(?P<tid>\w+)/$', views.detailcontent, name="detailcontent"),
    url('savecontent/',views.savecontent, name="savecontent"),
    url('getcontent/(?P<id>\w+)/$',views.getcontent, name="getcontent"),
    url('savetravelnote/',views.savetravelnote, name="savetravelnote"),

    url('storagereview/(?P<tid>\w+)/(?P<uid>\w+)/$', views.storagereview, name="storagereview"),
    # 更新浏览数量
    url('updatelooknum/(?P<tid>\w+)/$', views.updatelooknum, name="updatelooknum"),
    # 查询用户评论
    url('searchreview/(?P<tid>\w+)/$', views.searchreview, name="searchreview"),
    # 查询文章是否被收藏过
    url('searchcollect/(?P<cid>\w+)/', views.searchcollect, name="searchcollect")

]

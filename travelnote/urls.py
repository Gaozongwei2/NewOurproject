
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
    url('searchbysome/(?P<index>\w+)/$',views.searchbysome, name="searchbysome"),
    url('savecontent/',views.savecontent, name="savecontent"),
    url('getcontent/(?P<id>\w+)/$',views.getcontent, name="getcontent"),

]

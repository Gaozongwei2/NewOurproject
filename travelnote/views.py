from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
import json
from . import models
import time
from datetime import datetime
# 查询方法
def gettravelnote(res):
    tposts = models.travelnote.objects.filter(title__icontains=res).values()
    print(tposts)
    return tposts
# 查询所有的游记``
def searchall(request):

    try:
        travelnotes = models.travelnote.objects.filter().values("id","title","good","view","state","cover__url","userid__icno__imageurl","userid__username")
        travelnotes = list(travelnotes)
        return HttpResponse(json.dumps(travelnotes))
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})
# 根据id查询游记
def searchbyuserid(request,userid):
    try:
        mytravelnotes = models.travelnote.objects.filter(userid = userid).values("title","time","","cover__url","state","good","view","condition__condition")
        mytravelnotes = list(mytravelnotes)
        for item in mytravelnotes:
            item["time"] = item["time"].strftime("%Y-%m-%d")
        mytravelnotes = json.dumps(mytravelnotes)
        return HttpResponse(mytravelnotes)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})

# 展示游记详细信息
def gettravelnotedetail(request,id):
    if request.method == "GET":

        detail = models.travelnote.objects.filter(id = id).values("userid__username","userid__icno__imageurl","title","time","cover__url","tcontent__contentt","good","view","state")
        detail = list(detail)
        for item in detail:
            item["time"] = item["time"].strftime("%Y-%m-%d")
        return HttpResponse(json.dumps(detail))



# 普通搜索功能
def searchbysome(request):
    pass
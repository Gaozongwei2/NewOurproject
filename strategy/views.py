from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request

import json
import time
from django.db import connection
from travelnote.models import *
from users.views import updatemark
from django.http import *
import json
from . import models
import  tools.toolmethod as time
import tools.toolmethod


# from travelnote.models import *
def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter().values()
        return HttpResponse(data)
    if request.method == 'POST':
        print(request.body)
        data = request.POST.get("content")
        print(data)
        data = {
            "content": str(data)
        }
        # data = json.loads(data)

        # data = {
        #     "content":''
        # }

        aa = models.test.objects.create(**data)

        return HttpResponse(aa)
    else:
        return HttpResponse("失败")

    # 插入详情
    # Create your views here.


def show(request):
    # 帖子id
    pass
    # try:
    #     pid = request.GET.get('postid')
    #     print(pid)
    #     contents = models.content.objects.filter(postid=1).values()
    #     contents = list(contents)
    #     for item in contents:
    #         item["time"] = item["time"].strftime("%Y-%m-%d")
    #     contents = json.dumps(contents)
    #     return HttpResponse(contents)
    # except Exception as ex:
    #     print(ex)
    #     return JsonResponse({"code":"500"})


def edit(request):
    pass
    # if request.method=="POST":
    #     try:
    #         dcontent=request.POST.get("content")
    #         djcontent = {
    #             "html":dcontent
    #         }
    #         print(111)
    #         jdata = json.dumps(djcontent)
    #         f = open('file1.json','w')
    #         f.write(jdata)
    #         f.close()
    #         return JsonResponse({"code": 200})
    #     except Exception as ex:
    #         return JsonResponse({"code": 404})
    # elif request.method == "GET":
    #     return JsonResponse({"code": 100})


def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter(id="2").values('content')
        # data = str(data)
        # data = list(data)
        # temdata = data[0]['content']
        # print(type(temdata))
        return HttpResponse(json.dumps(list(data), ensure_ascii=False))
        # return JsonResponse({"content":temdata},json_dumps_params={'ensure_ascii':False})
    if request.method == 'POST':

        data = json.loads(request.body, strict=False)
        # data =request.body
        aa = models.test.objects.create(**data)
        # print(type(data.decode('utf-8')))
        # content1 = {
        #     "content" : data
        # }
        # print(json.dumps(data.decode()))
        print(aa)
        return HttpResponse('')
    else:
        return HttpResponse("失败")


# 卡片展示所有攻略
def showall(request):
    try:
        allstrategy = models.strategy.objects.filter().values('id', "title", 'time', "scover__url","condition__condition", "good", "view", "state","userid_id", "userid__username", "userid__icno__imageurl")
        listallstrategy = timechange(allstrategy)
        print(listallstrategy)
        return HttpResponse(listallstrategy)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "505"})
    # 格式转化


def timechange(contents):
    contents = list(contents)
    if len(contents):
        for item in contents:
            print(type(item))
            item["time"] = item["time"].strftime("%Y-%m-%d")
        contents = json.dumps(contents)
        print(contents)
        print(type(contents))
    else:
        contents.append({"this":"nodata"})
        contents = json.dumps(contents)
        print("haha"+contents)
        print(type(contents))
    return contents


def timechangeu(contents):
    contents = list(contents)
    if len(contents):
        for item in contents:
            print(item)
            item["birthday"] = item["birthday"].strftime("%Y-%m-%d")
        contents = json.dumps(contents)
    else:
        contents = [{"result": "nodata"}]
    return contents





# 用户查询自己的攻略(卡片)
def searchbyuserid(request):
    if request.method == "GET":
        try:
            uid = request.GET.get('userid')
            strategy = models.strategy.objects.filter(userid=uid).values('scover__url', 'condition__strategy__title', 'condition__strategy__good','condition__strategy__view', 'condition__strategy__userid','condition__strategy__userid')
            strategy = list(strategy)
            strategy = json.dumps(strategy)
            return HttpResponse(strategy)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "500"})
    elif request.method == "POST":
        return JsonResponse({"code": "505"})

# 用户查询自己的攻略数量
def searchcount(request,uid):
    try:
        strategy = models.strategy.objects.filter(userid=uid).values().count()
        print(strategy)
        return HttpResponse(strategy)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})

# 攻略详情展示
def showdetail(request, postid):
    if request.method == "POST":
        try:
            contenttop = models.sccontent.objects.filter(sid=postid).values('contents')
            commitbtm = models.scommit.objects.filter(sid=postid).values("commit", "userid__username", 'time')

            # 时间转换
            for item in commitbtm:
                item["time"] = item["time"].strftime("%Y-%m-%d")
            return JsonResponse({"contenttop": list(contenttop), "commitbtm": list(commitbtm)},
                                json_dumps_params={"ensure_ascii": False})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "500"})
    elif request.method == "GET":
        return JsonResponse({"code": "505"})


# 新建攻略
def add(request):
    try:
        # test data
        # data1={
        #         "title":"hoooooooooohhhhh",
        #         "state":"hhhh",
        #         "condition_id":2,
        #         "cover":"oooo",
        #         "time":"2018-9-4",
        #     "good":11,
        #     "view":66,
        #     "userid_id":2,
        #     "condition":2,
        #     "contents":"1212121212121",
        #     "url":"3333333333"
        # }
        data1 =json.loads(request.body)
        # strategy
        data_strategy = {
            "state": data1["state"],
            "title": data1["title"],
            "time": data1["time"],
            "good":data1["good"],
            "view":data1["view"],
            "userid_id": data1["userid_id"],
            "condition_id": data1["condition"]
        }
        sstrategy = models.strategy.objects.create(**data_strategy)
        # contents
        data_contents = {
            "contents": data1["contents"],
            "sid_id":sstrategy.id
        }
        scontent = models.sccontent.objects.create(**data_contents)
        # cover
        data_cover = {
            "url":data1["url"],
            "sid_id": sstrategy.id
        }
        scover = models.scover.objects.create(**data_cover)
        # 新建攻略后更新用户积分
        if sstrategy and scontent and scover:
            # 新建攻略用户所得积分
            mark=30
            updatemark(request,data1["userid_id"],mark)
            # 更新成功
            return  JsonResponse({"code": "200"})
        else:
            # 更新失败
            return  JsonResponse({"code": "500"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})


# 根据postid更新攻略信息
def update(request, postid):
    try:
        if request.method == "POST":
            newdate = json.loads(request.body)

            # newdata = {
            #     "title":"newdate",
            #     "state":"hhhh",
            #     "condition_id":2,
            # #     封面
            #     "cover":"oooo",
            # #     图片
            #     "img":{
            #         "img1":"11111",
            #         "img2":"22222"
            #     }
            # }

            affect_rows = models.strategy.objects.filter(id=postid).update(title=newdate["title"], state=newdate["state"],condition_id=newdate["condition_id"])
            affect_rowsurl = models.scover.objects.filter(id=postid).update(url=newdate["cover"])
            affect_rowsimg = models.simages.objects.filter(id=postid).update(url=newdate["img"]["img1"])
        return JsonResponse({"code": "200"})
    except Exception as ex:
        print(ex)
    return JsonResponse({"code": "500"})


# 删除攻略
def delete(request):
    try:
        sid = request.GET.get('sid_id')
        pcontent = models.sccontent.objects.filter(sid_id=sid).delete()
        pcommit = models.scommit.objects.filter(sid_id=sid).delete()
        pcover = models.scover.objects.filter(sid_id=sid).delete()
        pimage = models.simages.objects.filter(sid_id=sid).delete()
        pstrate = models.strategy.objects.filter(id=sid).delete()
        return JsonResponse({"code": "200"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})

# 获取用户的攻略评论
def scommit(request,userid):
    scommit = models.scommit.objects.filter(userid_id=userid).values('sid_id','commit','time','sid__scover__url')
    scommit =list(scommit)
    scommit = time.changestyleC(scommit)
    return HttpResponse(scommit)




# 2018.10.24
# 普通搜索功能
def searchbysome(request,index):
    if request.method =="GET":
        if (index == "index"):
            tport = models.strategy.objects.filter(condition_id=2).values("id","title","time","scover__url","content","view","userid__icno__imageurl","userid__username")
            tport = tools.toolmethod.changestyle(tport)
        else :
            tport = models.strategy.objects.filter(title__icontains=index ,condition_id=2).values("id","title","time","scover__url","content","view","userid__icno__imageurl","userid__username")
            tport = tools.toolmethod.changestyle(tport)
        return HttpResponse(tport)
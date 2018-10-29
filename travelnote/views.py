from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
import json
from . import models
import tools.toolmethod
import time
from datetime import datetime
import  tools.toolmethod as time
# 查询用户游记数量
def tnum(userid):
    num = models.travelnote.objects.filter(userid_id=userid).count()
    return num
# 查询方法
def gettravelnote(res):
    tposts = models.travelnote.objects.filter(title__icontains=res).values()
    print(tposts)
    return tposts
# 查询所有的游记``
def searchall(request):
    try:
        travelnotes = models.travelnote.objects.filter().values("id", "title", "good", "view", "state", "cover__url",
                                                                "userid__icno__imageurl", "userid__username")
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
def searchbysome(request,index):
    if request.method =="GET":
        if (index == "index"):
            tport = models.travelnote.objects.filter(condition_id=2).values("id","title","time","cover__url","content","view","userid__icno__imageurl","userid__username")
            tport = tools.toolmethod.changestyle(tport)
        else:
            tport = models.travelnote.objects.filter(title__icontains=index, condition_id=2).values("id", "title","time","cover__url","content", "view","userid__icno__imageurl","userid__username")
            if len(list(tport))==0:
                tport = models.travelnote.objects.filter(state__icontains=index, condition_id=2).values("id", "title", "time","cover__url","content", "view","userid__icno__imageurl","userid__username")
            if len(list(tport)) == 0:
                tport = models.travelnote.objects.filter(content__icontains=index,condition_id=2).values("id", "title", "time","cover__url","content", "view","userid__icno__imageurl","userid__username")
            tport = tools.toolmethod.changestyle(tport)
        return HttpResponse(tport)

# 用户查询自己的游记数量
def searchcount(request,userid):
    try:
        travelnote = models.travelnote.objects.filter(userid_id=userid).values().count()
        print(travelnote)
        return HttpResponse(travelnote)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})

# 2018.10.24
# 保存游记内容
def savecontent(request):
    if request.method == "POST":
        ncontent = request.POST.get("content")
        print(ncontent)
        nncontent = models.tcontent.objects.create(contentt=ncontent)
        print(nncontent.id)
        return HttpResponse(nncontent.id)
    else:
        return HttpResponse("这里是请求")

# 保存整个游记
def savetravelnote(request):
    if request.method == "POST":
        title = request.POST.get("title")
        state = request.POST.get("state")
        content = request.POST.get("content")
        time = request.POST.get("time")
        cover_id = request.POST.get('cover_id')
        condition_id = request.POST.get('condition_id')
        good = request.POST.get('good')
        userid_id = request.POST.get('userid_id')
        view = request.POST.get('view')
        content_id = request.POST.get('content_id')

        nncontent = models.travelnote.objects.create(
            title=title,
            state=state,
            content=content,
            time=time,
            cover_id=cover_id,
            condition_id=condition_id,
            good=good,
            view=view,
            userid_id=userid_id,
            contentall_id=content_id
        )
        # print(nncontent.id)
        # return HttpResponse(nncontent.id)
        return HttpResponse("chenggong")
    else:
        return HttpResponse("这里是请求")


# 取出游记内容(废掉)
def getcontent(request, id):
    if request.method == "GET":
        content = json.dumps(list(models.tcontent.objects.filter(id=id).values("contentt"))[0])
        return HttpResponse(content)


# 存储用户评论
def storagereview(request, tid, uid):
    # if request.method =="POST":
    # 获取前端传过来的数据
    if request.method == "POST":
        dat = request.POST.get('date')
        commi = request.POST.get('content')
        # res = json.dumps(request.body)

        res = models.tcommit.objects.create(commit=commi, time=dat, tid_id=1, userid_id=1)
        return JsonResponse({"code": "200"})


# 根据tid查评论
def searchreview(request, tid):
    try:
        userreview = models.tcommit.objects.filter(tid_id=tid).values("commit", "time", "tid__userid__username",
                                                                      'tid__userid__icno')
        data = list(userreview)

        return JsonResponse({'data': data})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})


# 根据tid更新浏数量
def updatelooknum(request, tid):
    # print(2222222)
    if request.method == "POST":
        res = request.POST.get('view')
        # print(1111)
        print(res)

        # newdate = {
        #     "view":"177777"
        # }
        affect_row = models.travelnote.objects.filter(id=tid).update(view=res)
        return JsonResponse({"code": "200"})


# 根据id查询是否收藏过文章
def searchcollect(request, cid):

    try:
        usercollect = models.tcollection.objects.filter(id=1).values("tid_id")
        if usercollect:
            return JsonResponse({'code':'被收藏过'})
        else:
            return JsonResponse({'code':'没被收藏过'})

        return JsonResponse({"code": collect})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})

# 根据游记查询用户去过哪些地方
def gonecity(request, userid):

        city = models.travelnote.objects.filter(userid_id=userid).values('state')
        # city2 = models.travelnote.objects.filter(userid_id=userid).values('state')
        # city = list(city)
        # city = json.dumps(city)
        # setcity = set(city)
        li =[]
        for item in city:
            if item['state'] in li:
                pass
            else:
                li.append(item['state'])

        # 随机分配图片
        img = models.travelnote.objects.filter(userid_id=userid).values('cover__url')[:len(li)]
        img = list(img)
        for i in range(len(li)):
            img[i]["city"] = li[i]
        return HttpResponse(json.dumps(img))

# 查询用户游记的评论
def tcommit(request,userid):

    tcommit = models.tcommit.objects.filter(userid_id=userid).values('tid_id','commit','time','tid__cover__url','tid__title')
    tcommit =list(tcommit)
    tcommit = time.changestyleC(tcommit)
    return HttpResponse(tcommit)

# 查询用户是否已经点赞过某个游记,以及当前游记的被点赞数
def hasgood(request,tid,userid):
    goodcount = models.travelnote.objects.filter(id=tid,userid_id=userid).values('file1','good')
    goodcount = list(goodcount)
    # goodcount = json.dumps(goodcount)

    if goodcount[0]["file1"]=='0':
        goodcount[0]["file1"]='点赞'
    else:
        goodcount[0]["file1"] = '已点赞'

    return JsonResponse({"data":goodcount})


# 更新用户的点赞状态
def updategood(request,tid,userid):
    if request.method == "POST":
        goods = request.POST.get("good")
        updatecount = models.travelnote.objects.filter(id=tid,userid_id=userid).update(good=goods,file1=1)
        return HttpResponse(goods)
    else:
        return HttpResponse("这里是请求")

# 根据游记id显示里面具体的内容
def detailcontent(request,tid):
    detailcontent =  models.travelnote.objects.filter(id=tid).values('contentall__contentt')
    detailcontent = list(detailcontent)
    return JsonResponse({"code":detailcontent})



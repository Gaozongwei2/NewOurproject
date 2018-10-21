from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
from django.http import *
import json
from . import models
from .utils.util_token import *
import re

# 获取用户信息
def getuser(res):
    user = models.user.objects.filter(username__icontains=res).values()
    return user


# 用户中心
def index(request):
    if request.method =="GET":
        return HttpResponse("欢迎来到用户中心")
    elif request.method =="POST":
        print(type(str(request.body)))
        print(json.loads(str(request.body)))
        return HttpResponse("这里是用户中心")
# 测试方法
def test(request):
    try:
        user = models.user.objects.all().values('telephone','username','icno__imageurl','sex__sex','login__password')
        print(user)
        return HttpResponse("测试")
    except Exception as ex:
        return HttpResponse("error")
# 用户登录
# def login(request):
#     if request.method=='POST':
#         user=json.loads(request.body)
#         print(user)
#         # 首先判断手机号，密码是否为空
#         # 判断手机号是否合法
#         # 查询数据库中是否存在此电话号码
#         # 若存在取出其对应的密码
#         # 密码对照
#         # 成功，返回用户数据(电话号码)
#         # 失败，返回提示信息
#         # (上面的每一步判读失败都要有对应的状态码返回 )
#         result=models.login.objects.filter(telephone=user['telephone'],password=user['password']).values()
#         if len(result):
#             result = json.dumps(list(result))
#             return HttpResponse(result)
#             return JsonResponse({"code":"808"})
#         else:
#             return HttpResponse(result)
#             return JsonResponse({"code":"408"})
#     else:
#         return JsonResponse({"code": "408"})
# 用户登录
# def login(request):
#     if request.method == "POST":
#         try:
#             # 首先获取telephone
#             user = json.loads(request.body)
#             # 验证手机号是否符合要求
#             telephone = user["telephone"]
#             print(telephone)
#             if len(telephone) == 0:
#                 print(user)
#                 return JsonResponse({"error":"手机号不能为空"})
#             if len(telephone)== 11 and telephone.isdigit():
#                 print("here")
#                 telephone = models.login.objects.filter(telephone=user["telephone"])
#                 if len(telephone):
#                     if user["password"] == telephone[0].password:
#                         # 登录成功，签发token
#                         token = jwtEncoding(telephone)
#                         # resp["Access-Control-Expose-Headers"] = "token"
#                         # 页面跳转到首页（登录后的）
#                         return JsonResponse({"code":"233"})# 信息正确，登录成功
#                     else:
#                         return JsonResponse({"code":"244"})# 用户名存在，但是密码错误
#                 return JsonResponse({"code":"255"})# 电话号不存在，用户尚未注册
#             else:
#                 return JsonResponse({"error":"手机号不合法"})
#         except Exception as ex:
#             print(ex)
#             return JsonResponse({"code":"500"})
#     elif request.method == "GET":
#         return JsonResponse({"code":200})

# 用户注册

# 用户注册
def login(request):
    tel = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    if request.method == 'POST':
        user = json.loads(request.body)
        print(user)
        if len(user['telephone']):
            res = re.search(tel, user['telephone'])
            if res:
                result = models.login.objects.filter(telephone=user['telephone'], password=user['password']).values(
                    'telephone')
                if len(result):
                    result = list(result)
                    return JsonResponse({"code": "202", "telephone": result[0]['telephone']})
                else:
                    return JsonResponse({"code": "406"})
            else:
                return JsonResponse({"code": "406"})
        else:
            return JsonResponse({"code": "手机号不能为空"})
    else:
        return JsonResponse({"code": "406"})

def regist(request):
    if request.method == "POST":
        # 获取前端传过来的数据
        usermsg = json.loads(request.body)
        users={
            "telephone":usermsg["telephone"],
            "password":usermsg["password"]
        }
        # print(usermsg)
        # 查询telephone是否存在
        # print(usermsg["telephone"])
        user = models.login.objects.filter(telephone=usermsg["telephone"])
        # print(user)
        if len(user):
            return HttpResponse("该用户已存在，请登录")
        else:
            pwd=usermsg["password"]
            pwd1=usermsg["password1"]
            if pwd==pwd1:
                uu=models.login.objects.create(**users)
                print(uu.id)
                # 返回电话号码
                return JsonResponse({"code":"202"})
            else:

                return HttpResponse('两次密码不一致')
            return JsonResponse({"code":"406"})
    else:
        # GET 请求
        return JsonResponse({"code":"406"})
# def regist(request):
#     if request.method == "POST":
#         # 获取前端传过来的数据
#         usermsg = json.loads(request.body)
#         print(usermsg)
#         # 查询telephone是否存在
#         user = models.login.objects.filter(telephone=usermsg[0]["telephone"])
#         if len(user):
#             return HttpResponse("该用户已存在，请登录")
#         else:
#             # 将数据插入数据库中
#             newlog = models.login.objects.create(**usermsg[0])
#             print(newlog.id)
#             newuser = models.user.objects.create(**usermsg[1])
#             return HttpResponse(newuser.telephone)
#     return HttpResponse("注册")

# 查询个人信息
def getusermessage(request,id):
    if request.method == "GET":
        usermessage = models.user.objects.filter(id = id).values("username", "sex__sex", "birthday", "icno__imageurl","state","content")
        usermessage = list(usermessage)
        for item in usermessage:
            item["birthday"] = item["birthday"].strftime("%Y-%m-%d")
        usermessage = json.dumps(list(usermessage))
    return HttpResponse(usermessage)
# 修改个人信息
def updateusermessage(request):
    if request.method=="POST":
        usermessage = request.POST.get("user")
        print(usermessage)
        usermessage = json.loads(usermessage)
        print(usermessage["username"])
        print(usermessage)
        newuser = models.user.objects.get(id = usermessage["id"])
        newuser.username = usermessage["username"]
        newuser.birthday = usermessage["birthday"]
        newuser.state = usermessage["state"]
        newuser.content = usermessage["content"]
        newuser.save()

        print(newuser)
        return HttpResponse("成功")
    else:
        return HttpResponse("这里是请求")


# 查询关注人数
def myfocusnum(request,id):
    # 关注人数
    focus = models.focus.objects.filter(userid = id).values().count()
    # 粉丝数
    fans = models.focus.objects.filter(uid_id=id).values().count()
    some = {
        "focus":focus,
        "fans":fans,
    }
    return JsonResponse(some)
# 查询用户表的游记数

# 查询用户发布的帖子数


# 查询关注用户信息
def myfocus(request, id):
    usermessage = list(),
    message = []
    focusid = models.focus.objects.filter(userid=id).values("uid")
    focusid = list(focusid)
    for i in range(len(focusid)):
        message.append(list(models.user.objects.filter(id = focusid[i]["uid"]).values("id","username","icno__imageurl"))[0])
    return HttpResponse(message)


# 查询神秘代码
def searchsecrit(request,id):
    if request.method == "GET":
        data = models.test.objects.filter(id = id).values("content")
        data = list(data)[0]["content"]
        print(data)
        # print(json.dumps(list(data)))
        return HttpResponse(data)
        return HttpResponse("要查询神秘代码吗？？？")
    # else:
    #     data = models.test.objects.filter(id = 18).values("content")
    #     print(json.dumps(list(data)))
    #     return HttpResponse(json.dumps(list(data)))
def addtravelnotes(request):
    if request.method =="POST":
        # 获取前端传过来的数据
        print(request.body)
        resp = request.body
        # 将数据存入数据库
        res = models.test.objects.create(content=resp)
        print(res)
        return JsonResponse({"code": "200"})
    else:
        return HttpResponse("error")
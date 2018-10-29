from django.db import models
from users.models import *


# 攻略状态
class condition(models.Model):
    condition = models.CharField(max_length=20, null=True)

# 攻略封面
class scover(models.Model):
    url = models.TextField()
    file1 = models.CharField(max_length=50, null=True)
    file2 = models.CharField(max_length=50, null=True)

# 攻略
class strategy(models.Model):
    title = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=20)
    good = models.IntegerField()
    # 浏览量python manage.py makemigrations
    view = models.IntegerField()
    content = models.CharField(max_length=200,null=False,default="聪明人才能看到的简介")
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE,default=1)
    condition = models.ForeignKey(to='condition',to_field='id', on_delete=models.CASCADE)
    scover = models.ForeignKey(to='scover',to_field='id', on_delete=models.CASCADE,default=1)
    file1 = models.CharField(max_length=100, null=True)
    file2 = models.CharField(max_length=100, null=True)
# 攻略内容
class scontent(models.Model):
    contents = models.TextField(default='not have message',null=True)
    # 地点)
    # 优点
    advantage = models.TextField(null=True)
    # 地点
    address = models.TextField(null=True)
    # 地点)
    # 游玩攻略
    play = models.TextField(null=True)
    # 地点)
    # 游玩图片
    playphoto = models.TextField(null=True)
    # 地点)
    # 交通攻略
    traffic = models.TextField(null=True)
    # 地点)
    # 门票攻略
    ticket = models.TextField(null=True)
    # 地点)
    # 餐饮攻略
    food = models.TextField(null=True)
    # 地点)
    # 餐饮图片
    foodphoto = models.TextField(null=True)
    # 地点)
    # 对应攻略的外键
    sid = models.ForeignKey(to='strategy', to_field='id', on_delete=models.CASCADE,default=1)
    file1 = models.CharField(max_length=50, null=True)
    file2 = models.CharField(max_length=50, null=True)

# 攻略图片
class simages(models.Model):
    url = models.TextField()
    sid = models.ForeignKey(to='strategy', to_field='id', on_delete=models.CASCADE)
    file1 = models.CharField(max_length=50, null=True)
    file2 = models.CharField(max_length=50, null=True)



# # 攻略评论
class scommit(models.Model):
    commit = models.TextField()
    time = models.DateTimeField(max_length=20)
    sid = models.ForeignKey(to='strategy', to_field='id', on_delete=models.CASCADE)
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE,default=1)

# 攻略收藏
class scollection(models.Model):
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE,default=1)
    sid = models.ForeignKey(to='strategy', to_field='id', on_delete=models.CASCADE)





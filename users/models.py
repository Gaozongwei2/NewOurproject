from django.db import models

from travelnote.models import *


# 登录表
class login(models.Model):
    telephone = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
# 性别表
class sex(models.Model):
    sex = models.CharField(max_length=10)
# 头像表
class icno(models.Model):
    imageurl = models.CharField(max_length=300)
# 用户表
class user(models.Model):
    telephone = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30)
    state = models.CharField(null=True, max_length=30)
    birthday = models.DateField(null=True,max_length=20)
    mark = models.IntegerField(null=True)
    content = models.TextField(null=True)
    filed1 = models.CharField(null=True, max_length=10)
    filed2 = models.CharField(null=True, max_length=10)
    login = models.ForeignKey(to='login', to_field='id', on_delete=models.CASCADE)
    icno = models.ForeignKey(default=1, to='icno', to_field='id', on_delete=models.CASCADE)
    sex = models.ForeignKey(default=1, to='sex', to_field='id', on_delete=models.CASCADE)

# 关注表
class focus(models.Model):
    # 一个人的id
    userid = models.IntegerField()
    uid = models.ForeignKey(to='user', to_field= 'id', on_delete=models.CASCADE)
    # 这个人关注的人的id


# 攻略收藏表
class colstrategy(models.Model):
    cstrategy = models.ForeignKey(to='strategy.strategy', to_field='id', on_delete=True)
    cuser = models.ForeignKey(to='user', to_field='id', on_delete=True)

# 游记收藏表
class coltravelnote(models.Model):
    ctravelnote = models.ForeignKey(to='travelnote.travelnote', to_field='id', on_delete=models.CASCADE)
    cuser = models.ForeignKey(to='user', to_field='id', on_delete=models.CASCADE)

# 成就表
class achievement(models.Model):
    minstandard = models.CharField(max_length=30,default=1)
    maxstandard = models.CharField(max_length=30,default=1)
    name = models.CharField(max_length=30)


# 热门城市表
class hotcity(models.Model):
    cityname = models.CharField(max_length=50, null=True)
    file1 = models.IntegerField(max_length=10, null=True)
    file2 = models.CharField(max_length=50, null=True)

# 热门景点
class hotviewpoint(models.Model):
    viewpoint = models.CharField(max_length=50,null=True)
    cityid = models.CharField(max_length=50,null=True)
    file1 = models.IntegerField(max_length=10, null=True)
    file2 = models.CharField(max_length=50, null=True)

# 新建省表
class province(models.Model):
    provinceID = models.CharField(max_length=10)
    province = models.CharField(max_length=40)


# 新建市表
class city(models.Model):
    cityID = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    father = models.CharField(max_length=10)
    # father = models.ForeignKey(unique= True ,to='province', to_field='provinceID', on_delete=models.CASCADE)

# 新建地区表
class area(models.Model):
    areaID = models.CharField(max_length=50)
    area = models.CharField(max_length=60)
    father = models.CharField(max_length=10)

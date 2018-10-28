from django.db import models

from users.models import *
# 封面
class tcover(models.Model):
    url = models.TextField()

# 帖子状态
class condition(models.Model):
    condition = models.CharField(max_length=20)

# 游记
class travelnote(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=20)
    good = models.IntegerField()
    view = models.IntegerField(null=False)
    state = models.CharField(max_length=200)
    content = models.TextField(default="聪明人才能看见的简介")
    file1 = models.CharField(max_length=200, null=True)
    file2 = models.CharField(max_length=200, null=True)
    userid = models.ForeignKey(to="users.user",to_field="id",on_delete= models.CASCADE,default=1)
    condition = models.ForeignKey(to='condition',to_field='id', on_delete=models.CASCADE,default=1)
    cover = models.ForeignKey(to='tcover',to_field='id',on_delete=models.CASCADE,default=1)
#    是否点赞

# 图片
class timages(models.Model):
    url = models.TextField()
    timages = models.ForeignKey(to='travelnote', to_field='id',on_delete=models.CASCADE)


# 内容
class tcontent(models.Model):
    contentt = models.TextField(default='not have message')
    tid = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE)

# 游记收藏
class tcollection(models.Model):
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE)
    tid = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE)
# # 游记评论
class tcommit(models.Model):
    commit = models.TextField()
    time = models.DateTimeField(max_length=20)
    tid = models.ForeignKey(to='travelnote', to_field='id', on_delete=models.CASCADE,default=1)
    userid = models.ForeignKey(to='users.user',to_field='id',on_delete=models.CASCADE,default=1)
    field01 = models.CharField(max_length=200, null= True)
    field02 = models.CharField(max_length=200, null= True)

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")

)


class BaseModel(models.Model):
    """抽象出一个基类,后面需要用到"""
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        """防止这个抽象类建表"""
        abstract = True


class UserCorrelation(AbstractUser):
    """用户信息"""

    nick_name = models.CharField(max_length=50, verbose_name="名称", null=True, blank=True)
    birthbay = models.DateField(verbose_name="生日",  null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address =  models.CharField(verbose_name="地址", max_length=100, default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg", verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"

        verbose_name_plural = verbose_name

    def __str__(self):

        if self.nick_name:
            return self.nick_name
        else:

            return self.username

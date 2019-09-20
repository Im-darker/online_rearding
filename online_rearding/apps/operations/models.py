# import os,django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")   # project_name指项目名
# django.setup()

from django.db import models
from django.contrib.auth import get_user_model

# from Share import FAV_TYPE, Message_Start
# from courses.models import Course
# from users.models import BaseModel
from Share import FAV_TYPE, Message_Start
from courses.models import Course
from users.models import BaseModel

User = get_user_model()



class UserAsk(BaseModel):
    """用户咨询"""
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="电话号码")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名称")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{mobile}_{course_name}".format(name=self.name,
                    mobile=self.mobile, course_name=self.course_name)


class CourseComment(BaseModel):
    """课程评论"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名称")
    comment = models.CharField(max_length=200, verbose_name="评论内容")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class UserFavorite(BaseModel):
    """用户收藏"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据id")
    fav_type = models.IntegerField(choices=FAV_TYPE, default=1, verbose_name="收藏类型")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    """用户消息"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    message_start = models.BooleanField(choices=Message_Start, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    """用户课程"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名称")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name

















































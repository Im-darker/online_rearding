
from django.db import models

# from .Share import COURSE_DEGREE
# from organizations.models import Teacher
# from users.models import BaseModel
# from Share import COURSE_DEGREE
from Share import COURSE_DEGREE
from organizations.models import Teacher, CourseOrg
from users.models import BaseModel


class Course(BaseModel):
    """课程"""

    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name="课程机构")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(max_length=70, verbose_name="课程名称",)
    describe = models.CharField(max_length=300, verbose_name="课程描述")
    Learning_time = models.IntegerField(default=0, verbose_name="学习时长")
    degree = models.CharField(choices=COURSE_DEGREE, max_length=6, verbose_name="课程难度")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default="", max_length=100, verbose_name="课程标签")
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师告诉你")

    datail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(upload_to="courses/%Y/%m", max_length=100, verbose_name="封面图")
    is_classic = models.BooleanField(default=False, verbose_name="是否经典")

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    """课程章节"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名" )
    name = models.CharField(max_length=100, verbose_name="章节名")
    learn_time = models.IntegerField(default=0, verbose_name="学习时长")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Vidoe(BaseModel):
    """课程视频"""
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name="章节视频")
    name = models.CharField(max_length=100,verbose_name=u"视频名")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长")
    url = models.CharField(max_length=200, verbose_name=u"视频地址")

    class Meta:
        verbose_name = "课程视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CurriculumResources(BaseModel):
    """课程资源"""
    CurriculumResources = models.ForeignKey(Vidoe, on_delete=models.CASCADE, verbose_name="课程资源")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m", max_length=200, verbose_name="下载地址")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
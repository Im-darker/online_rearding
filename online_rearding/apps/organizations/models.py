from django.db import models

# from Share import COURSEORG_CATEGORY
# from users.models import BaseModel
from Share import COURSEORG_CATEGORY
from users.models import BaseModel


class City(BaseModel):
    """城市"""
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    describe = models.CharField(max_length=200, verbose_name=u"描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        """解决后台界面显示城市乱码问题"""
        return self.name


class CourseOrg(BaseModel):
    """培训机构"""
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")
    name = models.CharField(max_length=50, verbose_name="机构名称")
    describe = models.TextField(verbose_name="相关描述")
    category = models.CharField(default="PXJG", choices=COURSEORG_CATEGORY, max_length=20, verbose_name=u"机构类别")
    tag = models.CharField(default="全国知名", max_length=10, verbose_name="机构标签")

    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    address = models.CharField(max_length=200, verbose_name="机构地址")
    image = models.ImageField(upload_to="org/%Y/%m", max_length=100, verbose_name=u"logo", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")

    is_auth = models.BooleanField(default=False, verbose_name="是否认证")
    is_gold = models.BooleanField(default=False, verbose_name="是否为金牌")

    def courses(self):
        # 反向取课程中的前三位经典课程
        course = self.course_set.filter(is_classic=True)[0:3]

        return course

    class Meta:
        verbose_name = "培训机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    """讲师"""
    courseOrg = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=20, verbose_name="讲师名称")
    worke_position = models.CharField(max_length=50, verbose_name="工作职位")
    worke_company = models.CharField(max_length=50, verbose_name="就职公司")
    worke_years = models.IntegerField(verbose_name="工作年限")
    points = models.CharField(max_length=100, verbose_name="教学特点")

    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    age = models.IntegerField(verbose_name="讲师年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", max_length=100, verbose_name="头像图")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


















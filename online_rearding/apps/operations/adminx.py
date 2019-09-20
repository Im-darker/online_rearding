
import xadmin

from operations.models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    """"把用户咨询到后台管理系统中"""
    # name = models.CharField(max_length=20, verbose_name="姓名")
    # mobile = models.CharField(max_length=11, verbose_name="电话号码")
    # course_name = models.CharField(max_length=50, verbose_name=u"课程名称")

    list_display = ["id", "name", "mobile", "course_name"]  # 后台系统中每个课程章节显示字段列
    search_fields = ["name", "mobile", "course_name"]  # 增加课程章节的搜索框以及搜索课程章节的字段
    list_filter = ["name", "mobile", "course_name"]  # 增加课程章节的过滤功能以及过滤课程章节的字段
    list_editable = ["name", "mobile", "course_name"]  # 增加课程章节字段的修改功能


class CourseCommentAdmin(object):
    """"把课程评论添加到后台管理系统中"""
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名称")
    # comment = models.CharField(max_length=200, verbose_name="评论内容")

    list_display = ["id", "user", "comment", "course"]
    search_fields = ["user", "comment", "course"]
    list_filter = ["user", "comment", "course"]
    list_editable = ["user", "comment", "course"]


class UserFavoriteAdmin(object):
    """"把用户收藏到后台管理系统中"""
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # fav_id = models.IntegerField(verbose_name="数据id")
    # fav_type = models.IntegerField(choices=FAV_TYPE, default=1, verbose_name="收藏类型")

    list_display = ["id", "user", "fav_type", "fav_id"]
    search_fields = ["user", "fav_type", "fav_id"]
    list_filter = ["user", "fav_type", "fav_id"]
    list_editable = ["user", "fav_type", "fav_id"]


class UserCourseAdmin(object):
    """"把培训机构添加到后台管理系统中"""

    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名称")

    list_display = ["id", "user", "course"]
    search_fields = ["user", "course"]
    list_filter = ["user", "course"]
    list_editable = ["user", "course"]


class UserMessageAdmin(object):
    """"把培训机构添加到后台管理系统中"""
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # message = models.CharField(max_length=200, verbose_name="消息内容")
    # message_start = models.BooleanField(choices=Message_Start, verbose_name="是否已读")

    list_display = ["id", "user", "message", "message_start"]
    search_fields = ["user", "message", "message_start"]
    list_filter = ["user", "message", "message_start"]
    list_editable = ["user", "message", "message_start"]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
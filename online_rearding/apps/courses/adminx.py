import xadmin

from courses.models import Course, Chapter, Vidoe, CurriculumResources


class ZaiXianXue(object):
    """添加标题"""
    site_title = "在线学习后台管理系统"
    site_footer = "在线学习网"
    # menu_style = "accordion"  # 给模块提供伸缩效果


class BaseSettings(object):
    """是否启动主题皮肤"""
    enable_themes = True
    user_bootswatch = True


class CourseAdmin(object):
    """"把课程信息添加到后台管理系统中"""

    list_display = ["id", "name", "describe", "Learning_time", "degree", "category", "tag",
                    "youneed_know", "teacher_tell", "add_time"]  # 后台系统中每个课程显示字段列
    search_fields = ["name", "degree", "Learning_time", "click_nums", "fav_nums",
                     "category", "students", "fav_nums"]  # 增加课程的搜索框以及搜索课程的字段
    list_filter = ["name", "describe", "add_time", "degree", "students", "category"]  # 增加课程的过滤功能以及过滤课程的字段
    list_editable = ["name", "describe", "tag", "teacher_tell"]  # 增加课程字段的修改功能


class ChapterAdmin(object):
    """"把课程章节添加到后台管理系统中"""

    list_display = ["id", "name", "course", "learn_time"]  # 后台系统中每个课程章节显示字段列
    search_fields = ["name", "course", "learn_time"]  # 增加课程章节的搜索框以及搜索课程章节的字段
    list_filter = ["name", "course", "learn_time"]  # 增加课程章节的过滤功能以及过滤课程章节的字段
    list_editable = ["name", "course", "learn_time"]  # 增加课程章节字段的修改功能


class VidoeAdmin(object):
    """"把课程视频添加到后台管理系统中"""

    list_display = ["id", "chapter", "learn_time", "url"]  # 后台系统中每个课程章节显示字段列
    search_fields = ["chapter", "learn_time"]  # 增加课程章节的搜索框以及搜索课程章节的字段
    list_filter = ["chapter", "learn_time"]  # 增加课程章节的过滤功能以及过滤课程章节的字段
    list_editable = ["chapter", "learn_time"]  # 增加课程章节字段的修改功能


class CurriculumResourcesAdmin(object):
    """"把课程资源加到后台管理系统中"""

    list_display = ["id", "name", "CurriculumResources", "file"]  # 后台系统中每个课程章节显示字段列
    search_fields = ["name", "CurriculumResources", "learn_time"]  # 增加课程章节的搜索框以及搜索课程章节的字段
    list_filter = ["name", "CurriculumResources"]  # 增加课程章节的过滤功能以及过滤课程章节的字段
    list_editable = ["name", "CurriculumResources"]  # 增加课程章节字段的修改功能


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Vidoe, VidoeAdmin)
xadmin.site.register(CurriculumResources, CurriculumResourcesAdmin)

xadmin.site.register(xadmin.views.CommAdminView, ZaiXianXue)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
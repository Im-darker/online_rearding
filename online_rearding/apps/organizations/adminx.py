import xadmin

from organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    """"把讲师添加到后台管理系统中"""


    list_display = ["id", "name", "courseOrg","age", "worke_position", "worke_company", "worke_years", "points",
                    "click_nums", "fav_nums"]
    search_fields = ["name", "worke_position", "worke_company", "worke_years", "points", "age"]
    list_filter = ["name", "worke_position", "worke_company", "worke_years", "points", "age"]
    list_editable = ["name", "worke_position", "worke_company", "worke_years", "points", "age"]


class CourseOrgAdmin(object):
    """"把培训机构添加到后台管理系统中"""

    list_display = ["id", "name", "city", "category", "tag", "address", "click_nums", "students"]
    search_fields = ["name", "city", "category", "address", "click_nums", "students", "course_nums", "fav_nums"]
    list_filter = ["name", "city", "category", "address", "click_nums", "students", "course_nums", "fav_nums"]
    list_editable = ["name", "city", "category", "address", "click_nums", "students", "course_nums", "fav_nums"]


class CityAdmin(object):
    """"把城市添加到后台管理系统中"""



xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)

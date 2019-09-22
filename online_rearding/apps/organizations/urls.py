from django.conf.urls import url
from .views import OrgView, AddCourse_Ask, OrgHomesView, OrgTeachersView, OrgCourseView, OrgDescView
urlpatterns = [
    # 课程机构首页
    url(r'list/$', OrgView.as_view(), name="list"),
    # 用户咨询窗口
    url(r'add_ask/$', AddCourse_Ask.as_view(), name="add_ask"),

    url(r'(?P<org_id>\d+)/$', OrgHomesView.as_view(), name="home"),
    url(r'(?P<org_id>\d+)/teacher/$', OrgTeachersView.as_view(), name="teacher"),
    url(r'(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    url(r'(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),



]
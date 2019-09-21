from django.conf.urls import url
from .views import OrgView, Add_Course_Ask, Org_HomesView, Org_TeachersView
urlpatterns = [
    # 课程机构首页
    url(r'list/$', OrgView.as_view(), name="list"),
    # 用户咨询窗口
    url(r'add_ask/$', Add_Course_Ask.as_view(), name="add_ask"),

    url(r'(?P<org_id>\d+)/$', Org_HomesView.as_view(), name="home"),
    url(r'(?P<org_id>\d+)/teacher/$', Org_TeachersView.as_view(), name="teacher"),
    # url(r'add_ask/$', Add_Course_Ask.as_view(), name="desc"),
    # url(r'add_ask/$', Add_Course_Ask.as_view(), name="teachers"),

]
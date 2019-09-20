from django.conf.urls import url, include
from .views import OrgView, Add_Course_Ask, Org_Homes

urlpatterns = [
    # 课程机构首页
    url(r'list/$', OrgView.as_view(), name="list"),
    # 用户咨询窗口
    url(r'add_ask/$', Add_Course_Ask.as_view(), name="add_ask"),

    url(r'(?P<org_id>\d+)/$', Org_Homes.as_view(), name="home"),
    # url(r'add_ask/$', Add_Course_Ask.as_view(), name="course"),
    # url(r'add_ask/$', Add_Course_Ask.as_view(), name="desc"),
    # url(r'add_ask/$', Add_Course_Ask.as_view(), name="teachers"),

]
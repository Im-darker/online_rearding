from django.core.paginator import PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
from .form import Add_UserAsk
from Share import PAGE_NUMS
from organizations.models import CourseOrg, City
from pure_pagination import Paginator
from django.http import JsonResponse


class Org_Homes(View):

    def get(self, request, org_id):

        return render(request, "org-detail-homepage.html")





class Add_Course_Ask(View):
    """添加用户咨询窗口"""
    def post(self, request):
        ask_form = Add_UserAsk(request.POST)

        if ask_form.is_valid():
            # 把数据写入到数据库保存
            ask_form.save(commit=True)

            return JsonResponse({
                "status": "success"
            })

        else:
            return JsonResponse({
                "status": "fail",
                "msg": "数据有误,添加失败",
            })


class OrgView(View):
    """课程机构"""
    def get(self, request):

        # 从数据库中取出数据
        org_all = CourseOrg.objects.all()

        city_all = City.objects.all()

        host_org = org_all.order_by("click_nums")[0:3]



        # 通过机构类型对课程机构进行筛选
        category = request.GET.get("ct", default='')

        if category:

            org_all = org_all.filter(category=category)

        # 通过城市对课程机构进行筛选
        city_id = request.GET.get("city", default='')

        if city_id:
            # 验证前端传过来的城市id是否为全数字的字符串
            if city_id.isdigit():
                org_all = org_all.filter(city_id=int(city_id))

        # 对课程机构进行排序
        sort = request.GET.get('sort', '')
        if sort == "students":
            org_all = org_all.order_by("-students")

        elif sort == "course_nums":

            org_all = org_all.order_by("course_nums")

        org_count = org_all.count()

        # 对课程机构数据分页处理
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(org_all, per_page=PAGE_NUMS, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html",
                      {"org_all": orgs,
                       "city_all": city_all,
                       'org_count': org_count,
                       'category': category,
                       'city_id': city_id,
                       'sort': sort,
                       'host_org': host_org,})















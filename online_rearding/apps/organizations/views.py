from django.core.paginator import PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View

from Share import PAGE_NUMS
from operations.models import UserFavorite
from .form import Add_UserAsk
from organizations.models import CourseOrg, City
from pure_pagination import Paginator
from django.http import JsonResponse


class OrgDescView(View):
    """机构课程列表"""
    def get(self, request, org_id, *args, **kwargs):
        # 传递一个变量给前端用于判断那个标签被选中
        status_desc = "desc"
        course_orgs = CourseOrg.objects.filter(id=int(org_id))[0]

        if course_orgs:
            course_orgs.click_nums += 1
            course_orgs.save()

            # 默认是显示收藏状态,用户没点收藏！
            has_fav = False
            if request.user.is_authenticated:
               if UserFavorite.objects.filter(user=request.user, fav_id=course_orgs.id, fav_type=2):
                   has_fav = True

            return render(request, "org-detail-desc.html", {
                "course_orgs": course_orgs,
                "status_desc": status_desc,
                "has_fav": has_fav,
            })


class OrgCourseView(View):
    """机构课程列表"""
    def get(self, request, org_id):
        # 传递一个变量给前端用于判断那个标签被选中
        status_course = "course"
        course_orgs = CourseOrg.objects.filter(id=int(org_id))[0]

        if course_orgs:
            course_orgs.click_nums += 1
            course_orgs.save()

            all_course = course_orgs.course_set.all()

            # 默认是显示收藏状态,用户没点收藏！
            has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=course_orgs.id, fav_type=2):
                    has_fav = True

            # 对机构课程数据分页处理
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            p = Paginator(all_course, per_page=PAGE_NUMS, request=request)

            course = p.page(page)

            return render(request, "org-detail-course.html", {
                "course_orgs": course_orgs,
                "all_course": course,
                "status_course": status_course,
                "has_fav": has_fav,
            })


class OrgTeachersView(View):
    """单个机构的老师列表"""
    def get(self, request, org_id):

        # 传递一个变量给前端用于判断那个标签被选中
        status_teacher = "teacher"
        course_orgs = CourseOrg.objects.filter(id=int(org_id))[0]

        if course_orgs:
            course_orgs.click_nums += 1
            course_orgs.save()

            all_teachers = course_orgs.teacher_set.all()

            # 默认是显示收藏状态,用户没点收藏！
            has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=course_orgs.id, fav_type=2):
                    has_fav = True

            # 对机构课程数据分页处理
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            p = Paginator(all_teachers, per_page=PAGE_NUMS, request=request)

            teacher = p.page(page)

            return render(request, "org-detail-teachers.html", {
                "course_orgs": course_orgs,
                "all_teachers": teacher,
                "status_teacher": status_teacher,
                 "has_fav": has_fav
            })


class OrgHomesView(View):
    """单个机构首页"""

    def get(self, request, org_id):

        # 传递一个变量给前端用于判断那个标签被选中
        status_home = "home"

        course_orgs = CourseOrg.objects.filter(id=int(org_id))[0]
        # course_orgs = CourseOrg.objects.get(id=int(org_id))

        if course_orgs:
            course_orgs.click_nums += 1
            course_orgs.save()

            all_teachers = course_orgs.teacher_set.all()[:1]
            all_courses = course_orgs.course_set.all()[:3]

            # 默认是显示收藏状态,用户没点收藏！
            has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=course_orgs.id, fav_type=2):
                    has_fav = True

            return render(request, "org-detail-homepage.html", {
                "course_orgs": course_orgs,
                "all_teachers": all_teachers,
                "all_courses": all_courses,
                "status_home": status_home,
                "has_fav": has_fav,
            })


class AddCourse_Ask(View):
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
    """课程机构列表"""
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

            org_all = org_all.order_by("-course_nums")

        org_count = org_all.count()

        # # 默认是显示收藏状态,用户没点收藏！
        # fav_status = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=host_org.id, fav_type=3):
        #         fav_status = True

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
                       'host_org': host_org,
                       # 'fav_status': fav_status
                       })















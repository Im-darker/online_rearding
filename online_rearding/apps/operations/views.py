
from django.views.generic import View
from django.http import JsonResponse
from courses.models import Course
from operations.form import AddFavform
from operations.models import UserFavorite
from organizations.models import Teacher, CourseOrg


class AddUserFavorite(View):
    """用户收藏, 取消收藏"""
    def post(self, request):

        # 验证用户是否登录
        if request.user.is_authenticated:

            user_fav_form = AddFavform(request.POST)

            if user_fav_form.is_valid():
                fav_id = user_fav_form.cleaned_data["fav_id"]
                fav_type = user_fav_form.cleaned_data["fav_type"]

                existence_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)

                # 如果有已存在记录，说明点过收藏
                if existence_records:
                    existence_records.delete()

                    # fav_type==1代表课程, 2代表讲师, 3代表机构
                    if fav_type == 1:
                        course = Course.objects.get(id=fav_type)
                        course.fav_nums -= 1
                        course.save()

                    elif fav_type == 2:
                        teacher = Teacher.objects.get(id=fav_type)
                        teacher.fav_nums -= 1
                        teacher.save()

                    elif fav_type == 3:
                        courseorg = CourseOrg.objects.get(id=fav_type)
                        courseorg.fav_nums -= 1
                        courseorg.save()

                    return JsonResponse({
                        "status": "success",
                        "msg": "收藏"

                    })

                else:
                    # 没有就说明没有点收藏, 保存记录！
                    user_fav = UserFavorite()
                    user_fav.fav_type = fav_type
                    user_fav.fav_id = fav_id
                    user_fav.user = request.user
                    user_fav.save()

                    return JsonResponse({
                        "status": "success",
                        "msg": "已收藏",
                    })

        else:
            return JsonResponse({
                "status": "fail",
                "msg": "用户未登录"
            })


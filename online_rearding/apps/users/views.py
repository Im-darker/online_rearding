import redis
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from utils.random_str import generate_random
from Share import SMS_CODE_TIME
from online_rearding.dev import yunpian_apikey, REDIS_HOST, REDIS_PORT
from users.form import RegistGitForm, SendSms, LoginForm, DynamicPostLogin
from users.models import UserCorrelation
from utils.random_str import generate_random
from utils.yunpian import send_single_sms


class RegisterView(View):
    """手机注册"""
    def get(self, request, *args, **kwargs):

        register_get_form = RegistGitForm()

        return render(request, "register.html", {"register_get_form": register_get_form})

    def post(self, request, *args, **kwargs):

        register_get_form = RegistGitForm(request.POST)

        if register_get_form.is_valid():

            mobile = register_get_form.cleaned_data["mobile"]
            password = register_get_form.cleaned_data["password"]
            # 新建用户
            user = UserCorrelation(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()

            # 状态保持
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            register_get_form = RegistGitForm(request.POST)
            return render(request, "register.html", {"register_get_form": register_get_form})


class DynamicLoginView(View):
    """验证码登录"""

    def post(self, request, *args, **kwargs):

        login_form = DynamicPostLogin(request.POST)

        # 解决动态登录页面出错时会跳到账号登录页面的问题, 后端定义一个变量传到前端来判定隐藏那个标签！
        DynamicLogin_login = True
        if login_form.is_valid():
            # 查询数据库, 验证这个手机号码是否第一次登录
            mobile = login_form.cleaned_data["mobile"]
            user = UserCorrelation.objects.filter(mobile=mobile).first()

            # 如果没有这个用户的记录, 那就新建这个用户数据
            if user is None:

                # 利用用户表名实力用户对象
                user = UserCorrelation(username=mobile)

                # 没有密码就使用随机生成的数字＋字符串＋特殊字符做密码
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()

            # 状态保持
            login(request, user)
            # 跳转首页
            return HttpResponseRedirect(reverse("index"))
        else:
            d_form = SendSms(request.POST)
            return render(request, "login.html", {"login_form": login_form, "DynamicLogin_login": DynamicLogin_login,
                                                  "d_form": d_form})


class SendSmsView(View):
    """短信验证码的发送"""
    def post(self, request, *args, **kwargs):
        send_sms_form = SendSms(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():

            mobile = send_sms_form.cleaned_data["mobile"]
            #随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(yunpian_apikey, code, mobile=mobile)
            if re_json["code"] == 0:
                re_dict["status"] = "success"
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
                r.setex("sms_code_{}".format(mobile), SMS_CODE_TIME, code)
            else:
                re_dict["msg"] = re_json["msg"]
        else:

            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class LogoutViews(View):
    """退出登陆"""
    def get(self, request):

        logout(request)

        response = redirect(reverse('login'))
        # 退出账号清除cookie中的username信息
        response.delete_cookie('username')
        return response


class LoginViews(View):
    """登陆"""

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            return HttpResponseRedirect(reverse("index"))
        # 实例化验证码的form表但
        login_form = SendSms()

        return render(request, "login.html", {"login_form": login_form})

    def post(self, request, *args, **kwargs):
        """通过用户名和密码进行登陆"""
        # 实例化表单对象
        login_form = LoginForm(request.POST)

        # 表单验证
        if login_form.is_valid():

            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            # if not username:
            #     return render(request, "login.html", {"msg": "请输入用户名"})
            #
            # if not password:
            #     return render(request, "login.html", {"msg": "请输入密码"})

            # 通过用户名和密码得到一个user用户对象,验证用户是否存在！
            user = authenticate(username=username, password=password)

            if user is not None:

                # 进行状态保持
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

            else:
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})

        else:
            return render(request, "login.html", {"login_form": login_form})













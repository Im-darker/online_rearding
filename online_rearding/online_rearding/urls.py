"""online_rearding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url, include
from django.urls import path
# 去除token验证
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

import xadmin
from django.views.static import serve

from online_rearding.dev import MEDIA_ROOT

from users.views import LoginViews, LogoutViews, RegisterView, SendSmsView, DynamicLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginViews.as_view(), name="login"),
    path('logout/', LogoutViews.as_view(), name="logout"),
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
    url(r'^captcha/', include('captcha.urls')),
    # 动态验证码登录
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    # 手机注册
    path('register/', RegisterView.as_view(), name="register"),

    # 配置上传图片的url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 机构相关页面
    url(r'^org/', include(('organizations.urls', "organizations"), namespace="org")),

]






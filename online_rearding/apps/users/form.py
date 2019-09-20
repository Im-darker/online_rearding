from django import forms
from captcha.fields import CaptchaField
import redis
from users.models import UserCorrelation
# class CaptchaTestForm(forms.Form):
#     # myfield = AnyOtherField()
#     captcha = CaptchaField()
from online_rearding.dev import REDIS_HOST, REDIS_PORT


class RegistGitForm(forms.Form):
    """进行注册验证"""
    captcha = CaptchaField()
    code = forms.CharField(required=True, max_length=4, min_length=3)
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    password = forms.CharField(required=True, min_length=8)

    def clean_mobile(self):
        # 验证mobile参数
        mobile = self.data.get("mobile")
        user = UserCorrelation.objects.filter(mobile=mobile).first()

        if user:
            raise forms.ValidationError("该手机号码已注册")
        return mobile

    def clean_code(self):
        # 验证码的验证
        mobile = self.data.get("mobile")
        code = self.data.get("code")

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        get_reids_code = r.get("sms_code_{}".format(mobile))

        # 判断验证码code的正确性
        if get_reids_code != code:
            raise forms.ValidationError("")

        # 返回数据集
        return code


class DynamicPostLogin(forms.Form):
    """进行验证码登录的验证"""
    code = forms.CharField(required=True, max_length=4, min_length=3)
    mobile = forms.CharField(required=True, min_length=11, max_length=11)

    def clean_code(self):
        # 可以针对性对字段进行验证,可以返回异常字段的信息！
        mobile = self.data.get("mobile")
        code = self.data.get("code")

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        get_reids_code = r.get("sms_code_{}".format(mobile))

        # 判断验证码code的正确性
        if get_reids_code != code:
            raise forms.ValidationError("验证码错误")

        # 返回数据集
        return self.cleaned_data




    # def clean(self):
    #     # 对redis的验证码进行验证
    #     mobile = self.cleaned_data["mobile"]
    #     code = self.cleaned_data["code"]
    #
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
    #     get_reids_code = r.get("sms_code_{}".format(mobile))
    #
    #     # 判断验证码code的正确性
    #     if get_reids_code != code:
    #         raise forms.ValidationError("验证码错误")
    #
    #     # 返回数据集
    #     return self.cleaned_data


class LoginForm(forms.Form):
    """用于用户登陆验证，解决views的冗余验证代码"""
    username = forms.CharField(required=True, min_length=3)
    password = forms.CharField(required=True, min_length=8)


class SendSms(forms.Form):
    """动态验证码发送"""
    captcha = CaptchaField()
    mobile = forms.CharField(required=True, min_length=11, max_length=11)

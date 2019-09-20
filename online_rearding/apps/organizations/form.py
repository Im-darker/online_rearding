import re

from django import forms

from operations.models import UserAsk


class Add_UserAsk(forms.ModelForm):

    mobile = forms.CharField(required=True, max_length=11, min_length=11)

    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]

    def clean_mobile(self):
        # 验证手机号码是否合法
        mobile = self.cleaned_data["mobile"]
        regular_mobile = "1[358]\d{9}$|^147]\d{8}$|^176\d{8}$"
        b = re.compile(regular_mobile)

        if b.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码不合法", code="Invalid number")
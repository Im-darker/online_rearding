from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UserCorrelation


class UserCorrelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserCorrelation, UserAdmin)


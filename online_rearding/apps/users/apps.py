from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    # 把后台USER改为中文用户
    verbose_name = u'用户'

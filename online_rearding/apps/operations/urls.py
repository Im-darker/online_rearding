from django.conf.urls import url
from .views import AddUserFavorite


urlpatterns = [
    # 用户收藏
    url(r'fav/$', AddUserFavorite.as_view(), name="fav"),



]
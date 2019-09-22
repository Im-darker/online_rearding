

from django import forms


from operations.models import UserFavorite


class AddFavform(forms.ModelForm):

    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]








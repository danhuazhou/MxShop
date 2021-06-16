from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator


class UserFavSerializer(serializers.ModelSerializer):
    # 用户设置为当前用户
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        # 联合唯一值，防止反复收藏，model中的unique_together也有相同功能
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已收藏"
            )
        ]
        fields = ("user", "goods", "id")

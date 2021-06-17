from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


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

from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # 自定义category，返回整个GoodsCategory的model的序列化，category为外键不定义返回只id
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"

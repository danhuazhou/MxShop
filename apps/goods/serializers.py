from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage


# 父类别嵌套子类别
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    # 自定义category，返回整个GoodsCategory的model的序列化，category为外键不定义返回只id
    category = CategorySerializer()
    # images 要与model GoodsImage中related_name相同
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"

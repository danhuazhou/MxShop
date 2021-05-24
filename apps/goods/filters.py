import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    # django2.x 使用field_name替代name
    price_min = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    # icontains忽略大小写 contain不忽略大小写
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']  # 为空好像也可以实现过滤

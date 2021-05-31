from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods, GoodsCategory
from .filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer


# Create your views here.

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     List all goods ,GoodsListView
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     # def get(self, request, format=None):
#     #     goods = Goods.objects.all()[:10]
#     #     goods_serializer = GoodsSerializer(goods, many=True)
#     #     return Response(goods_serializer.data)
#
#     def get(self, request, *args, **kwargs):
#         # list方法继承至mixins.ListModelMixin
#         return self.list(request, *args, **kwargs)
class StandardResultsSetPagination(PageNumberPagination):
    """
    重写page类，setting也可以调用原类型进行设置
    """
    page_size = 10  # 可以在地址栏中使用&page_size=20方式改变
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List all goods ,GoodsListView  分页搜索过滤排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    # authentication_classes = (TokenAuthentication,)
    # 使用drf自带SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter  # 使用自定义过滤类
    search_fields = ('^name', '=goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List:
         商品分类列表
    """
    # queryset = GoodsCategory.objects.all()
    queryset = GoodsCategory.objects.filter(category_type=1)  # 第一类标签
    serializer_class = CategorySerializer

    class Meta:
        model = Goods
        fields = "__all__"

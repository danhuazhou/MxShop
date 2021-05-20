from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Goods


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


class GoodsListView(generics.ListAPIView):
    """
    List all goods ,GoodsListView
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # REST_FRAMEWORK配置，setting中可不用配置了
    pagination_class = StandardResultsSetPagination

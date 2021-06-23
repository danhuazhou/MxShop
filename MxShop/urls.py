"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewset
from trade.views import ShoppingCartViewSet, OrderViewSet
import xadmin

router = DefaultRouter()

# goods的url
router.register(r'goods', GoodsListViewSet, basename='goods')

# category url
router.register(r'categorys', CategoryViewSet, basename="categorys")

router.register(r'codes', SmsCodeViewSet, basename="codes")

router.register(r'users', UserViewSet, basename="users")

router.register(r'userfavs', UserFavViewSet, basename='userfavs')

router.register(r'messages', LeavingMessageViewSet, basename='messages')

router.register(r'address', AddressViewset, basename='address')

router.register(r'shopcarts', ShoppingCartViewSet, basename='shopcarts')

router.register(r'orders', OrderViewSet, basename='orders')
# 绑定 被router.register替代
# good_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*$)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'goods/$', good_list, name='good-list'),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title="mxshop")),

    # drf自带认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt认证接口
    url(r'^login/', obtain_jwt_token),
]

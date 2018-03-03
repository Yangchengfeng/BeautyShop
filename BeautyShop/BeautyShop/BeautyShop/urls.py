"""BeautyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*-coding: utf-8 -*-

from django.conf.urls import url, include
# from django.contrib import admin
from extra_apps import xadmin
from goods.view_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet

router = DefaultRouter()

# goods - url
router.register(r'new-goods', GoodsListViewSet, base_name="new-goods")

# category - url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

# codes - smsurl
router.register(r'codes', SmsCodeViewset, base_name="codes")

# user - url
router.register(r'users', UserViewset, base_name="users")

# userfav - url
router.register(r'userfav', UserFavViewSet, base_name="fav")

# message - url
router.register(r'messages', LeavingMessageViewSet, base_name="messages")

# address - url
router.register(r'address', AddressViewSet, base_name="address")

# shopcart
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

# order
router.register(r'orders', OrderViewSet, base_name="orders")

# banner
router.register(r'banners', BannerViewset, base_name="banners")

# homepageIndex
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-jwt-token-auth/', obtain_jwt_token),

    url(r'^base-goods/$', GoodsListView.as_view(), name="base_good-list"),
    url(r'^goods/$', goods_list, name="good-list"),

    # thirdpart-login
    url('', include('social_django.urls', namespace='social')),

    # drf -- document
    url(r'docs/', include_docs_urls(title="BeautyGirls")), 

    url(r'^', include(router.urls)),
]

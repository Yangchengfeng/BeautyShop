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
from django.conf.urls import url, include
# from django.contrib import admin
from extra_apps import xadmin
from goods.view_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from goods.views import GoodsListViewSet

router = DefaultRouter()

router.register(r'new-goods', GoodsListViewSet, base_name="price_min")


goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^base-goods/$', GoodsListView.as_view(), name="base_good-list"),
    url(r'^goods/$', goods_list, name="good-list"),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/$', include_docs_urls(title="BeautyGirls")),
    url(r'^', include(router.urls)),
]

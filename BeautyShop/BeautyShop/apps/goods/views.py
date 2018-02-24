# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from .serializers import GoodsSerializer, GoodsCategorySerializer
from .models import Goods, GoodsCategory
from .filters import GoodsFilter

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_size_query_param = "p"
    max_page_size = 4

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    分页 过滤(搜索、排序)
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (TokenAuthentication,)

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price=int(price_min))
    #     return queryset

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # queryset = GoodsCategory.objects.all()
    queryset = GoodsCategory.objects.filter(category_type=2)
    serializer_class = GoodsCategorySerializer
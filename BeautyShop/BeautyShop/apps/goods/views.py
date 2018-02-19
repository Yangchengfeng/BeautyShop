# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import GoodsSerializer
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .filters import GoodsFilter

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_size_query_param = "p"
    max_page_size = 4

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price=int(price_min))
    #     return queryset

    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Goods

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_size_query_param = "p"
    max_page_size = 4

class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
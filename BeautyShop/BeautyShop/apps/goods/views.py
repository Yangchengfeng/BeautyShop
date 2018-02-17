# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Goods

# Create your views here.
class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

import django_filters

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet): 
    min_price = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price']
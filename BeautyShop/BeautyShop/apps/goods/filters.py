import django_filters
from django.db.models import Q

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet): 
    min_price = django_filters.NumberFilter(name="shop_price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(name="shop_price", lookup_expr="lte")
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'is_hot', 'is_new',]
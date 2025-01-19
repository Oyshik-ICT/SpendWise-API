import django_filters
from .models import Catagoery


class CatagoeryFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
    created_at_gt = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gt')
    created_at_lt = django_filters.DateFilter(field_name='created_at', lookup_expr='date__lt')

    class Meta:
        model = Catagoery
        fields = []  
from django_filters.widgets import RangeWidget
from django_filters import rest_framework as filters, DateFromToRangeFilter

import django_filters


class PhotoFilter(filters.FilterSet):

    date_range = DateFromToRangeFilter(
        label='Введите период, за который вывести фото',
        field_name='date',
        widget=RangeWidget(attrs={'type': 'date'}),
    )

    geo_location = django_filters.CharFilter(field_name='geo_location',
                                             label='Введите локацию полностью или частично',
                                             method='filter_location'
                                             )

    people_names = django_filters.CharFilter(field_name='people_names',
                                             label='Введите имя',
                                             method='filter_names'
                                             )

    def filter_location(self, queryset, name, value):
        return queryset.filter(geo_location__startswith=value)

    def filter_names(self, queryset, name, value):
        return queryset.filter(people_names__contains=[value])

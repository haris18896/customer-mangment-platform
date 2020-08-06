import django_filters
from django_filters import DateFilter, CharFilter
from . models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")  #cusotme fields,'gte' means greater then or equal to
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")    #custom field, 'lte' means less then or equal to
    note = CharFilter(field_name="note", lookup_expr="icontains")    #icontains means ignore case sensitvity


    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created', ]
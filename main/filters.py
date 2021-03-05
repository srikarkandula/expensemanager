import django_filters 

from .models import *

class ExpensesFilter(django_filters.FilterSet):
    class Meta:
        model = Expenses
        fields = '__all__'




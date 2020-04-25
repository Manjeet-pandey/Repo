import django_filters
from .models import ProductRegister


class ProductFilter(django_filters.FilterSet):
    CHOICES=(
        ('a','A-Z'),
         ('d','Z-A')
        )
    ordering=django_filters.ChoiceFilter(label='order',choices=CHOICES, method='sorting_method')

    def sorting_method(self,queryset,name,value):
        expression= 'product_Name'if value=='a' else '-product_Name'
        return queryset.order_by(expression)

    class Meta:
        model=ProductRegister
        fields={
            'product_Name':['icontains'],
            'productMaterialItemCode':['icontains']
            }
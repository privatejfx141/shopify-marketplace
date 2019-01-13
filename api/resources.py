# api/resources.py

from tastypie.resources import ModelResource
from api.models import Product
from tastypie.authorization import Authorization

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()
        fields = ['title', 'price', 'inventory_count']

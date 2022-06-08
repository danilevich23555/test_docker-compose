from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', ]
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    serializer_class = StockSerializer
    def get_queryset(self):
        queryset = Stock.objects.all()
        product = self.request.query_params.get('products')
        if product is not None:
            queryset = Stock.objects.filter(products=product)
        return queryset
    # при необходимости добавьте параметры фильтрации

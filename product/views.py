from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['DELETE'])
    def delete_product(self, request, pk=None):
        product = self.get_object()
        product.delete()
        return Response({'message': 'Product deleted successfully'})

    @action(detail=True, methods=['PUT'])
    def update_product(self, request, pk=None):
        product = self.get_object()
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

from rest_framework import viewsets
from .models import Product, ProductLove
from .serializers import ProductLoveSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductLove.objects.all()
    serializer_class = ProductLoveSerializer

    @action(detail=True, methods=['post'], url_path='love')
    def love(self, request, pk=None):
        product = self.get_object()
        user = request.user

        love, created = ProductLove.objects.get_or_create(user=user, product=product)

        if not created:
            love.delete()
            return Response({'message': 'Love removed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Love added'}, status=status.HTTP_201_CREATED)


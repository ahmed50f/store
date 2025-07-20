from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Rating, Order, CartItem, Cart
from .serializers import (
    CategorySerializer, ProductSerializer, RatingSerializer,
    OrderSerializer, CartItemSerializer, CartSerializer
)
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, order_date=now())  # Assuming Order has a 'user' field


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        cart, _ = Cart.objects.get_or_create(user=request.user)

        product = get_object_or_404(Product, id=product_id)

        try:
            item = CartItem.objects.get(cart=cart, product=product)
            item.quantity += quantity
            item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        return Response({'detail': 'تمت إضافة المنتج إلى السلة.'}, status=status.HTTP_200_OK)


class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        item.delete()
        return Response({'detail': 'تمت إزالة المنتج من السلة.'})

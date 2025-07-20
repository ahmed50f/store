from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, RatingViewSet, OrderViewSet, CartView, AddToCartView, RemoveFromCartView   



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]


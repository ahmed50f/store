from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, RatingViewSet, OrderViewSet



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls


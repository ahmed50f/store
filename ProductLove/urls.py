from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'love', ProductViewSet, basename='productlove')

urlpatterns = [
    path('', include(router.urls)),
]
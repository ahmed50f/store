from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # هذا المسار يسمح بالوصول إلى /api/users/   
]


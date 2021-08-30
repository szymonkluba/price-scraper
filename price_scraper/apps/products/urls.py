from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'', views.CategoryViewSet)

app_name = 'products'
urlpatterns = [
    path('', include((router.urls, app_name), namespace=app_name))
]
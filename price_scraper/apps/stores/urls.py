from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StoreViewSet

router = DefaultRouter()
router.register('', StoreViewSet)

app_name = 'stores'
urlpatterns = [
    path('', include((router.urls, app_name), namespace=app_name))
]
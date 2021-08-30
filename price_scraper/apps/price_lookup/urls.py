from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PricesViewSet

router = DefaultRouter()
router.register(r'prices', PricesViewSet)

app_name = 'prices'
urlpatterns = router.urls

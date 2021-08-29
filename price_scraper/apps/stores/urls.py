from django.urls import path, include
from rest_framework.routers import DefaultRouter

from price_scraper.apps.stores.views import StoreViewSet

router = DefaultRouter()
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
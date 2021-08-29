from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavouritesViewSet

router = DefaultRouter()
router.register(r'favs', FavouritesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
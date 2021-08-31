from rest_framework.routers import DefaultRouter

from .views import FavouritesViewSet

router = DefaultRouter()
router.register(r'favourites', FavouritesViewSet, basename="favourites")

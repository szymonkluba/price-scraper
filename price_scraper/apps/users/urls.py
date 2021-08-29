from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavouritesViewSet

router = DefaultRouter()
router.register(r'favs', FavouritesViewSet)

app_name = "users"
urlpatterns = [
    path('', include((router.urls, app_name), namespace=app_name))
]
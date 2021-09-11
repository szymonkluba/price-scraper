"""price_scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.price_lookup.urls import router as prices_router
from apps.products.urls import router as products_router
from apps.stores.urls import router as stores_router
from apps.users.urls import router as users_router
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(users_router.registry)
router.registry.extend(stores_router.registry)
router.registry.extend(products_router.registry)
router.registry.extend(prices_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url('', include(router.urls))
]

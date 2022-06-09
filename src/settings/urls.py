from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.addresses.api.views import AddressAPIViewSet
from apps.users.api.views import TelegramUserAPIViewSet


router = SimpleRouter()
router.register('addresses-set', AddressAPIViewSet)
router.register('users', TelegramUserAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/addresses/', include('apps.addresses.api.urls')),
    path('api/v1/products/', include('apps.products.api.urls')),
]

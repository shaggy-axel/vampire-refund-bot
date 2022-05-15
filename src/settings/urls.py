from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.users.api.views import TelegramUserAPIViewSet


router = SimpleRouter()
router.register('users', TelegramUserAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

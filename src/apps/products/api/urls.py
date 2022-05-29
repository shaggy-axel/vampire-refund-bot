from django.urls import path

from apps.products.api.views import ProductAPIView


urlpatterns = [
    path('', ProductAPIView.as_view()),
]

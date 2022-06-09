
from django.urls import path

from apps.addresses.api.views import GetAddressAPI, GetUsedAddressesAPI


urlpatterns = [
    path('first/', GetAddressAPI.as_view()),
    path('used/', GetUsedAddressesAPI.as_view()),
]

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    shop_name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    delivery_date = models.DateTimeField(null=True, blank=True)
    address = models.OneToOneField(
        'addresses.Address', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'products'

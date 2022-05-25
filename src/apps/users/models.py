from datetime import datetime
from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    current_address = models.ForeignKey(
        'addresses.Address', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'telegram_users'
        verbose_name = 'Пользователь telegram'
        verbose_name_plural = 'Пользователи telegram'


def update_address(sender, instance, created: bool, **kwargs):
    if created:
        return

    if instance.current_address:
        address = instance.current_address
        address.status = 'using'
        address.used_by = instance
        address.used_at = datetime.now()
        address.save()


models.signals.post_save.connect(update_address, TelegramUser)

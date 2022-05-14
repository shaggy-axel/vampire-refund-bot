from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    current_address = models.ForeignKey(
        'addresses.Address', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'telegram_users'
        verbose_name = 'Пользователь telegram'
        verbose_name_plural = 'Пользователи telegram'

from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=128)
    line_1 = models.CharField(max_length=128)
    line_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.PositiveIntegerField()
    phone = models.CharField(max_length=40)

    ADDRESS_STATUS_CHOICES = (
        ('used', 'Used'),
        ('notused', 'Not Used'),
        ('hold', 'Hold'),
    )

    status = models.CharField(
        max_length=20, choices=ADDRESS_STATUS_CHOICES,
        default=ADDRESS_STATUS_CHOICES[1][0]
    )
    used_by = models.ForeignKey(
        'users.TelegramUser', on_delete=models.SET_NULL,
        null=True, blank=True
    )
    used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'addresses'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        unique_together = (
            'name', 'line_1', 'line_2', 'city',
            'state', 'zip_code', 'phone'
        )


def update_user(sender, instance, created: bool, **kwargs):
    if created:
        return

    if instance.used_by:
        user = instance.used_by
        user.current_address = None
        user.save()


models.signals.post_save.connect(update_user, Address)

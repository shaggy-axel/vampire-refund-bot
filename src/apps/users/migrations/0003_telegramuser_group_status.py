# Generated by Django 4.0.4 on 2022-06-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_telegramuser_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='group_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

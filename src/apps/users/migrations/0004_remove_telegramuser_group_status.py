# Generated by Django 4.0.4 on 2022-06-05 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_telegramuser_group_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='group_status',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]

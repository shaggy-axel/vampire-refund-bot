# Generated by Django 4.0.6 on 2022-07-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='track_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

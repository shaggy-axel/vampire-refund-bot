# Generated by Django 4.0.4 on 2022-05-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_alter_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='status',
            field=models.CharField(choices=[('notused', 'Not Used'), ('using', 'Using'), ('used', 'Used'), ('hold', 'Hold')], default='notused', max_length=20),
        ),
    ]

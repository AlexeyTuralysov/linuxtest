# Generated by Django 5.0.1 on 2024-02-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.2 on 2020-12-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0013_ship_prices_last_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="shiporder",
            name="payment_taken",
            field=models.BooleanField(default=False),
        ),
    ]

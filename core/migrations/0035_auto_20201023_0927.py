# Generated by Django 3.1.2 on 2020-10-23 09:27

import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0034_auto_20201023_0854")]

    operations = [
        migrations.AddField(
            model_name="transferlog",
            name="count",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transferlog",
            name="total",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2, default_currency="EEI", max_digits=14, default=0
            ),
        ),
        migrations.AddField(
            model_name="transferlog",
            name="total_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("EEI", "Eve Echoes ISK")],
                default="EEI",
                editable=False,
                max_length=3,
            ),
        ),
    ]

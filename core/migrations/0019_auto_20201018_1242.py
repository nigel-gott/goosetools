# Generated by Django 3.1.2 on 2020-10-18 12:42

import djmoney.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0018_auto_20201017_1756")]

    operations = [
        migrations.AddField(
            model_name="inventoryitem",
            name="total_fees",
            field=djmoney.models.fields.MoneyField(
                blank=True,
                decimal_places=2,
                default_currency="EEI",
                max_digits=14,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="total_fees_currency",
            field=djmoney.models.fields.CurrencyField(
                choices=[("EEI", "Eve Echoes ISK")],
                default="EEI",
                editable=False,
                max_length=3,
            ),
        ),
    ]

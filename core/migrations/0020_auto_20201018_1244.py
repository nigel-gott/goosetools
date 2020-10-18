# Generated by Django 3.1.2 on 2020-10-18 12:44

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20201018_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='total_fees',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='EEI', max_digits=14),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='total_profit',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='EEI', max_digits=14),
        ),
    ]

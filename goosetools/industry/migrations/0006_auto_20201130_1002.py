# Generated by Django 3.1.2 on 2020-11-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0005_ship_free"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shiporder",
            name="payment_method",
            field=models.TextField(
                choices=[("eggs", "eggs"), ("isk", "isk"), ("free", "free")]
            ),
        ),
    ]
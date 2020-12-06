# Generated by Django 3.1.2 on 2020-12-02 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0006_auto_20201130_1002"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderLimitGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("days_between_orders", models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="shiporder",
            name="order_limit_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="industry.orderlimitgroup",
            ),
        ),
    ]
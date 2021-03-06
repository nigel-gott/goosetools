# Generated by Django 3.1.2 on 2020-11-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0003_auto_20201128_1511"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Ship",
                    fields=[
                        ("name", models.TextField(primary_key=True, serialize=False)),
                        ("tech_level", models.PositiveIntegerField()),
                    ],
                ),
                migrations.AlterField(
                    model_name="shiporder",
                    name="ship",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="industry.ship"
                    ),
                ),
            ]
        )
    ]

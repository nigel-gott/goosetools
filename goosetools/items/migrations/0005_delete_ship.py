# Generated by Django 3.1.2 on 2020-11-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0004_auto_20201129_1049"),
        ("items", "0004_ship"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable(
                    name="Ship",
                    table="industry_ship",
                ),
            ],
            state_operations=[
                migrations.DeleteModel(
                    name="Ship",
                ),
            ],
        )
    ]

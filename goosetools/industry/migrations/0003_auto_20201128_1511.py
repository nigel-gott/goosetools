# Generated by Django 3.1.2 on 2020-11-28 15:11

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0004_ship"),
        ("industry", "0002_add_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="shiporder",
            name="contract_made",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="shiporder",
            name="uid",
            field=models.TextField(default="MISSING", unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="shiporder",
            name="ship",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="items.ship"
            ),
        ),
        migrations.AlterField(
            model_name="shiporder",
            name="state",
            field=django_fsm.FSMField(default="not_started", max_length=50),
        ),
    ]

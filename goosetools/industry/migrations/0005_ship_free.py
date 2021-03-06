# Generated by Django 3.1.2 on 2020-11-29 23:30

from django.db import migrations, models

# pylint: disable=unused-argument
def make_t6_and_below_ships_free(apps, schema_editor):
    Ship = apps.get_model("industry", "Ship")
    for person in Ship.objects.all():
        person.free = person.tech_level <= 6
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ("industry", "0004_auto_20201129_1049"),
        ("items", "0005_delete_ship"),
    ]

    operations = [
        migrations.AddField(
            model_name="ship",
            name="free",
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-14 09:28

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0070_fleet_loot_was_stolen"),
    ]

    operations = [
        migrations.AddField(
            model_name="fleet",
            name="loot_type",
            field=models.TextField(choices=[('Master Looter', 'Master Looter'), ('Free For All', 'Free For All')], default='Master Looter'),
        ),
    ]

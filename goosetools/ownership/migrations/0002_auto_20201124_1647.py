# Generated by Django 3.1.2 on 2020-11-24 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fleets", "0001_initial"),
        ("ownership", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transferlog",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="lootshare",
            name="character",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.character"
            ),
        ),
        migrations.AddField(
            model_name="lootshare",
            name="loot_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ownership.lootgroup"
            ),
        ),
        migrations.AddField(
            model_name="lootgroup",
            name="bucket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ownership.lootbucket"
            ),
        ),
        migrations.AddField(
            model_name="lootgroup",
            name="fleet_anom",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fleets.fleetanom",
            ),
        ),
        migrations.AddField(
            model_name="lootgroup",
            name="killmail",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fleets.killmail",
            ),
        ),
        migrations.AddField(
            model_name="lootbucket",
            name="fleet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fleets.fleet"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="lootshare",
            unique_together={("character", "loot_group")},
        ),
    ]

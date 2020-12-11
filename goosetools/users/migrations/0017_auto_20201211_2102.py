# Generated by Django 3.1.2 on 2020-12-11 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_discordguild_member_role_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="corp",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.corp",
            ),
        ),
        migrations.CreateModel(
            name="CorpApplication",
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
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("unapproved", "unapproved"),
                            ("approved", "approved"),
                            ("rejected", "rejected"),
                        ],
                        default="unapproved",
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.character",
                    ),
                ),
                (
                    "corp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.corp"
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_auto_20201210_1641"),
    ]

    operations = [
        migrations.AddField(
            model_name="discorduser",
            name="nick",
            field=models.TextField(blank=True, null=True),
        ),
    ]

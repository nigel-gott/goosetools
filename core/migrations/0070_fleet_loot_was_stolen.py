# Generated by Django 3.1.2 on 2020-11-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20201104_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='loot_was_stolen',
            field=models.BooleanField(default=False),
        ),
    ]
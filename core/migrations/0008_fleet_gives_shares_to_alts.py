# Generated by Django 3.1.2 on 2020-10-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201016_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='gives_shares_to_alts',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20201022_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggtransaction',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='isktransaction',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]

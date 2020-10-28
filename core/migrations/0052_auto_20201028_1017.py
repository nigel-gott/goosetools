# Generated by Django 3.1.2 on 2020-10-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_anomtype_item_filter_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anomtype',
            name='item_filter_groups',
        ),
        migrations.AddField(
            model_name='itemfiltergroup',
            name='anom_type',
            field=models.TextField(blank=True, choices=[('PvP Roam', 'PvP Roam'), ('PvP Gatecamp', 'PvP Gatecamp'), ('Deadspace', 'Deadspace'), ('Scout', 'Scout'), ('Inquisitor', 'Inquisitor'), ('Condensed Belt', 'Condensed Belt'), ('Condensed Cluster', 'Condensed Cluster')], null=True),
        ),
        migrations.AddField(
            model_name='itemfiltergroup',
            name='faction',
            field=models.TextField(blank=True, choices=[('Guristas', 'Guritas'), ('Angel', 'Angel'), ('Blood', 'Blood'), ('Sansha', 'Sansha'), ('Serpentis', 'Serpentis'), ('Asteroids', 'Asteroids'), ('PvP', 'PvP')], null=True),
        ),
        migrations.AddField(
            model_name='itemfiltergroup',
            name='max_level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemfiltergroup',
            name='min_level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ItemFilterLink',
        ),
    ]

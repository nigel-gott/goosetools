# Generated by Django 3.1.2 on 2020-10-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201017_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomtype',
            name='faction',
            field=models.TextField(choices=[('Guristas', 'Guritas'), ('Angel', 'Angel'), ('Blood', 'Blood'), ('Sansha', 'Sansha'), ('Serpentis', 'Serpentis'), ('Asteroids', 'Asteroids')], default='Guristas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anomtype',
            name='type',
            field=models.TextField(choices=[('Deadspace', 'Deadspace'), ('Scout', 'Scout'), ('Inquisitor', 'Inquisitor'), ('Condensed Belt', 'Condensed Belt'), ('Condensed Cluster', 'Condensed Cluster')]),
        ),
    ]
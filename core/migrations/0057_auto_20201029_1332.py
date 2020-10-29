# Generated by Django 3.1.2 on 2020-10-29 13:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20201029_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='StackedInventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 13, 32, 45, 396652, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.contract'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='loot_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.lootgroup'),
        ),
        migrations.AlterField(
            model_name='solditem',
            name='transfer_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.transferlog'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.stackedinventoryitem'),
        ),
    ]

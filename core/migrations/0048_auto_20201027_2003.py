# Generated by Django 3.1.2 on 2020-10-27 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20201027_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemFilterGroup',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_type', models.TextField(choices=[('exclude', 'exclude'), ('require', 'require'), ('suggest', 'suggest')])),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.itemfiltergroup')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('item_sub_sub_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itemsubsubtype')),
                ('item_sub_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itemsubtype')),
                ('item_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itemtype')),
            ],
        ),
        migrations.AddField(
            model_name='anomtype',
            name='item_filter_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.itemfiltergroup'),
        ),
    ]
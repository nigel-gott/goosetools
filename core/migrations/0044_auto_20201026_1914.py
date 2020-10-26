# Generated by Django 3.1.2 on 2020-10-26 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20201026_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_contracts', to='core.character')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system')),
                ('to_char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.character')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contract'),
        ),
    ]

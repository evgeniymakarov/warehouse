# Generated by Django 5.0.2 on 2024-02-08 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_units_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='units',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.units'),
        ),
    ]
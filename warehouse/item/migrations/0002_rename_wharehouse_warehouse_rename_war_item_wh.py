# Generated by Django 5.0.2 on 2024-02-08 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wharehouse',
            new_name='Warehouse',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='war',
            new_name='wh',
        ),
    ]
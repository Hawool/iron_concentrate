# Generated by Django 3.2.9 on 2021-11-23 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iron_concentrate', '0002_auto_20211122_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ironconcentrate',
            old_name='aluminium',
            new_name='aluminum',
        ),
    ]

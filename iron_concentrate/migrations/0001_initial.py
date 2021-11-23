# Generated by Django 3.2.9 on 2021-11-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IronConcentrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('iron', models.DecimalField(decimal_places=5, max_digits=5)),
                ('silicon', models.DecimalField(decimal_places=5, max_digits=5)),
                ('aluminium', models.DecimalField(decimal_places=5, max_digits=5)),
                ('calcium', models.DecimalField(decimal_places=5, max_digits=5)),
                ('sulfur', models.DecimalField(decimal_places=5, max_digits=5)),
                ('month', models.IntegerField(choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сенябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')])),
            ],
            options={
                'verbose_name': 'IronConcentrate',
                'verbose_name_plural': 'IronConcentrates',
            },
        ),
    ]
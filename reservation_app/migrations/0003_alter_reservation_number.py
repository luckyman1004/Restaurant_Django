# Generated by Django 4.1.3 on 2022-11-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0002_alter_reservation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], max_length=1, verbose_name='تعداد نفرات رزروی'),
        ),
    ]

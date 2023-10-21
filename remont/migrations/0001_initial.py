# Generated by Django 4.2.6 on 2023-10-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_of_one_room', models.IntegerField(default=200000)),
            ],
        ),
        migrations.CreateModel(
            name='PriceSquareArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_remont', models.CharField(max_length=50)),
                ('price_square_meter', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remont', '0002_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleRemont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='PriceRooms',
        ),
    ]

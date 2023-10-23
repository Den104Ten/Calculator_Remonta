from django.db import models

class PriceSquareArea(models.Model):
    # Стоимость на метр квадратный
    # Разные типы ремонтов имеют разную стоимость на метр квадратный
    type_of_remont = models.CharField(max_length=50)
    price_square_meter = models.IntegerField()
    mnozhitel = models.FloatField(default=1)

    class Meta:
        verbose_name = "Тип ремонта. Стоимость за м2"
        verbose_name_plural = "Тип ремонта. Стоимость за м2"


class CountToilets(models.Model):
    count = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        verbose_name = "Количество санузлов"
        verbose_name_plural = "Количество санузлов"

# Стиль ремонта
class StyleRemont(models.Model):
    style = models.CharField(max_length=70)

    class Meta:
        verbose_name = "Стиль ремонта"
        verbose_name_plural = "Стиль ремонта"

# Отталкиваюсь от новостройки или вторички потом уже от типа помещения (Квартира, Офис, Коттедж)
class TypeBuilding(models.Model):
    building = models.CharField(max_length=50)
    # Множитель. Зависит от типа здания (Новостройка, Вторичка)
    price = models.FloatField()

    class Meta:
        verbose_name = r"Тип дома. Новостройка\вторичка"
        verbose_name_plural = r"Тип дома. Новостройка\вторичка"

class TypeHouse(models.Model):
    house = models.CharField(max_length=50)
    price = models.FloatField()

    class Meta:
        verbose_name = "Тип помещения. Квартира, Коттедж, Офис"
        verbose_name_plural = "Тип помещения. Квартира, Коттедж, Офис"







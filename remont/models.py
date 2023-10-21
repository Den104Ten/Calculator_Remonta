from django.db import models

class PriceSquareArea(models.Model):
    # Стоимость на метр квадратный
    # Разные типы ремонтов имеют разную стоимость на метр квадратный
    type_of_remont = models.CharField(max_length=50)
    price_square_meter = models.IntegerField()


# Материалы которые будут использоваться
class Materials(models.Model):
    material = models.CharField(max_length=50)
    price = models.IntegerField()


# Стиль ремонта
class StyleRemont(models.Model):
    style = models.CharField(max_length=70)




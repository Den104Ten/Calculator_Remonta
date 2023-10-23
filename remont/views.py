from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from .models import PriceSquareArea, StyleRemont, TypeBuilding, TypeHouse, CountToilets
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class RemontHomeView(View):

    def get(self, request):
        remonts = PriceSquareArea.objects.all()
        styles = StyleRemont.objects.all()
        buildings = TypeBuilding.objects.all()
        houses = TypeHouse.objects.all()
        toilets = CountToilets.objects.all()
        data = {'remonts': remonts,
                'styles': styles,
                'buildings': buildings,
                'houses': houses,
                'toilets': toilets,
                }
        return render(request, 'remont/home.html', context=data)

    def post(self, request):
        type_remont = get_object_or_404(PriceSquareArea, type_of_remont=request.POST['type_remont'])
        amount_of_square_meters = request.POST['numberInput']
        type_building = get_object_or_404(TypeBuilding, building=request.POST['buildings'])
        type_house = get_object_or_404(TypeHouse, house=request.POST['houses'])
        count_toilets = get_object_or_404(CountToilets, count=request.POST['toilets'])

        # Пока что ни на что не влияет. Сделать чтобы влияло на стоимость.
        style_of_remont = request.POST['style_remont']

        final_price = (((int(type_remont.price_square_meter) * int(amount_of_square_meters)) * float(type_building.price)) * float(type_house.price))
        # Итоговая цена за метр квадратный с учетом всех факторов.
        final_price_square_meter = int((type_remont.price_square_meter) * float(type_building.price)) * float(type_house.price)

        # Примерное время работы
        final_work_time = (int(amount_of_square_meters) * float(type_remont.mnozhitel)) // 20

        # Тип ремонта. Площадь ремонта. Стиль ремонта. Финальная цена.
        data = {'type_remont': type_remont,
                'final_price_square_meter': final_price_square_meter,
                'amount_of_square_meters': amount_of_square_meters,
                'style_of_remont': style_of_remont,
                'final_price': int(final_price) + int(count_toilets.price),
                'final_work_time': final_work_time,
                'count_toilets': count_toilets,
                }
        return render(request, 'remont/calculator_result.html', context=data)


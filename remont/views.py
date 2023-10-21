from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import PriceSquareArea, StyleRemont, Materials
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class RemontHomeView(View):

    def get(self, request):
        remonts = PriceSquareArea.objects.all()
        styles = StyleRemont.objects.all()
        materials_all = Materials.objects.all()
        data = {'remonts': remonts,
                'styles': styles,
                'materials_all': materials_all,
                }
        return render(request, 'remont/home.html', context=data)

    def post(self, request):
        type_remont = request.POST['type_remont']
        amount_of_square_meters = request.POST['numberInput']
        style_of_remont = request.POST['style_remont']
        selected_materials = request.POST.getlist('materials_all')
        materials_list = list(selected_materials)
        number_of_material = request.POST.getlist('numberOfMaterial')

        # Получение стоимости за метр квадратный материала
        list_of_price_materials = []
        for i in materials_list:
            material = get_object_or_404(Materials, material=i)
            list_of_price_materials.append(material.price)

        # Расчет суммы количества материалов и цены материала
        list_of_final_price = []
        pk = 0
        for j in number_of_material:
            list_of_final_price.append(int(j) * int(list_of_price_materials[pk]))
            pk += 1

        # Конечный результат стоимости. Также красивая распаковка словаря.
        final_dict_of_materials = dict(zip(materials_list, list_of_final_price))
        formatted_string = ", ".join("{}: {}".format(key, value) for key, value in final_dict_of_materials.items())


        result_of_type = get_object_or_404(PriceSquareArea, type_of_remont=type_remont)
        # Вычисление стоимости по метра и типу ремонта. И вычисление финальной стоимости вместе с материалами.
        price_materials = sum(map(int, list_of_final_price))
        final_price = (int(result_of_type.price_square_meter) * int(amount_of_square_meters)) + price_materials

        # Тип ремонта. Площадь ремонта. Стиль ремонта. Финальная цена.
        # Материалы. Количество материалов. Конечный список материалов
        data = {'result_of_type': result_of_type,
                'amount_of_square_meters': amount_of_square_meters,
                'style_of_remont': style_of_remont,
                'final_price': final_price,
                'materials': ', '.join(materials_list),
                'number_of_material': number_of_material,
                'final_list_of_materials': formatted_string,
                }
        return render(request, 'remont/calculator_result.html', context=data)



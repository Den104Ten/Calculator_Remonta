from django.urls import path
from .views import *


urlpatterns = [
    path('home/', RemontHomeView.as_view(), name='home'),
    #path('calculator_result', CalculatorResult.as_view(), name='calculator_result')
]









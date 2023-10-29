from django.urls import path
from .views import *


urlpatterns = [
    path('home/', RemontHomeView.as_view(), name='home'),
    path('base/', BaseView.as_view(), name='base')
]










from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/ph',views.phView,name='dashboardPh'),
    path('dashboard/gas',views.gasView,name='dashboardGas'),
    path('dashboard/sound',views.soundView,name='dashboardSound'),

    path('api/data/ph',views.getPhData,name="apiPh"),
    path('api/data/gas',views.getGasData,name="apiGas"),
    path('api/data/sound',views.getSoundData,name="apiSound"),

]

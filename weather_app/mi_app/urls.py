from django.urls import path
from . import views

urlpatterns = [
    path('forecast/', views.forecast_weather_view, name='forecast_weather'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Nueva ruta para el dashboard

]

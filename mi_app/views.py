from django.shortcuts import render
from .models import ForecastWeather
from django.http import HttpResponse
from mi_app.dbutils import get_forecast_data 
import plotly.express as px


def home_view(request):
    return render(request, 'mi_app/home.html')

def forecast_weather_view(request):
    # Obtiene los datos desde la base de datos SQL Server
    forecast_df = get_forecast_data()

    # Convierte el DataFrame en una lista de diccionarios para pasarlo a la plantilla
    forecasts = forecast_df.to_dict('records')

    return render(request, 'mi_app/forecast.html', {'forecasts': forecasts})

def dashboard_view(request):
    # Obtener datos del forecast
    forecast_df = get_forecast_data()

    # Crear gráfico interactivo con Plotly
    fig = px.line(forecast_df, x='date', y='temperature', title='Temperatura vs Fecha')
    fig.add_scatter(x=forecast_df['date'], y=forecast_df['humidity'], mode='lines+markers', name='Humedad')

    # Convertir el gráfico a HTML
    graph = fig.to_html(full_html=False)

    # Renderizar la página con el gráfico
    return render(request, 'mi_app/dashboard.html', {'graph': graph})




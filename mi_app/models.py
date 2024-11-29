from django.db import models

class ForecastWeather(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"Forecast on {self.date}"

class CurrentWeather(models.Model):
    date = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"Current Weather on {self.date}"

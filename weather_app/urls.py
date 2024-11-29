from django.contrib import admin
from django.urls import path, include
from mi_app.views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # Página principal
    path('admin/', admin.site.urls),
    path('weather/', include('mi_app.urls')),
]

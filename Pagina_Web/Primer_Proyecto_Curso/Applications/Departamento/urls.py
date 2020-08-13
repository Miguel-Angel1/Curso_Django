"""
Sección 4:Sección 4: Entorno de trabajo optimo en Django
4.5 Urls de aplicaciones
"""
from django.urls import path

from . import views

urlpatterns = [
    path('new-depa/', views.NewDepartamento.as_view(), name="new_depa"),
]

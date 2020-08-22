"""
Sección 4:Sección 4: Entorno de trabajo optimo en Django
4.5: Urls de aplicaciones
-> Importación de las librerias re_path e inlcude
-> Incluir las url de la aplicacion Departamento:
   re_path('', include('Applications.Departamento.urls')),

"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('Applications.Departamento.urls')),
    # 5.2.5 Busqueda de urls en la app Home_Pruebas
    re_path('', include('Applications.Home_Pruebas.urls')),
    re_path('', include('Applications.Empleado.urls')),

]

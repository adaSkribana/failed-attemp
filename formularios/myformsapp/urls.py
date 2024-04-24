from django.contrib import admin
from django.urls import path
from myformsapp import views

app_name = 'myformsapp'  # Define el espacio de nombres de la aplicación

urlpatterns = [
    path('', views.Cuerpo, name='base'),
    path('formularioContacto/', views.Fcontacto, name='formularioContacto'),
    path('Contacto/', views.Mcontacto),
    path('inicio/', views.Inicio, name='Inicio'),
    path('catalogo/', views.Catologo, name='Catalogo'),
    path('admin/', admin.site.urls),
]


from django.urls import path
from . import views

urlpatterns = [
    # path(ruta y/o nombre en la ruta, vista, nombre)
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('recetas/', views.recetas, name='recetas'),
    path('top/', views.top_10, name='top_10'),
    path('ofertas/', views.ofertas, name='ofertas'),
]
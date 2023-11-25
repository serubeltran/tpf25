from django.contrib import admin
from django.urls import path
from mitienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('productos', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos/guardar', views.guardar, name='guardar'),
    path('productos/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/modificar/<int:id>', views.modificar, name='modificar'),
    path('productos/editar', views.editar, name='editar')
]
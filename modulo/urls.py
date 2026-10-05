from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_gastos, name='lista_gastos'),
    path('gasto/<int:pk>/', views.detalle_gasto, name='detalle_gasto'),
    path('gasto/nuevo/', views.crear_gasto, name='crear_gasto'),
    path('gasto/<int:pk>/editar/', views.editar_gasto, name='editar_gasto'),
    path('gasto/<int:pk>/eliminar/', views.eliminar_gasto, name='eliminar_gasto'),
]
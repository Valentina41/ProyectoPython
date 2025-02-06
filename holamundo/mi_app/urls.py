from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login es la página principal
    path('inicio/', views.inicio, name='inicio'),  # Página de inicio después del login
    path('acercade/', views.acercade, name='acercade'),
   path('contacto/', views.contacto, name='contacto'),  # Nueva ruta para la página de contacto desactivada
    path('procesar-formulario/', views.procesar_formulario, name='procesar_formulario'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somos', views.somos, name="somos"),
    path('canchas', views.canchas, name="canchas"),
    path('reservas', views.reservas, name="reservas"),
    path('contacto', views.contacto, name="contacto"),
    path('login', views.login, name="login"),
    path('crear_venta', views.crear_venta, name="crear_venta"),
    path('gracias', views.gracias, name="gracias"),
    path('admin', views.admin, name="admin")
#    path('saludar/<str:nombre>', views.saludar, name='saludar')
]

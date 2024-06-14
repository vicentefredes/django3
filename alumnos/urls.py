#from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('crud_ramos', views.crud_ramos, name='crud_ramos'),
    path('ramosAdd', views.ramosAdd, name='ramosAdd'),
    path('ramos_edit/<str:pk>', views.ramos_edit, name='ramos_edit'),
    path('ramos_del/<str:pk>', views.ramos_del, name='ramos_del'),
    path('crud_secciones', views.crud_secciones, name='crud_secciones'),
    path('seccionesAdd', views.seccionesAdd, name='seccionesAdd'),
    path('secciones_edit/<str:pk>', views.secciones_edit, name='secciones_edit'),
    path('secciones_del/<str:pk>', views.secciones_del, name='secciones_del'),
    path('menu', views.menu, name='menu'),
]
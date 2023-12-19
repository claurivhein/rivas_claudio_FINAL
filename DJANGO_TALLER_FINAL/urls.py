from django.contrib import admin
from django.urls import path
from serialApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('crudinscritos',views.listarinscritos, name='crudinscritos'),
    path('crudinstitucion',views.listarinstituciones, name='crudinstitucion'),
    path('agregarinstitucion',views.agregarinstitucion, name='agregarinstitucion'),
    path('eliminarinstitucion/<int:id>', views.eliminarinstitucion, name='eliminarinstitucion'),
    path('actualizarinstitucion/<int:id>', views.actualizarinstitucion, name='actualizarinstitucion'),
    path('agregarinscripcion',views.agregarinscripcion, name='agregarinscripcion'),
    path('eliminarinscripcion/<int:id>', views.eliminarinscripcion, name='eliminarinscripcion'),
    path('actualizarinscripcion/<int:id>', views.actualizarinscripcion, name='actualizarinscripcion'),
    path('inscritos/',views.ListarInscripciones.as_view(), name='inscritos'),
    path('inscritos/<int:pk>',views.InscritosDetalle.as_view(), name='inscritosD'),
    path('institucion/',views.institucion_list, name='institucion'),
    path('institucion/<int:pk>',views.institucion_detalle, name='institucionD'),
    path('datos_autor/',views.ListarAutor.as_view(), name='datos_autor'),
    path('datos_autor/<int:pk>',views.AutorDetalle.as_view(), name='autor_detalle'),
]

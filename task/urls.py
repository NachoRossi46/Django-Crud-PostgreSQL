from django.urls import path
from .views import listadoTareas, crearTarea, eliminarTarea, editarTarea

urlpatterns = [
    path('', listadoTareas, name='listadoTareas'),
    path('crear/', crearTarea, name='crearTarea'),
    path('eliminar/<int:id>/', eliminarTarea, name='eliminarTarea'),
    path('editar/<int:id>/', editarTarea, name='editarTarea'),
]

from django.shortcuts import render, redirect
from .models import Task

def listadoTareas(request):
    tareas = Task.objects.all()
    return render(request, 'listado_tarea.html', {'tareas': tareas})

def crearTarea(request):
    tarea = Task(title=request.POST['titulo'], description=request.POST['descripcion'])
    tarea.save()
    return redirect('/tareas/')

def eliminarTarea(request, id):
    tarea = Task.objects.get(id=id)
    tarea.delete()
    return redirect('/tareas/')

def editarTarea(request, id):
    tarea = Task.objects.get(id=id)
    tarea.title = request.POST['titulo']
    tarea.description = request.POST['descripcion']
    tarea.save()
    return redirect('/tareas/')

def paginaPrincipal(request):
    return render(request, 'pagina_principal.html')
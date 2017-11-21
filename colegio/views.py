from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import GradoForm
from django.shortcuts import get_object_or_404
from colegio.models import Materia, Grado, Pertenece
# Create your views here.

def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                pertenece = Pertenece(materia_id=materia_id, grado_id = grado.id)
                pertenece.save()
            messages.add_message(request, messages.SUCCESS, 'Grado creado exitosamente')
        return redirect('grados/listagrados')
    else:
        formulario = GradoForm()
    return render(request, 'colegio/grado_editar.html', {'formulario': formulario})

def listar(request):
    grados = Grado.objects.all()
    return render(request,'colegio/listar.html',{'grados': grados})

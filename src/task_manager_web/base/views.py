from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#Permite restringir accesos a usuarios no logeados:
from django.contrib.auth.mixins import LoginRequiredMixin
#Crear vistas:
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
#LLevarte a una pagina ante la ocurrencia de un evento:
from django.urls import reverse_lazy

from .models import Tarea
#ListView tipo de página que representa una lista de objetos resultado de una consulta

# from django.http import HttpResponse
# #Importamos el modulo de Django que nos permite responder un llamado HTTP
#
# # Create your views here.
#
# #Definimos una vista que retornará como respuesta Http el mensaje 'Lista pendientes'
# def lista_pendientes(pedido):
#     return HttpResponse('Lista de pendientes')

#En este caso no hay consulta, solo estamos mostrando toda la lista de tareas en Tarea

#Logeo - cuando el usuario se logee se mostrarán las tareas
class Logeo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    #Redireccionar al usuario logeado
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')

class PaginaRegistro(FormView):
    template_name =  'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    #Si se registra exitosamente el usuario quedrá logeado
    def form_valid(self, form):
        #Guardamos datos del registro en una variable
        usuario = form.save()
        #si se registro correctamente
        if usuario is not None:
            #hacemos login con los datos del registro
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    #Si el usuario hizo login lo redirecciona a la página principal de tareas
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'

    #sobreescribimos mét0do de clase padre get_context
    def get_context_data(self, **kwargs):
        #llamamos al metodo de la clase padre pasando los kwargs
        context = super().get_context_data(**kwargs)
        #De todas las tareas que recibe filtrarlas por usuario y retornar solo esas
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        #EL modulo count de context serán las tareas no completadas aún
        context['count'] = context['tareas'].filter(completo=False).count()

        #Buscamos lo que el usuario ingrese en la cajita o si esta en blanco
        valor_buscado = self.request.GET.get('area-buscar') or ''
        #Si es True
        if valor_buscado:
            #Mostrar valores filtrados y mantener palabra en box
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

#Creamos vista de detalle dada una plantilla
class DetalleTarea(LoginRequiredMixin,DetailView):
    #hace referencia a cada objeto de la lista contenida en Tarea
    model = Tarea
    context_object_name = 'tarea'
    #definimos el nombre del template que no sigue el patron nombre_list.html
    template_name = 'base/tarea.html'

#clase que tomara nuestros modelos y creará un formulario basado en sus atributos
class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    #también podria ser field = ['campo1','campo2',...]
    #con '__all__' indicamos que todos los campos
    fields = ['titulo','descripcion','completo']
    #Evento success - registro exitoso nos lleva a tareas
    success_url = reverse_lazy('tareas')
    #Asigna el usuario logeadoa la creación de la tarea y elimina el campo de usuario del form
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

#Formulario para EDITAR tareas
class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = ['titulo','descripcion','completo']
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
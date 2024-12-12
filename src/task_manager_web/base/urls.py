from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logeo, PaginaRegistro
from django.contrib.auth.views import LogoutView

#Importamos las vistas de base y los paths de django

# '''
# urlpatterns -> Lista que contendra los patrones de URL
#     * path() -> utilizamos path de django para indicar que crearemos una ruta
#     * '' -> Indica que ira a la ruta base, en este caso http://127.0.0.1:8000/
#             si tuviera un contenido, este se esperaria al final de la ruta
#             EX:
#              - path('pendienteslist', views.lista_pendientes, name='pendientes')
#              - http://127.0.0.1:8000/pendienteslist
#     * views.lista_pendientes -> Indica que este llamado retornala lo que haya en la vista 'lista pendientes'
#     * name='pendientes' -> Indica el nombre del path
#     EX: http://127.0.0.1:8000/
# '''
# urlpatterns = [path('', views.lista_pendientes, name='pendientes')]

#LLamamos a la nueva vista generada por ListView
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Logeo.as_view(), name='login'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               #Establecemos vista de logout y mandamos a login cuando es success logout
               path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
               #<int:pk> -> indica referencia a una primary key integer
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               #Agregando ruta del formulario para agregar tarea
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               #Agregando ruta del formulario para EDITAR tarea
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               #Agregando ruta del formulario para ELIMINAR tarea
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]

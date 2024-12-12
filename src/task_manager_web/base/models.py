from django.db import models
from django.contrib.auth.models import User
#Importamos clasew de Django que nos permite manejar usuarios
#en las bases de datos de una manera más facil

# Create your models here.
class Tarea(models.Model):
    '''
    Definimos usuario con el tipo de dato Usuario de django y como Foreing Key
    - models.ForeignKey -> Indica que este u otro registro puede estar relacionado a un usuario por medio de campo/tributo
    - on_delete = models.CASCADE -> indica que cuando un usuario sea borrado se borraran todos los registros de esta tabla juanto con él
    - null = True -> Indica que este campo en esta tabla puede estar nullo
    - blank = True -> Indica que este campo en esta tabla puede estar vacio
    '''
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    #Titulo -> Campo de caracteres con limite máximo de 200
    titulo = models.CharField(max_length=200)
    #Descripción -> Campo de texto (con mas atributos que el de caracteres), puede ser null o estar vacio
    descripcion = models.TextField(null=True,
                                   blank=True)
    #Completo -> Campo booleano que por default es false
    completo = models.BooleanField(default=False)
    #Creado -> Tipo de dato datetime para almacenar fecha
    #Agrega automaticamente la fecha actual
    creado = models.DateTimeField(auto_now_add=True)

    #Lo que retornará cuando invoquemos string
    def __str__(self):
        return  self.titulo

    class Meta:
        #como se ordenaran las atreas dentro de la tabla
        ordering = ['completo'] # en este caso por el campo 'completo'
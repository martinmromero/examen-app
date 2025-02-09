
# Create your models here.
from django.db import models

class Pregunta(models.Model):
    texto = models.TextField()
    respuesta = models.TextField()
    fuente = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
class Examen(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    preguntas = models.ManyToManyField(Pregunta)

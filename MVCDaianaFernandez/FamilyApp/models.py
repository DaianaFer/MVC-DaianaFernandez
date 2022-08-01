from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    trabajo = models.CharField(max_length=30)
    edad = models.ImageField()
    direccion= models.CharField(max_length=50)
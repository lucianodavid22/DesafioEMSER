from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=15, null=False)
    apellido = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=36, null=False)

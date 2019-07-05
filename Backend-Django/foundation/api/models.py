from django.db import models
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Correo')
    phone_number = models.CharField(max_length=10, verbose_name='Celular')
    message = models.TextField(verbose_name='Mensaje')

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["-name"]

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number} - {self.message}'

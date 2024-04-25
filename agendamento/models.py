from django.db import models
from django.contrib.auth.models import User

class Entrevista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_entrevista = models.CharField(max_length=20)  
    data_hora = models.DateTimeField()
    cancelada = models.BooleanField(default=False)

    def __str__(self):
        return f"Entrevista de {self.usuario.username} - {self.tipo} em {self.data_hora}"

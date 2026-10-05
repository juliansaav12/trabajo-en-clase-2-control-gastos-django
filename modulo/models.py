from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Gasto(models.Model):
    CATEGORIAS = [
        ('ALIMENTACION', 'Alimentación'),
        ('TRANSPORTE', 'Transporte'),
        ('SERVICIOS', 'Servicios Públicos'),
        ('EDUCACION', 'Educación'),
        ('ENTRETENIMIENTO', 'Entretenimiento'),
        ('SALUD', 'Salud'),
        ('OTROS', 'Otros'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTROS')
    fecha = models.DateField(default=timezone.now)
    pagado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"
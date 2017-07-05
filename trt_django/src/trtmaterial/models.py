from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Materials(models.Model):
    material = models.CharField(max_length=500)
    tecnico = models.CharField(max_length=45)
    profissional = models.CharField(max_length=500)
    anexo = models.CharField(max_length=45, blank=True, null=True)
    registro = models.DateTimeField(auto_now=True, blank=True)
    data = models.DateField()
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'materials'

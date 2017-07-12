from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comentarios(models.Model):
    texto = models.CharField(max_length=2000)
    anexo = models.FileField(null=True,blank=True,upload_to='documents/%Y/%m/%d')

    class Meta:
        managed = False
        db_table = 'comentarios'

class ComentarioCompras(models.Model):
    id_compra = models.IntegerField()
    id_comentario = models.CharField(max_length=45)
    user = models.CharField(max_length=45, blank=True, null=True)
    registro = models.DateTimeField(auto_now=True,blank=True, null=True)
    anexo = models.FileField(null=True,blank=True,upload_to='documents/%Y/%m/%d')

    class Meta:
        managed = False
        db_table = 'comentario_compras'

class Compras(models.Model):
    data = models.DateField()
    origem = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)
    detalhes = models.CharField(max_length=1000)
    anexo = models.FileField(null=True,blank=True,upload_to='documents/%Y/%m/%d')
    valor = models.FloatField(blank=True, null=True)
    registro = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'

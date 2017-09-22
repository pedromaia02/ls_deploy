from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MossoroPosts(models.Model):
    numero_chamado = models.BigIntegerField(blank=True, null=True)
    local = models.CharField(max_length=45, blank=True, null=True)
    detalhe = models.CharField(max_length=500, blank=True, null=True)
    material = models.CharField(max_length=500, blank=True, null=True)
    tecnico = models.CharField(max_length=45, blank=True, null=True)
    profissional = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=17, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    anexo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inss_mossoro_chamados'


class MossoroCidades(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'inss_mossoro_cidades'


class MossoroProfissionals(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inss_mossoro_profissionals'

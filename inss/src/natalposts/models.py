from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# Show database command lines for creating here the existing ones:
# python manage.py inspectdb
#


class NatalPosts(models.Model):
    numero_chamado = models.BigIntegerField(blank=True, null=True)
    local = models.CharField(max_length=45, blank=True, null=True)
    detalhe = models.CharField(max_length=500, blank=True, null=True)
    material = models.CharField(max_length=500, blank=True, null=True)
    tecnico = models.CharField(max_length=45, blank=True, null=True)
    profissional = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=17, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    anexo = models.FileField(null=True,blank=True,upload_to='documents/%Y/%m/%d')

    class Meta:
        # managed = False
        db_table = 'inss_natal_chamados'


class NatalProfissionals(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    cargo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'inss_natal_profissionals'

class NatalCidades(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        # managed = False
        db_table = 'inss_natal_cidades'

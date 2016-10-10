from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# Show database command lines for creating here the existing ones:
# python manage.py inspectdb
#


class Posts(models.Model):
    contrato = models.CharField(max_length=45, blank=True, null=True)
    legenda = models.CharField(max_length=100, blank=True, null=True)
    detalhe = models.CharField(max_length=500, blank=True, null=True)
    valor = models.FloatField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    tipo = models.CharField(max_length=45, blank=False, null=False)
    anexo = models.FileField(null=True,blank=True,upload_to='documents/%Y/%m/%d')

    class Meta:
        managed = True
        db_table = 'posts'

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})


class Contratos(models.Model):
    nome = models.CharField(max_length=45)
    obs = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contratos'

class Legendas(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legendas'


# class Posts(models.Model):
#     title = models.CharField(max_length=45, blank=False, null=False)
#     content = models.CharField(max_length=45, blank=False, null=False)
#     updated = models.DateTimeField(blank=True, null=True)
#     timestamp = models.DateTimeField(blank=True, null=True)
#     data = models.DateField(blank=False, null=False)

#     def __unicode__(self):
#         return self.title

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"id": self.id})

#     class Meta:
#         #managed = False
#         db_table = 'posts'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from .models import Compras,Contratos,Comentarios
# import time
import datetime

class PostForm(forms.ModelForm):

	class Meta:
		model = Compras
		fields = [
			# "identificador",
			"origem",
			"data",
			"detalhes",
			"status",
			"prazo",
			"valor",
			"anexo",
		]


	STATUS = [
		('PENDENTE', 'PENDENTE'),
		('FECHADO', 'FECHADO'),
		('URGENTE', 'URGENTE'),
		]
	status = forms.CharField(widget=forms.Select(choices=STATUS))
	#data = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
	data = forms.DateField(widget=forms.SelectDateWidget(years=range(2015, 2020)),initial=datetime.date.today())
	prazo = forms.DateField(widget=forms.SelectDateWidget(years=range(2015, 2020)),initial=datetime.date.today())

	CONTRATOS = []
	nomes = [nome.encode("utf8") for nome in Contratos.objects.all().values_list('nome', flat=True)]
	for nome in nomes:
		CONTRATOS.append((nome,nome))
	origem = forms.CharField(widget=forms.Select(choices=CONTRATOS))
	#material = forms.CharField(widget=forms.Textarea)
	#profissional = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PROFESSIONAL_NOMES,)
	detalhes = forms.CharField(widget=forms.Textarea)
	anexo = forms.FileField(label='Anexar algum arquivo',help_text='max. 42 megabytes',required = False)

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['origem'].label = 'Origem:'
		self.fields['status'].label = 'Status:'
		self.fields['detalhes'].label = ''
		self.fields['data'].label = 'Data:'
		self.fields['prazo'].label = 'Prazo até dia:'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comentarios
		fields = [
			"texto",
			"anexo"
		]
	texto = forms.CharField(widget=forms.Textarea)
	anexo = forms.FileField(label='Anexar algum arquivo',help_text='max. 42 megabytes',required = False)
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['texto'].label = ''

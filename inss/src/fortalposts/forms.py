# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from .models import FortalPosts,FortalProfissionals,FortalCidades

import datetime

class PostForm(forms.ModelForm):

	class Meta:
		model = FortalPosts
		fields = [
			"numero_chamado",
			"local",
			"detalhe",
			"material",
			"tecnico",
			"data",
			"status",
			"profissional",
			"anexo",
		]

	PROFESSIONAL_NOMES = []
	nomes = [nome.encode("utf8") for nome in FortalProfissionals.objects.all().values_list('nome', flat=True)]
	for nome in nomes:
		PROFESSIONAL_NOMES.append([nome,nome])



	STATUS = [
		('FINALIZADO', 'FINALIZADO'),
		('EM ANDAMENTO', 'EM ANDAMENTO'),
		('FALTA DE MATERIAL', 'FALTA DE MATERIAL'),
		]
	status = forms.CharField(widget=forms.Select(choices=STATUS))
	#data = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
	data = forms.DateField(widget=forms.SelectDateWidget(years=range(2012, 2020)),initial=datetime.date.today())

	profissional = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PROFESSIONAL_NOMES,)
	detalhe = forms.CharField(widget=forms.Textarea)
	anexo = forms.FileField(label='Anexar algum arquivo',help_text='max. 42 megabytes',required = False)

	LOCAIS = []
	nomes = [nome.encode("utf8") for nome in FortalCidades.objects.all().values_list('nome', flat=True)]
	for nome in nomes:
		LOCAIS.append((nome,nome))

	local = forms.CharField(widget=forms.Select(choices=LOCAIS))

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['numero_chamado'].label = 'Chamado Nº:'
		self.fields['detalhe'].label = ''
		self.fields['tecnico'].initial = 'GEORGE'
		self.fields['profissional'].label = 'Profissionais'

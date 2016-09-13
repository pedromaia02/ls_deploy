# -*- coding: utf-8 -*-
from django import forms

from .models import Posts

import datetime

class PostForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = [
			"contrato",
			"legenda",
			"detalhe",
			"valor",
			"data",
			"tipo",
			"anexo",
		]

	LEGENDA = (
		('MATERIAIS DE OBRA', 'MATERIAIS DE OBRA'),
		('COMBUSTIVEL', 'COMBUSTIVEL'),
		('DESPESAS VIAGEM', 'DESPESAS VIAGEM'),
		('MANUTENCAO VEICULOS', 'MANUTENCAO VEICULO'),
		('MATERIAIS CONSUMO', 'MATERIAIS CONSUMO'),
		('DESPESAS OPERACIONAIS', 'DESPESAS OPERACIONAIS'),
		('FOLHA DE PAGAMENTO', 'FOLHA DE PAGAMENTO'),
		('UNIFORMES, FERAMENTAS, EPI', 'UNIFORMES, FERAMENTAS, EPI'),
		)

	CONTRATOS = (
		('TRT', 'TRT'),
		('FORTALEZA', 'FORTALEZA'),
		('SOBRAL', 'SOBRAL'),
		('JUAZEIRO', 'JUAZEIRO'),
		('INSS-NATAL', 'INSS-NATAL'),
		('PETROLINA', 'PETROLINA'),
		('BAHIA', 'BAHIA'),
		('IMPERATRIZ', 'IMPERATRIZ'),
		)

	CHOICES = (('1', 'Saída',), ('2', 'Entrada',))

	contrato = forms.CharField(widget=forms.Select(choices=CONTRATOS))
	legenda = forms.CharField(widget=forms.Select(choices=LEGENDA))
	data = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
	tipo = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	detalhe = forms.CharField(widget=forms.Textarea)
	anexo = forms.FileField(label='Select a file',help_text='max. 42 megabytes')

	def __init__(self, *args, **kwargs): 
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['legenda'].label = 'Serviço'
		self.fields['detalhe'].label = ''

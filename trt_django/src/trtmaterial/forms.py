# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from .models import Materials

import datetime

class PostForm(forms.ModelForm):

	class Meta:
		model = Materials
		fields = [
			"material",
			"profissional",
			"tecnico",
			"data",
			"status",
			#"registro",
			#"anexo",
		]


	STATUS = [
		('ENTREGUE AO PROFISSIONAL', 'ENTREGUE AO PROFISSIONAL'),
		('DEVOLVIDO', 'DEVOLVIDO'),
		]
	status = forms.CharField(widget=forms.Select(choices=STATUS))
	#data = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
	data = forms.DateField(widget=forms.SelectDateWidget(years=range(2012, 2020)),initial=datetime.date.today())
	#material = forms.CharField(widget=forms.Textarea)
	#profissional = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PROFESSIONAL_NOMES,)
	#detalhe = forms.CharField(widget=forms.Textarea)
	#anexo = forms.FileField(label='Anexar algum arquivo',help_text='max. 42 megabytes',required = False)


	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['material'].label = 'Material:'
		self.fields['profissional'].label = 'Profissional Responsavel:'
		self.fields['tecnico'].label = 'Emitido por:'
		self.fields['data'].label = 'Data:'

# -*- coding: utf-8 -*-
from django import forms
from posts.models import Contratos

class PostForm(forms.ModelForm):
    class Meta:
    	model = Contratos
    	fields = [
    		"nome",
    		"obs",
    	]
    obs = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['obs'].label = ''

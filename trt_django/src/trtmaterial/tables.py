# -*- coding: utf-8 -*-
# Customizar as tabelas do django-table2

import django_tables2 as tables
from .models import Materials

class PostsTable(tables.Table):

    #actions = tables.TemplateColumn("<a href=/trtmaterial/{{record.id}}>Detalhes</a>  -  <a href=/trtmaterial/{{record.id}}/edit>Modificar</a>  -  <a href=/trtmaterial/{{record.id}}/delete onclick='return confirm(\"Confima deletar o item selecionado?\")'>Excluir</a>", orderable=False)
    actions = tables.TemplateColumn("<a href=/trtmaterial/{{record.id}}/edit>Modificar</a>  -  <a href=/trtmaterial/{{record.id}}/delete onclick='return confirm(\"Confima deletar o item selecionado?\")'>Excluir</a>", orderable=False)
    #valor = tables.Column(footer="Total: ")

    def __init__(self, *args,**kwargs):
        super(PostsTable,self).__init__(*args, **kwargs)
        self.base_columns['data'].verbose_name = "Data"
        self.base_columns['data'].format = "D d M Y"
        #self.base_columns['anexo'].verbose_name = "Anexo"
        self.base_columns['material'].verbose_name = "Material"
        self.base_columns['profissional'].verbose_name = "Profissional Responsavel"
        self.base_columns['status'].verbose_name = "Status"
        self.base_columns['tecnico'].verbose_name = "Tecnico Responsavel"
        # self.base_columns['profissional'].verbose_name = "Profissional Responsável"
        self.base_columns['actions'].verbose_name = "Ações"
        self.base_columns['registro'].verbose_name = "Ultima Alteracao"

    class Meta:
        model = Materials
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ('data', 'material', 'profissional','status','tecnico','actions', 'registro')
        #fields = ('data', 'material', 'profissional','status','tecnico','anexo')

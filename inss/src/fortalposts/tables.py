# -*- coding: utf-8 -*-
# Customizar as tabelas do django-table2

import django_tables2 as tables
from .models import FortalPosts

class PostsTable(tables.Table):

    actions = tables.TemplateColumn("<a href=/inssfortaleza/{{record.id}}>Detalhes</a>  -  <a href=/inssfortaleza/{{record.id}}/edit>Modificar</a>  -  <a href=/inssfortaleza/{{record.id}}/delete onclick='return confirm(\"Confima deletar o item selecionado?\")'>Excluir</a>", orderable=False)
    #valor = tables.Column(footer="Total: ")

    def __init__(self, *args,**kwargs):
        super(PostsTable,self).__init__(*args, **kwargs)
        self.base_columns['data'].verbose_name = "Data"
        self.base_columns['data'].format = "D d M Y"
        self.base_columns['anexo'].verbose_name = "Anexo"
        self.base_columns['local'].verbose_name = "Local"
        self.base_columns['numero_chamado'].verbose_name = "Nº Chamado"
        self.base_columns['status'].verbose_name = "Status"
        # self.base_columns['profissional'].verbose_name = "Profissional Responsável"
        self.base_columns['actions'].verbose_name = "Ações"

    class Meta:
        model = FortalPosts
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ('data', 'numero_chamado', 'local','status','anexo','actions')

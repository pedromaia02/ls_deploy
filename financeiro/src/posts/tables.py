# -*- coding: utf-8 -*-
# Customizar as tabelas do django-table2

import django_tables2 as tables
from .models import Posts

class PostsTable(tables.Table):

    actions = tables.TemplateColumn("<a href=/posts/{{record.id}}/edit>Modificar</a>  -  <a href=/posts/{{record.id}}/delete onclick='return confirm(\"Confima deletar o item selecionado?\")'>Excluir</a>", orderable=False)
    #valor = tables.Column(footer="Total: ")

    def __init__(self, *args,**kwargs):
        super(PostsTable,self).__init__(*args, **kwargs)
        self.base_columns['data'].verbose_name = "Data"
        self.base_columns['data'].format = "D d M Y"
        self.base_columns['anexo'].verbose_name = "Anexo"
        self.base_columns['detalhe'].verbose_name = "Descrição"
        self.base_columns['contrato'].verbose_name = "Contrato"
        self.base_columns['tipo'].verbose_name = "Tipo"
        self.base_columns['valor'].verbose_name = "Valor (R$)"
        self.base_columns['actions'].verbose_name = "Ações"

    class Meta:
        model = Posts
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ('data', 'contrato', 'legenda','detalhe','tipo','valor','anexo',)

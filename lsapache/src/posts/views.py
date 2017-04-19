# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required
from decimal import Decimal
# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy

from django_tables2 import RequestConfig

from .models import Posts,Contratos,Legendas
from .forms import PostForm
from .tables import PostsTable
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@login_required(login_url='/login/')
def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()

		messages.success(request,"Successfully Created!!")
		#return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("posts:list")

	#if request.method == 'POST':
		#print request.POST.get("title")
	#	title = request.POST.get("title")
		#print request.POST.get("content")
	#	content = request.POST.get("content")
	#	Posts.objects.create(title=title,content=content)

	context = {
		"form":form,
	}
	return render(request,"post_form.html", context)

@login_required(login_url='/login/')
def post_detail(request, local=None):

	queryset = Posts.objects.all().filter(contrato__icontains=local)
	query = request.GET.get('mes','')
	query_ano = request.GET.get('ano','')
	legenda_nomes = Legendas.objects.all().values_list('nome') #Obter nome das legendas na tabela legendas
	title = ('Estruturado por Legenda - Contrato: %s - ' % local)+"Todos os meses"

	if query != None:
		try:
			if query_ano == "todos":
				queryset = queryset.filter(data__month=query)
			elif query == "todos":
				queryset = queryset.filter(data__year=query_ano)
			else:
				queryset = queryset.filter(data__year=query_ano,data__month=query)
			title = ('Estruturado por Legenda - Contrato: %s - ' % local)+str(query)+"/"+str(query_ano)
			#print title
		except:
			pass

	legendas_valores = {}
	for nome in legenda_nomes:

		#valorSaida = queryset.filter(legenda__icontains=nome[0],tipo__icontains='SAIDA').aggregate(Sum('valor'))
		valorSaida = queryset.filter(legenda__icontains=nome[0]).aggregate(Sum('valor'))
		legendas_valores[str(nome[0])] = {}

		if valorSaida['valor__sum'] != None:
			#contrato_valor_saida.update({str(nome[0]):valorSaida['valor__sum']})
			legendas_valores[str(nome[0])]['saida'] = round(valorSaida['valor__sum'],2)
		else:
			#contrato_valor_saida.update({str(nome[0]):0})
			legendas_valores[str(nome[0])]['saida'] = 0


	valorEntrada = queryset.filter(tipo__icontains='ENTRADA').aggregate(Sum('valor'))
	if valorEntrada['valor__sum'] != None:
		valorEntrada = round(valorEntrada['valor__sum'],2)
	else:
		valorEntrada = 0
	valorSaida = queryset.filter(tipo__icontains='SAIDA').aggregate(Sum('valor'))
	if valorSaida['valor__sum'] != None:
		valorSaida = round(valorSaida['valor__sum'],2)
	else:
		valorSaida = 0

	graph_saida = [['Legenda','Saida']]
	for x in legendas_valores.items():
		graph_saida.append([x[0],x[1]['saida']])

	#print legendas_valores
	context = {
		"title":title,
		"graph_saida": json.dumps(graph_saida),
		"legendas_valores": legendas_valores,
		"valorTotalEntrada": locale.currency(valorEntrada, grouping=True, symbol=True),
		"valorTotalSaida": locale.currency(valorSaida, grouping=True, symbol=True),
		"valorTotalLucro": locale.currency((valorEntrada - valorSaida), grouping=True, symbol=True),
		"local": local,
		"mes": query,
		"ano": query_ano,
	}

	return render(request,"post_detail.html", context)

@login_required(login_url='/login/')
def post_list(request):

	queryset = Posts.objects.all().order_by('data')
	query = request.GET.get('mes','')
	query_ano = request.GET.get('ano','')
	mes = "todos"
	ano = "todos"
	if query != None:
		try:
			if query_ano == "todos":
				queryset = queryset.filter(data__month=query)
			elif query == "todos":
				queryset = queryset.filter(data__year=query_ano)
			else:
				queryset = queryset.filter(data__year=query_ano,data__month=query)
			data = str(query)+"/"+str(query_ano)
			#print title
			mes = str(query)
			ano = str(query_ano)
		except:
			pass
		queryset = queryset.filter(contrato__icontains=request.GET.get('contrato',''))
		queryset = queryset.filter(legenda__icontains=request.GET.get('servico',''))
		queryset = queryset.filter(tipo__icontains=request.GET.get('tipo',''))
		queryset = queryset.filter(detalhe__icontains=request.GET.get('detalhe',''))

	valor_total = queryset.aggregate(Sum('valor'))
	valor_total = valor_total['valor__sum']
	if valor_total == None:
		valor_total = 0

	contrato = request.GET.get('contrato','')
	if contrato == None:
		contrato = "todos"
	servico = request.GET.get('servico','')
	if servico == None:
		servico = "todos"
	tipo = request.GET.get('tipo','')
	if tipo == None:
		tipo = "todos"

	# title = "Mes: " + mes + " Ano: " + ano + " " + contrato + " - " + servico + " - " + tipo

	table = PostsTable(queryset)
	RequestConfig(request, paginate={'per_page': 25}).configure(table)
	context = {
			"object_list": queryset,
			"table": table,
			"nome_contratos": [nome.encode("utf8") for nome in Contratos.objects.all().values_list('nome', flat=True)],
			"nome_legendas": [nome.encode("utf8") for nome in Legendas.objects.all().values_list('nome', flat=True)],
			"valor_total": round(valor_total,2),
			#"title": title
	 	}
	return render(request,"post_list.html", context)

@login_required(login_url='/login/')
def post_update(request, id=None):
	instance = get_object_or_404(Posts,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return redirect("posts:list")
	context = {
		"instance": instance,
		"form": form
	}
	return render(request,"post_form.html", context)

@login_required(login_url='/login/')
def post_delete(request, id=None):
	instance = get_object_or_404(Posts, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("posts:list")

@login_required(login_url='/login/')
def dre(request):

	if request.user.username == "aprendiz":
		return redirect('/login/?next=%s' % request.path)

	queryset = Posts.objects.all()
	query = request.GET.get('mes','')
	query_ano = request.GET.get('ano','')
	contrato_nomes = Contratos.objects.all().values_list('nome') #Obter nome dos contratos na tabela contratos
	contrato_valor_entrada = {} #dict com o nome do contrato + o valor de entrada resultante no periodo
	contrato_valor_saida = {} #dict com o nome do contrato + o valor de saida resultante no periodo
	title = "DRE - TOTAL"
	if query != None:
		try:
			if query_ano == "todos":
				queryset = queryset.filter(data__month=query)
			elif query == "todos":
				queryset = queryset.filter(data__year=query_ano)
			else:
				queryset = queryset.filter(data__year=query_ano,data__month=query)
			title = "DRE - "+str(query)+"/"+str(query_ano)
			print title
		except:
			pass

	contratos_valores = {}
	#Loop para preencher os dicts
	for nome in contrato_nomes:
		valorEntrada = queryset.filter(contrato__icontains=nome[0],tipo__icontains='ENTRADA').aggregate(Sum('valor'))
		valorSaida = queryset.filter(contrato__icontains=nome[0],tipo__icontains='SAIDA').aggregate(Sum('valor'))

		contratos_valores[str(nome[0])] = {}
		if valorEntrada['valor__sum'] != None:
			#contrato_valor_entrada.update({ nome[0]:valorEntrada['valor__sum']})
			contratos_valores[str(nome[0])]['entrada'] = round(valorEntrada['valor__sum'],2)
		else:
			#contrato_valor_entrada.update({nome[0]:0})
			contratos_valores[str(nome[0])]['entrada'] = 0
		if valorSaida['valor__sum'] != None:
			#contrato_valor_saida.update({str(nome[0]):valorSaida['valor__sum']})
			contratos_valores[str(nome[0])]['saida'] = round(valorSaida['valor__sum'],2)
		else:
			#contrato_valor_saida.update({str(nome[0]):0})
			contratos_valores[str(nome[0])]['saida'] = 0

	#Calculcar valores Lucros de cada contrato e valores totais:
	total_saida = 0
	total_entrada = 0
	total_lucro = 0
	graph_saida = [['Contrato','Saida']]
	graph_entrada = [['Contrato','Entrada']]
	graph_lucro = [['Contrato','Lucros']]
	for x in contratos_valores.items():
		contratos_valores[x[0]]['lucro'] = x[1]['entrada'] - x[1]['saida']
		total_lucro = total_lucro + contratos_valores[x[0]]['lucro']
		total_saida = total_saida + x[1]['saida']
		total_entrada = total_entrada + x[1]['entrada']
		graph_saida.append([x[0],x[1]['saida']])
		graph_entrada.append([x[0],x[1]['entrada']])
		graph_lucro.append([x[0],contratos_valores[x[0]]['lucro']])

	#print graph_saida
	# dictdata=[
    # ['Task', 'Hours per Day'],
    # ['Work',     11],
    # ['Eat',      2],
    # ['Commute',  2],
    # ['Watch TV', 2],
    # ['Sleep',    7]
    # ]

	context = {
			#"object_list": queryset,
			"title": title,
			"contratos_valores": contratos_valores,
			"total_saida": locale.currency(total_saida, grouping=True, symbol=True),
			"total_entrada": locale.currency(total_entrada, grouping=True, symbol=True),
			"total_lucro": locale.currency(total_lucro, grouping=True, symbol=True),
			"graph_saida": json.dumps(graph_saida),
			"graph_entrada": json.dumps(graph_entrada),
			"graph_lucro": json.dumps(graph_lucro),
			"mes": query,
			"ano": query_ano,
	 	}
	return render(request,"dre.html", context)

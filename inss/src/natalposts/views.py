# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required
# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy

from django_tables2 import RequestConfig

from .models import NatalPosts,NatalProfissionals,NatalCidades
from .forms import PostForm
from .tables import PostsTable

from django.http import HttpResponse
from django.views.generic import View
from inssonline.utils import render_to_pdf #created in step 4

#@login_required(login_url='/login/')
def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request,"Successfully Created!!")
		return redirect("natalposts:list")

	context = {
		"form":form,
	}
	return render(request,"post_natal_form.html", context)

#@login_required(login_url='/login/')
def post_detail(request, id=None):
	instance = get_object_or_404( NatalPosts,id=id)

	#Converter lá os nomes.
	profissional_nomes = []
	nomes_utf8 = instance.profissional.split(",")
	for nome in nomes_utf8:
		profissional_nomes.append(nome.partition("'")[2].partition("'")[0])
	profissional_nomes = [x.encode("utf8") for x in profissional_nomes]
	profissional_cargos = NatalProfissionals.objects.filter(nome__in=profissional_nomes).values_list('nome','cargo')


	context = {
		#"title":instance.title,
		"instance": instance,
		"profissional_nomes": profissional_nomes,
		"profissional_cargos":profissional_cargos,
	}
	return render(request,"post_natal_detail.html", context)

#@login_required(login_url='/login/')
def post_list(request):

	queryset = NatalPosts.objects.all().order_by('-data')
	query = request.GET

	if query:
		try:
			queryset = queryset.filter(data__month=request.GET.get('mes',''))
		except:
			pass
		queryset = queryset.filter(local__icontains=request.GET.get('local',''))
		queryset = queryset.filter(status__icontains=request.GET.get('status',''))
		queryset = queryset.filter(detalhe__icontains=request.GET.get('detalhe',''))
		#print queryset.values_list()
		if request.GET.get('tipo','')=='0' or request.GET.get('tipo','')== "":
			pass
		elif request.GET.get('tipo','')=='2':
			queryset = queryset.filter(numero_chamado__exact=None)
		else:
			queryset = queryset.filter(numero_chamado__icontains='')

	table = PostsTable(queryset)
	#NO PAGINATION: RequestConfig(request, paginate=false).configure(table)
	RequestConfig(request, paginate={'per_page': 25}).configure(table)
	context = {
			"object_list": queryset,
			"table": table,
			"cidades":NatalCidades.objects.all().order_by('nome').values_list('nome', flat=True)
	 	}
	return render(request,"post_natal_list.html", context)

#@login_required(login_url='/login/')
def post_update(request, id=None):
	instance = get_object_or_404(NatalPosts,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return redirect("natalposts:list")
	context = {
		"instance": instance,
		"form": form
	}
	return render(request,"post_natal_form.html", context)
#
#@login_required(login_url='/login/')
def post_delete(request, id=None):
	instance = get_object_or_404(NatalPosts, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("natalposts:list")


def setup_pdf(request):

	queryset = NatalPosts.objects.all().order_by('data')
	query = request.GET
	dados = []
	if query:
		mes = request.GET.get('mes','')
		ano = request.GET.get('ano','')
		queryset = queryset.filter(data__year=ano)
		queryset = queryset.filter(data__month=mes)

		for x in queryset.values_list():
			dados.append(list(x))

		for i in range(0,len(dados)):
			nomes = []
			str_list = ""
			nomes = dados[i][6].split(",")
			for nome in nomes:
				str_list += nome.partition("'")[2].partition("'")[0]
				str_list += " ; "
			dados[i][6] = str_list

		context = {
		'dados': dados,
		'ano': ano,
		'mes': mes,
		}
		pdf = render_to_pdf('pdf/invoice.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

	context = {
	'object_list': queryset,
	'dados': dados,
	}
	return render(request,"pdf/setup_pdf.html", context)

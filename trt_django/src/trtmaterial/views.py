# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Materials
from .forms import PostForm
from .tables import PostsTable
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q

from django_tables2 import RequestConfig
# Create your views here.

def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request,"Successfully Created!!")
		return redirect("trtmaterial:list")

	context = {
		"form":form,
	}
	return render(request,"create_form.html", context)


def post_list(request):

	queryset = Materials.objects.all().order_by('-data')
	query = request.GET

	if query:
		try:
			queryset = queryset.filter(data__month=request.GET.get('mes',''))
		except:
			pass
		# queryset = queryset.filter(profissional__icontains=request.GET.get('profissional',''))
		# queryset = queryset.filter(tecnico__icontains=request.GET.get('tecnico',''))
		queryset = queryset.filter(Q(tecnico__icontains=request.GET.get('detalhe',''))
		| Q(material__icontains=request.GET.get('detalhe','')) | Q(profissional__icontains=request.GET.get('detalhe','')))
		# queryset = queryset.filter(material__icontains=request.GET.get('detalhe',''))
		# queryset = queryset.filter(profissional__icontains=request.GET.get('detalhe',''))

		queryset = queryset.filter(status__icontains=request.GET.get('status',''))
		# print queryset.values_list()
		# if request.GET.get('tipo','')=='0' or request.GET.get('tipo','')== "":
		# 	pass
		# elif request.GET.get('tipo','')=='2':
		# 	queryset = queryset.filter(numero_chamado__exact=None)
		# else:
		# 	queryset = queryset.filter(numero_chamado__icontains='')

	table = PostsTable(queryset)
	#NO PAGINATION: RequestConfig(request, paginate=false).configure(table)
	RequestConfig(request, paginate={'per_page': 25}).configure(table)
	context = {
			"object_list": queryset,
			"table": table,
			#"cidades":NatalCidades.objects.all().order_by('nome').values_list('nome', flat=True)
	 	}
	return render(request,"post_list.html", context)


# def post_detail(request, id=None):
# 	instance = get_object_or_404( NatalPosts,id=id)
#
# 	#Converter lá os nomes.
# 	profissional_nomes = []
# 	nomes_utf8 = instance.profissional.split(",")
# 	for nome in nomes_utf8:
# 		profissional_nomes.append(nome.partition("'")[2].partition("'")[0])
# 	profissional_nomes = [x.encode("utf8") for x in profissional_nomes]
# 	profissional_cargos = NatalProfissionals.objects.filter(nome__in=profissional_nomes).values_list('nome','cargo')
#
#
# 	context = {
# 		#"title":instance.title,
# 		"instance": instance,
# 		"profissional_nomes": profissional_nomes,
# 		"profissional_cargos":profissional_cargos,
# 	}
# 	return render(request,"post_natal_detail.html", context)
#
#
#
#
def post_update(request, id=None):
	instance = get_object_or_404(Materials,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return redirect("trtmaterial:list")
	context = {
		"instance": instance,
		"form": form
	}
	return render(request,"create_form.html", context)
#
def post_delete(request, id=None):
	instance = get_object_or_404(Materials, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("trtmaterial:list")

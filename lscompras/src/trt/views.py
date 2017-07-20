# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Compras,Comentarios,ComentarioCompras
from .forms import PostForm, CommentForm
# from .tables import PostsTable
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
import socket
from django.contrib.auth.decorators import login_required
import os

# from django_tables2 import RequestConfig
# Create your views here.

@login_required(login_url='/login/')
def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request,"Successfully Created!!")
		os.system('echo -e "to: alexandra@lsprojetos.com.br\nsubject: Nova solicitação de compra cadastrada\n" | ssmtp ls.projetos02@gmail.com')
		os.system('echo -e "to: escritorio2@lsprojetos.com.br\nsubject: Nova solicitação de compra cadastrada\n" | ssmtp ls.projetos02@gmail.com')
		return redirect("comprastrt:list")

	context = {
		"form":form,
	}
	return render(request,"post_form_trt.html", context)

@login_required(login_url='/login/')
def post_list(request):

	queryset = Compras.objects.all().filter(origem='TRT').order_by('-registro')
	query = request.GET
	if query:
		try:
			queryset = queryset.filter(data__month=request.GET.get('mes',''))
		except:
			pass
		queryset = queryset.filter(origem__icontains=request.GET.get('local',''))
		queryset = queryset.filter(status__icontains=request.GET.get('status',''))
		queryset = queryset.filter(detalhes__icontains=request.GET.get('detalhe',''))

	title = ''
	if request.GET.get('local','') != '':
		title = title + ' | ' + request.GET.get('local','')
	if request.GET.get('status','') != '':
		title = title + ' | ' + request.GET.get('status','')
	context = {
			"title": title,
			"object_list": queryset,
			# "cidades":Contratos.objects.all().order_by('nome').values_list('nome', flat=True)
	 	}

	return render(request,"post_list_trt.html", context)

@login_required(login_url='/login/')
def post_detail(request, id=None):

	instance = get_object_or_404(Compras,id=id)
	form = CommentForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Ok!!")
		# print instance.anexo
		# id_comentario=instance.__dict__['id']
		ComentarioCompras(id_compra=id,id_comentario=instance.id,user="TRT",anexo=instance.anexo,).save()
		return redirect(request.META['HTTP_REFERER'])

	comentarios_compra = ComentarioCompras.objects.filter(id_compra=id)
	ids = []
	for obj in comentarios_compra.values_list('id'):
		ids.append(int(obj[0]))
	users = []
	for obj in comentarios_compra.values_list('user'):
		users.append(obj[0])
	registros = []
	for obj in comentarios_compra.values_list('registro'):
		registros.append(obj[0])
	anexos = []
	for obj in comentarios_compra.values_list('anexo'):
		anexos.append(obj[0])
	# print anexos
	comentarios = comentarios_compra.values_list('id_comentario')
	textos = []
	for obj in comentarios:
		textos.extend(Comentarios.objects.filter(id=int(obj[0])).values_list('texto')[0])

	zipped = zip(textos, ids, users, registros, anexos)
	context = {"zipped": zipped, "instance": instance,"form": form,"textos": textos}

	return render(request,"post_detail_trt.html", context)

@login_required(login_url='/login/')
def post_update(request, id=None):
	instance = get_object_or_404(Compras,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return redirect("comprastrt:list")
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request,"post_form_trt.html", context)
#
@login_required(login_url='/login/')
def post_delete(request, id=None):
	instance = get_object_or_404(Compras, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("comprastrt:list")

@login_required(login_url='/login/')
def comment_delete(request, id=None):
	instance = get_object_or_404(ComentarioCompras, id=id)
	instance.delete()
	messages.success(request,"Mensagem Excluída :(")
	return redirect(request.META['HTTP_REFERER'])

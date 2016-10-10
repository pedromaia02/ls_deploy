from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

from posts.models import Contratos
from .forms import PostForm

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created!!")
		return redirect("addinfo:list")

	context = {
		"form":form,
	}
	return render(request,"post_form.html", context)

def post_detail(request, local=None):
    a = 2

def post_list(request):
    queryset = Contratos.objects.all()
    context = {
		"object_list": queryset,
    }
    return render(request,"info_list.html", context)

def post_update(request, id=None):
    a = 2

def post_delete(request, id=None):
	instance = get_object_or_404(Contratos, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("addinfo:list")

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

from .models import Posts
from .forms import PostForm

def post_create(request):

	form = PostForm(request.POST, request.FILES)
	#form2 = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		#instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		#instance.save()
		newdoc = Document(docfile = request.FILES['docfile'])
		newdoc.save()
		messages.success(request,"Successfully Created!!")
		return HttpResponseRedirect(instance.get_absolute_url())

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

def post_detail(request, id=None):
	instance = get_object_or_404(Posts,id=id)
	context = {
		"title":instance.contrato,
		"instance": instance,
	}
	return render(request,"post_detail.html", context)

def post_list(request):
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title":"List (Ok)"
	# 	}
	# else:
	# 	context = {
	# 		"title":"List (no OK)"
	# 	}
	queryset = Posts.objects.all().order_by('data')
	context = {
			"object_list": queryset,
	 		"title":"List (Ok)"
	 	}
	return render(request,"post_list.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Posts,id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title":instance.title,
		"instance": instance,
		"form": form
	}
	return render(request,"post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Posts, id=id)
	instance.delete()
	messages.success(request,"Item Deleted :(")
	return redirect("posts:list")

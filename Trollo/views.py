from django.shortcuts import render
from django.http import HttpResponse
from .models import Object, Project, List, Task, Element
from django.template import loader

def index(request):
	Object_list = Object.objects.order_by('id')
	template = loader.get_template('Trollo/index.html')
	context = { 'Object_list': Object_list,}
	return HttpResponse(template.render(context,request))
	
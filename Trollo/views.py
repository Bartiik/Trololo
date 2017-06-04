from django.shortcuts import render
from django.http import HttpResponse
from .models import Object, Project, List, Task, Element
from django.template import loader

def index(request):
	Object_list = Project.objects.order_by('id')
	template = loader.get_template('Trollo/index.html')
	context = { 'Object_list': Object_list,}
	return HttpResponse(template.render(context,request))
def project(request, project_id):
    id = project_id
    context = {'id':id,}
    List_list = List.objects.order_by('id')
    template = loader.get_template('Trollo/cos.html')
    return HttpResponse(template.render(context,request))
def Sax(request):
    context = { 'object_context': 1,}
    template = loader.get_template('Trollo/SaxGuy.html')
    return HttpResponse(template.render(context,request))
from django.shortcuts import render
from django.http import HttpResponse
from .models import Object, Project, List, Task, Element
from django.template import loader

def index(request):
	Object_list = Object.objects.order_by('id')
	template = loader.get_template('Trollo/index.html')
	context = { 'Object_list': Object_list,}
	return HttpResponse(template.render(context,request))
def sax(request):
    context = { 'a': 1}
    template = loader.get_template('Trollo/SaxGuy.html')
    return HttpResponse(template.render(context,request))
def project(request,project_id):
    id = project_id
    List_list = List.objects.raw('SELECT * FROM trollo_list WHERE project_id=%s',id)
    Task_list = Task.objects.raw('SELECT * FROM trollo_task WHERE project_id=%s ORDER BY List_id',id)
    Element_list = Element.objects.raw('SELECT * FROM Trolo.element WHERE project_id=%s ORDER BY Task_id',id)
    context = { 'id': id, 'List_list': List_list, 'Task_list': Task_list, 'Element_list':Element_list,}
    template = loader.get_template('Trollo/project.html')
    return HttpResponse(template.render(context,request))
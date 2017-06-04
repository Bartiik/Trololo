from django.contrib import admin

from .models import Object, Project, List, Task, Element

admin.site.register(Object)
admin.site.register(Project)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Element)
# Register your models here.

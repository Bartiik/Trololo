from django.db import models

# Create your models here.
class Object(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField('Creation date')
    position = models.IntegerField(default=0)
    def __str__(self):
        return self.name
	
class Project(models.Model):
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class List(models.Model):
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    project_id = models.IntegerField(default=0)
	
class Task(models.Model):
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    deadline = models.DateTimeField('Deadline')
    List_id = models.IntegerField(default=0)
	
class Element(models.Model):
    Object = models.ForeignKey(Object, on_delete=models.CASCADE)
    Task_id = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
	
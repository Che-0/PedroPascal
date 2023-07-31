from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request, username):
    return HttpResponse("Hello %s! " % username)

def about(request):
    #return HttpResponse("About page ! ")
    username =  "mannuel " 
    return render(request, 'about.html',{
        'username': username
    })

def index(request):
    #return HttpResponse("Index page ! ")
    title =  "Welcome to django Course hijo de perra"    
    return render(request, 'index.html',{
        'title': title,
    })

def projects(request):
    #projects = list(Project.objects.values() )
    #return JsonResponse(projects, safe=False) #safe=false porque no es un diccionario 
    project = Project.objects.all()
    return render(request, 'project.html',{
        'project': project
    })

#def tasks(request,id):
def tasks(request):
    #task = Task.objects.get(id=id)  esta madre genera un error cuando no existe el id
    ##task = get_object_or_404(Task, id=id) #esta madre genera un error 404 cuando no existe el id pero no colapce la aplicacion
    
    #return HttpResponse("Tasks: %s! " % id) 

    taskss = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': taskss
    }) 
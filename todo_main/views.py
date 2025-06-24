from django.shortcuts import render, redirect
from todo_main.models import Task
from django.http import HttpResponse

# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') #filter is used fetch thr multiole date 
    # print(tasks)
    context = {
        'tasks': tasks,
    }
    return render(request,'home.html' , context)


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
from django.shortcuts import render, redirect, get_object_or_404
from todo_main.models import Task
from django.http import HttpResponse

# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') #filter is used fetch thr multiole date 
    # print(tasks)
    completed_task = Task.objects.filter(is_completed=True)
    # print(completed_task)
    context = {
        'tasks': tasks,
        'completed_task': completed_task,
        
    }
    return render(request,'home.html' , context)


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk) #this is a inbuld fuction which will get the data if there is no dtata it will give 404 erreor
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        # print(new_task)
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

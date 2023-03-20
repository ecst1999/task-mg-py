from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.



def home(request):

    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my_login.html')

# - CREATE TASK

def createTask(request):

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')


    context = {'form': form}

    return render(request, 'create-task.html', context)


# - READ TASK

def viewTasks(request):

    tasks = Task.objects.all()    

    context = {'tasks': tasks}

    return render(request, 'view-tasks.html', context)


# - UPDATE TASK

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
            
        form = TaskForm(request.POST, instance= task)

        if form.is_valid():
            
            form.save()

            return redirect('view-tasks')

    context = {'form': form}

    return render(request, 'update-task.html', context)


# - DELETE a task

def deleteTask(request, pk):
    
    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('view-tasks')
    
    context = {'object': task}

    return render(request, 'delete-task.html', context)
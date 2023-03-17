from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.



def home(request):

    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(request, 'index.html', context)

def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my_login.html')


def createTask(request):

    form = TaskForm()

    context = {'form': form}

    return render(request, 'task-form.html', context)
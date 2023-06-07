from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm, CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task

def home(request):

    return render(request, 'index.html')

# - REGISTER 

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponse('The user was registered!')
        

    context = {'form': form}

    return render(request, 'register.html', context)


# - Login a user
def my_login(request):

    form = LoginForm

    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
    
    context = {'form': form}

    return render(request, 'my_login.html', context=context)

#------------------------------------TASKS---------------------------------------#
@login_required(login_url='my-login')
def task_list(request):

    tasks = Task.objects.filter(user = request.user).all()

    return render(request, 'task/task_list.html', {
        'tasks': tasks
    })

# Dashboard a user
@login_required(login_url='my-login')
def dashboard(request):
    
    return render(request, 'profile/dashboard.html')

# Logout a user
def user_logout(request):

    auth.logout(request)
    
    return redirect("")

# - Create a Task page
@login_required(login_url='my-login')
def createTask(request):

    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            
            task = form.save(commit=False)

            task.user = request.user
            
            form.save()

            return redirect('view-tasks')
    
    context = {'form': form}

    return render(request, 'profile/create-task.html', context=context)

# - Read Tasks
@login_required(login_url='my-login')
def viewTasks(request):

    current_user = request.user.id

    tasks = Task.objects.all().filter(user=current_user)

    context = {'tasks': tasks}

    return render(request, 'profile/view-tasks.html', context=context)
    

# - Update Task
@login_required(login_url='my-login')
def updateTask(request, pk):
    
    task = Task.objects.get(pk=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')
        
    context = {'form': form}

    return render(request, 'profile/update-task.html', context=context)

@login_required(login_url='my-login')
def deleteTask(request, pk):
    
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('view-tasks')
    
    return render(request, 'profile/delete-task.html')
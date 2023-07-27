from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task, Profile

# - Import Django Messages (notifications)
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'index.html')

# - REGISTER 

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)
            
            messages.success(request, 'User registration was successful!')

            return redirect('my-login')
        

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

# Dashboard a user
@login_required(login_url='my-login')
def dashboard(request):

    profile = Profile.objects.get(user=request.user)

    context = {'profile': profile}
    
    return render(request, 'profile/dashboard.html', context=context)

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

# - Profile managment
@login_required(login_url='my-login')
def profileManagment(request):
    
    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    form2 = UpdateProfileForm(instance=profile)
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        form2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():

            user_form.save()

            messages.success(request, 'Se guardo los cambios con exito')

            return redirect('dashboard')    
        
        if form2.is_valid():

            form2.save()

            messages.success(request, 'Se cambio la imagen con exito')

            return redirect('dashboard')  

    context = {'user_form': user_form, 'form2': form2}

    return render(request, 'profile/profile-managment.html', context=context)

@login_required(login_url='my-login')
def deteleAccount(request):
    
    
    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('')
    
    return render(request, 'profile/delete-account.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import CreateUserForm, LoginForm, TaskForm, NoteForm, CategoryForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Task, Note, Category

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



# Dashboard a user
@login_required(login_url='my-login')
def dashboard(request):
    
    return render(request, 'profile/dashboard.html')

# Logout a user
def user_logout(request):

    auth.logout(request)
    
    return redirect("")

#------------------------------------TASKS---------------------------------------#
@login_required(login_url='my-login')
def task_list(request):

    tasks = Task.objects.filter(user = request.user, state = 1).all()

    return render(request, 'task/task_list.html', {
        'tasks': tasks
    })

@login_required(login_url='my-login')
def task_detail(request, pk):

    task = Task.objects.filter(pk=pk, state = 1).get()

    return render(request, 'task/task_detail.html', {
        'task': task
    })

@login_required(login_url='my-login')
def task_create(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user

            form.save()

            messages.success(request, "The task was saved!")


            return redirect('tasks')

    return render(request, 'task/task_form.html', {
        'form': form
    })

@login_required(login_url='my-login')
def task_edit(request, pk):

    task = Task.objects.filter(user=request.user).get(pk=pk)

    form = TaskForm(instance= task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            form.save()

            messages.success(request, "The changes was saved!")

            return redirect('tasks')

    return render(request, 'task/task_form.html', {
        'form': form
    })

@login_required(login_url='my-login')
def task_delete(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    task.state = False
    task.save()

    messages.success(request, "The task was deleted!")
    return redirect('tasks')


#------------------------------------NOTES---------------------------------------#
@login_required(login_url='my-login')
def note_list(request):

    notes = Note.objects.filter(user=request.user, state=True).all()    

    return render(request, 'note/note_list.html', {
        'notes': notes
    })

@login_required(login_url='my-login')
def note_create(request):

    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)

        if form.is_valid():
            note = form.save(commit=False)

            note.user = request.user

            form.save()

            messages.success(request, "The note was added")

            return redirect('notes')


    return render(request, 'note/note_form.html', {
        'form': form
    })

@login_required(login_url='my-login')
def note_detail(request, pk):

    note = Note.objects.filter(user=request.user, state = True).get(pk=pk)

    return render(request, 'note/note_detail.html', {
        'note': note
    })

@login_required(login_url='my-login')
def note_delete(request, pk):

    note = Note.objects.filter(user = request.user).get(pk=pk)
    note.state = False
    note.save()

    messages.success(request, 'The note was deleted!')

    return redirect('notes')

@login_required(login_url='my-login')
def note_edit(request, pk):

    note = Note.objects.filter(user = request.user).get(pk=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)

        if form.is_valid():
            form.save(commit=False)

            messages.success(request, 'The changes was saved!')

            return redirect('notes')

    return render(request, 'note/note_form.html', {
        'form': form
    })


#------------------------------------CATEGORIES---------------------------------------#

@login_required(login_url='my-login')
def category_list(request):

    categories = Category.objects.filter(user = request.user, state = True).all()

    return render(request, 'category/category_list.html', {
        'categories': categories
    })

@login_required(login_url='my-login')
def category_create(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            category = form.save(commit=False)

            category.user = request.user
            
            category.save()

            messages.success(request, 'The category was added!')

            return redirect('categories')

    return render(request, 'category/category_form.html', {
        'form': form
    })

@login_required(login_url='my-login')
def category_edit(request, pk):

    category = Category.objects.filter(user = request.user, state = True).get(pk=pk)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():

            form.save()

            messages.success(request, 'The changes was saved!')

            return redirect('categories')

    return render(request, 'category/category_form.html', {
        'form': form
    })

@login_required(login_url='my-login')
def category_delete(request, pk):

    category = Category.objects.filter(user = request.user).get(pk=pk)

    category.state = False

    category.save()

    messages.success(request, 'The category was deleted!')

    return redirect('categories')
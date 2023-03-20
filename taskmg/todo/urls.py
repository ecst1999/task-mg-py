
from django.urls import path
from . import views

urlpatterns = [
    
    path('register', views.register),

    path('my-login', views.my_login),

    path('', views.home),

    # ------------------ CRUD operations --------------------- #

    # - CREATE task
    path('create-task', views.createTask, name='create-task'),

    # - READ task
    path('view-tasks', views.viewTasks, name='view-tasks'),

    # - UPDATE task
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),

    # - DELETE task

    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),

]


from django.urls import path
from . import views

urlpatterns = [        

    path('', views.home, name=''),

    # ----------------------Register a user--------------------------#

    path('register', views.register, name='register'),

    # ----------------------Login a user--------------------------#

    path('my-login', views.my_login, name='my-login'),

    # ----------------------Dashboard a user--------------------------#

    path('dashboard', views.dashboard, name='dashboard'),

    # --------------------------------TASKS------------------------------#
    
    # View Tasks
    path('tasks', views.task_list, name='tasks'),

    # ----------------------CREATE TASK--------------------------#
    path('create-task', views.createTask, name='create-task'),

    # ----------------------READ TASK--------------------------#

    path('view-tasks', views.viewTasks, name='view-tasks'),

    # ----------------------UPDATE TASK--------------------------#

    path('update-task/<str:pk>/', views.updateTask, name='update-task'),

    # ----------------------DELETE TASK--------------------------#
    
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),

    # ----------------------Logout a user--------------------------#
    
    path('user-logout', views.user_logout, name='user-logout'),
]

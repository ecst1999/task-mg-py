
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

    
    # ----------------------Logout a user--------------------------#
    
    path('user-logout', views.user_logout, name='user-logout'),

    # --------------------------------TASKS------------------------------#
    
    # View Tasks
    path('tasks', views.task_list, name='tasks'),

    # Task detail
    path('task/<str:pk>', views.task_detail, name='task-detail'),

    # Task create
    path('task-create', views.task_create, name='task-create'),

    # Task edit
    path('tast-edit/<str:pk>', views.task_edit, name='task-edit'),

    # Task delete 
    path('task-delete/<str:pk>', views.task_delete, name='task-delete'),


    # --------------------------------NOTES------------------------------#

    # View Notes
    path('notes', views.note_list, name='notes'),

    # Note create
    path('note-create', views.note_create ,name='note-create'),

    # Note Detail
    path('note/<str:pk>', views.note_detail, name='note-detail'),

]

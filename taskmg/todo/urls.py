
from django.urls import path
from . import views

urlpatterns = [        

    path('', views.home, name=''),

    # ----------------------Register a user--------------------------#

    path('register', views.register, name='register'),

    # ----------------------Login a user--------------------------#

    path('my-login', views.my_login, name='my-login'),

    
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

    # --------------------------------SUBTASK------------------------------#

    # Subtask detail
    path('subtask/<str:pkT>/<str:pk>', views.subtask_detail, name='subtask-detail'),
    
    # SubTask Create
    path('subtask-create/<str:pk>', views.subtask_create, name='subtask-create'),

    # SubTask Edit
    path('subtask-edit/<str:pkT>/<str:pk>', views.subtask_edit, name='subtask-edit'),

    # Subtask Delete
    path('subtask-delete/<str:pkT>/<str:pk>', views.subtask_delete, name='subtask-delete'),


    # --------------------------------NOTES------------------------------#

    # View Notes
    path('notes', views.note_list, name='notes'),

    # Note Detail
    path('note/<str:pk>', views.note_detail, name='note-detail'),

    # Note create
    path('note-create', views.note_create ,name='note-create'),

    # Note edit
    path('note-edit/<str:pk>', views.note_edit, name='note-edit'),

    # Note Delete
    path('note-detele/<str:pk>', views.note_delete ,name='note-delete'),

    # --------------------------------CATEGORIES------------------------------#

    # View Categories
    path('categories', views.category_list, name='categories'),

    # Category Detail 
    path('category-edit/<str:pk>', views.category_edit, name='category-edit'),

    # Category create
    path('category-create', views.category_create, name='category-create'),

    # Category delete
    path('category-delete/<str:pk>', views.category_delete, name='category-delete'),

    # --------------------------------NOTIFICATIONS------------------------------#

    # View Notifications
    path('notifications', views.notifications, name='notifications'),

    # Notificiation Detail
    path('notification/<str:pk>', views.notification_detail, name='notification-detail'),
]

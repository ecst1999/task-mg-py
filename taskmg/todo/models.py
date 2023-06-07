from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    state = models.BooleanField(default=True)

class Status(models.Model):

    description = models.TextField(null=False)
    color = models.CharField(max_length=50, null=False)
    state = models.BooleanField(default=True)
    
class Task(models.Model):

    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    location = models.CharField(max_length=150, null=True)
    date_finished = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)
    icon = models.CharField(max_length=25, null=True)
    priority = models.CharField(max_length=250, default="Baja")
    state = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    files = models.FileField(null=True, blank=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Notification(models.Model):

    notification = models.CharField(max_length=150, null=False)
    type_notification = models.CharField(max_length=100, null=False)
    state = models.BooleanField(default=True)
    is_readead = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notifications')

class Subtask(models.Model):

    name = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True)
    date_finished = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)
    priority = models.CharField(max_length=250)
    state = models.BooleanField(default=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='subtasks')

class Note(models.Model):

    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=1000, null=True)
    tags = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    files = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notes')

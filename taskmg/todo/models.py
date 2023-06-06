from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 1
    USER = 2
    GUEST = 3

    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (USER, 'User'),
        (GUEST, 'Guest')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

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
    location = models.CharField(max_length=150)
    date_finished = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)
    icon = models.CharField(max_length=25)
    priority = models.CharField(max_length=250)
    state = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    files = models.FileField()
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Notification(models.Model):

    notification = models.CharField(max_length=150)
    type_notification = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notifications')

class Role(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

class Subtask(models.Model):

    name = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True)
    date_finished = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)
    priority = models.CharField(max_length=250)
    state = models.BooleanField(default=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='subtasks')
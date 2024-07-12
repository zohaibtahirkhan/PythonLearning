from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homepage')


class Task(models.Model):
    title = models.CharField(max_length=500)
    objective = models.TextField()
    done = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks', kwargs={"pk": self.list.id})

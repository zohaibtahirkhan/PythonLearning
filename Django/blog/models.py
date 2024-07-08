from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', null=True, blank=True)

    def __str__(self):
        return self.title


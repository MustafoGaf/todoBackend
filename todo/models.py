from django.db import models
from django.contrib.auth.models import User



class Todos(models.Model):
    todo = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    fk_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.todo
    
class Users(models.Model):
    username = models.CharField()
    password1 = models.CharField()
    password = models.CharField()
    email = models.EmailField()
    
class Password(models.Model):
    username = models.CharField()
    email = models.EmailField()
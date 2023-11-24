from django.db import models

class Customer(models.Model):
	first_name = models.CharField("First name", max_length=255)
	last_name = models.CharField("Last name", max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address =  models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	createdAt = models.DateTimeField("Created At", auto_now_add=True)
	
	def __str__(self):
		return self.first_name

class Users(models.Model):
    first_name = models.CharField("Surnmae", max_length=255)
    name = models.CharField("Name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    
    def __str__(self):
        return self.name

class Todos(models.Model):
    todo = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    fk_user = models.ForeignKey('Users', on_delete=models.PROTECT, null=True)

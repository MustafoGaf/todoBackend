from django.contrib import admin
from .models import Users, Todos
# Register your models here.
admin.site.register([Users, Todos])
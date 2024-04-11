from rest_framework import serializers
from .models import Users, Todos, Password, AllUsers
from django.contrib.auth.models import User
# class UsersSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Users
#         fields = ('pk', 'first_name', 'name', 'email', 'phone')
        
class TodosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todos
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = '__all__'
        
class AllUsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AllUsers
        fields = '__all__'
        
class CurrentUsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('is_staff', 'username')
        
     
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'
        
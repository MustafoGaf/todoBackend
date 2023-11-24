from rest_framework import serializers
from .models import Users, Todos, Password

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
        
        
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'
        
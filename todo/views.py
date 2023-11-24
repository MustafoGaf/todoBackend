from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Todos, Users
from django.db.utils import IntegrityError
from .serializers import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    """
 List  customers, or create a new customer.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        user = request.user
        
        todos = user.todos_set.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(todos, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = TodosSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/todos/?page=' + str(nextPage), 'prevlink': '/api/todos/?page=' + str(previousPage)})

    elif request.method == 'POST':
        print()
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def users_list(request):
    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            print('>>', serializer.data)
            try:
                user = User.objects.create_user(username=serializer.data["username"], email=serializer.data["email"], password=serializer.data["password1"])
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        # user = User.objects.create_user(username=serializer.data.username, password=serializer.data.password1)
        # user.save()
        else:
             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            
        
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todos_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        todo = Todos.objects.get(pk=pk)
    except Todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodosSerializer(todo,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(">>1")
        serializer = TodosSerializer(todo, data=request.data,context={'request': request})
        if serializer.is_valid():
            print(">>2")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])    
def forgotURL(request):
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
            print('>>', serializer.data)
            try:
                user = User.objects.get(username = serializer.data["username"])
                if user:
                    encoded_pk = urlsafe_b64encode(force_bytes(user.pk))
                    token = PasswordResetTokenGenerator().make_token(user)
                    print("????? >> ", str(encoded_pk))
                    refresh = f'http:localhost:8000/password-reset/{encoded_pk}/{token}/'
                    print(refresh)
                    return Response(refresh, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        # user = User.objects.create_user(username=serializer.data.username, password=serializer.data.password1)
        # user.save()
       
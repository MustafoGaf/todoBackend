"""
URL configuration for djangoreactproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
from todo import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordContextMixin, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/todos/$', views.todo_list),
    re_path(r'^auth/me/$', views.info_user),
    
    re_path('^api/admin/todos/$', views.all_todo_list),
    re_path('^api/admin/users/$', views.all_users_list),
    
    re_path(r'^api/users/$', views.users_list),
	re_path(r'^api/todos/(?P<pk>[0-9]+)$', views.todos_list),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/forgot/', views.forgotURL), 
    path("password-reset/", auth_views.PasswordResetView.as_view()),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view()), 
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view()), 
     
    path("password-reset/<uidb64>/<token>/",  auth_views.PasswordResetConfirmView.as_view()),
    path('house/', include('house.urls')),
    
    # path('password-reset/<str:encoded_pk>/<str:token>/'name="jhkjhjk")
 
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

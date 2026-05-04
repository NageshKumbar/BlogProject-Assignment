# blogapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_blog, name='create'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
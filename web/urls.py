from django.urls import path
from django.contrib.auth import views
from .views import index

urlpatterns = [
    path('login/', views.auth_logout, name='login'),
    path('', index, name='index'),
]

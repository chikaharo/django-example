from django.urls import path
from freshapp import views

urlpatterns = [
    path('', views.users, name='user'),
]
from django.urls import path
from .views import my_view

urlpatterns = [
    path('con-task/', my_view, name='con_task'),
]

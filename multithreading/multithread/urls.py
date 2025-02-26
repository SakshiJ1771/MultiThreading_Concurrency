from django.urls import path
from .views import my_view

urlpatterns = [
    path('run-task/', my_view, name='run_task'),
]

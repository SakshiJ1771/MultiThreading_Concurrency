from django.urls import path
from .views import MultithreadingExample

urlpatterns = [
    path('api/multithreading/', MultithreadingExample.as_view(), name='multithreading_example'),
]
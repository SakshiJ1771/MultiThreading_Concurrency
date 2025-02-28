from django.urls import path
from .views import multithreading_view

urlpatterns = [
    path("multithreading/", multithreading_view, name="multithreading"),
]

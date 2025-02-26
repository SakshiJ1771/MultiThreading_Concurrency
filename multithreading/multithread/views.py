from django.shortcuts import render
from django.http import JsonResponse
import threading
import time

# Create your views here.
def heavy_task():
    print("Task started")
    time.sleep(5)  
    print("Task completed")

def my_view(request):
    thread = threading.Thread(target=heavy_task)
    thread.start()

    return JsonResponse({"message": "Task started in the background!"})


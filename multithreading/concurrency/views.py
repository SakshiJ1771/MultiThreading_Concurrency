from django.shortcuts import render
from django.http import JsonResponse
from concurrent.futures import ThreadPoolExecutor
import time

# Create your views here.
executor = ThreadPoolExecutor(max_workers=3)

def heavy_task(task_id):
    print(f"Task {task_id} started")
    time.sleep(5)
    print(f"Task {task_id} completed")
    return f"Task {task_id} done"

def my_view(request):
    future = executor.submit(heavy_task, task_id=1)
    return JsonResponse({"message": "Task is running in the background!"})


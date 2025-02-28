
from django.shortcuts import render
from django.http import JsonResponse
from concurrent.futures import ThreadPoolExecutor
from multithreading_app.models import Task
import time

def fetch_task(task):
    time.sleep(2)
    return {"id": task.id, "title": task.title, "Completed": task.is_completed}

def multithreading_view(request):
    tasks = list(Task.objects.all())  # Fetch all tasks first
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_task, tasks))  # Fetch task details in parallel
    return JsonResponse({"tasks": results})


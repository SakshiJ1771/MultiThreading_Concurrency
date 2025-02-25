import threading
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def perform_task(thread_id):
    # Simulating a long-running task
    print(f"Task started by thread {thread_id}")
    import time
    time.sleep(5)
    print(f"Task completed by thread {thread_id}")

class MultithreadingExample(APIView):
    def get(self, request):
        threads = []
        for i in range(3):  # Start 3 threads as an example
            thread = threading.Thread(target=perform_task, args=(i,))
            threads.append(thread)
            thread.start()

        # Join all threads to ensure they complete before sending response
        for thread in threads:
            thread.join()

        return Response({"message": "Multithreading tasks completed!"}, status=status.HTTP_200_OK)

from django.shortcuts import render
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from concurrency_app.models import Product  # Ensure correct import

async def async_db_query(request):
    # Convert synchronous ORM query to asynchronous
    products = await sync_to_async(list)(Product.objects.all())  

    data = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    return JsonResponse({"products": data})

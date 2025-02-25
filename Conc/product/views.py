# product/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    # Deserialize the incoming data using the ProductSerializer
    serializer = ProductSerializer(data=request.data)
    
    # Validate the data
    if serializer.is_valid():
        # Save the new product to the database
        serializer.save()
        # Return the serialized product data with HTTP 201 (Created)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # If data is invalid, return errors with HTTP 400 (Bad Request)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    # Check if the version in the request matches the product's version
    if product.version != request.data.get('version'):
        # Send back the current product data so the user can compare it
        return Response({
            "detail": "Version conflict. Please refresh and try again.",
            "current_data": ProductSerializer(product).data  # Include current product data
        }, status=status.HTTP_409_CONFLICT)

    # If versions match, proceed with updating the product
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

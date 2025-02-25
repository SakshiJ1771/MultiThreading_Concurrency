# product/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/<int:pk>/update/', views.product_update, name='product-update'),
    path('products/', views.product_create, name='product-create'),  # Added URL for creating a product
]

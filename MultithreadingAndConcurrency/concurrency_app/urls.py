from django.urls import path
from .views import async_db_query

urlpatterns = [
    path("async-db/", async_db_query, name="async-db"),
]

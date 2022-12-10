from django.urls import path
from .views import get_last_order

urlpatterns = [
    path('/get', get_last_order)
]

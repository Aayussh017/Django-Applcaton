# employee/urls.py

from django.urls import path
from .views import add_employee, remove_employee, view_employee, list_employees

urlpatterns = [
    path('add/', add_employee, name='add_employee'),
    path('remove/', remove_employee, name='remove_employee'),
    path('view/', view_employee, name='view_employee'),
    path('list/', list_employees, name='list_employees'),
]

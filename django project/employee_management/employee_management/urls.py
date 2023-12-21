# employee_management/urls.py

from django.contrib import admin
from django.urls import include, path
from employee.views import list_employees, add_employee, remove_employee, view_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('employee/add/', add_employee, name='add_employee'),
    path('employee/remove/', remove_employee, name='remove_employee'),
    path('employee/view/', view_employee, name='view_employee'),
    path('employee/list/', list_employees, name='list_employees'),
    path('', list_employees, name='home'),  # Add this line for the empty path
    # Add other app URLs as needed
]

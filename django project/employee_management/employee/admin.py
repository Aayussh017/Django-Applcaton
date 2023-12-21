# employee_management/employee/admin.py

from django.contrib import admin
from .models import Employee  # Update this line

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'department')

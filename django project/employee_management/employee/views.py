# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from . import views


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('list_employees')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def remove_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employee = get_object_or_404(Employee, name=name)
        employee.delete()
        return redirect('list_employees')
    return render(request, 'remove_employee.html')

def view_employee(request):
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            employee = Employee.objects.get(name=name)
            return render(request, 'view_employee.html', {'employee': employee})
        except Employee.DoesNotExist:
            error_message = f"No employee found with the name '{name}'."

    return render(request, 'view_employee.html', {'error_message': error_message})

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'list_employees.html', {'employees': employees})

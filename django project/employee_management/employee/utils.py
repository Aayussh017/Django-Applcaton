from .models import Employee

def create_employee(name, age, department):
    employee = Employee.objects.create(name=name, age=age, department=department)
    return employee

def remove_employee(name):
    try:
        employee = Employee.objects.get(name=name)
        employee.delete()
        return True
    except Employee.DoesNotExist:
        return False

def view_employee(name):
    try:
        employee = Employee.objects.get(name=name)
        return f"Name: {employee.name}, Age: {employee.age}, Department: {employee.department}"
    except Employee.DoesNotExist:
        return "Employee not found"

def list_employees():
    employees = Employee.objects.all()
    return employees

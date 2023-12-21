# Import the Employee model from models.py
from employee.models import Employee
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Manage employees'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help='Available actions: add, remove, view, list, update')

    def handle(self, *args, **options):
        action = options['action']

        try:
            if action == 'add':
                # Prompt the user for employee details
                name = input('Enter employee name: ')
                age = int(input('Enter employee age: '))
                department = input('Enter employee department: ')

                # Create an employee in the database
                employee = Employee.objects.create(name=name, age=age, department=department)

                # Display a success message
                self.stdout.write(self.style.SUCCESS(f'Employee "{employee.name}" added successfully!'))

            elif action == 'remove':
                # Prompt the user for the name of the employee to remove
                name_to_remove = input('Enter the name of the employee to remove: ')

                try:
                    # Retrieve the employee from the database
                    employee = Employee.objects.get(name=name_to_remove)

                    # Remove the employee
                    employee.delete()

                    # Display a success message
                    self.stdout.write(self.style.SUCCESS(f'Employee "{name_to_remove}" removed successfully!'))

                except Employee.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Employee "{name_to_remove}" not found.'))

            elif action == 'view':
                # Prompt the user for the name of the employee to view
                name_to_view = input('Enter the name of the employee to view: ')

                try:
                    # Retrieve the employee from the database
                    employee = Employee.objects.get(name=name_to_view)

                    # Display employee information
                    self.stdout.write(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Department: {employee.department}")

                except Employee.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Employee "{name_to_view}" not found.'))

            elif action == 'list':
                # Retrieve all employees from the database
                employees = Employee.objects.all()

                # Display employee information in a tabular format
                self.stdout.write("Employee List:")
                for employee in employees:
                    self.stdout.write(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Department: {employee.department}")

            elif action == 'update':
                # Prompt the user for employee name to update
                name_to_update = input('Enter the name of the employee to update: ')

                try:
                    # Retrieve the employee from the database
                    employee = Employee.objects.get(name=name_to_update)

                    # Prompt for updated information
                    updated_name = input('Enter updated name (press Enter to keep the current name): ')
                    updated_age = int(input('Enter updated age (press Enter to keep the current age): '))
                    updated_department = input('Enter updated department (press Enter to keep the current department): ')

                    # Update employee information
                    if updated_name:
                        employee.name = updated_name
                    if updated_age:
                        employee.age = updated_age
                    if updated_department:
                        employee.department = updated_department

                    employee.save()

                    # Display a success message
                    self.stdout.write(self.style.SUCCESS(f'Employee "{name_to_update}" updated successfully!'))

                except Employee.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Employee "{name_to_update}" not found.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {e}'))

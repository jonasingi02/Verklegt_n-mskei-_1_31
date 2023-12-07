from data.EmployeeData import EmployeeData
from model.employee import Employee

class EmployeeLogic:
    def __init__(self):
        print("inside Logic")
        self.employee_data = EmployeeData()

    def create_employee(self, employee):
        """Takes an employee as an object and forwards it to the data layer"""
        self.employee_data.create_customer(employee)

    def get_all_employees(self):
        return self.employee_data.get_all_employees()
      




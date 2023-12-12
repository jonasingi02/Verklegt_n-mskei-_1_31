from data.EmployeeData import EmployeeData
from model.employee import Employee
from data.data_wrapper import data_wrapper

class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def create_employee(self, employee):
        """Takes an employee as an object and forwards it to the data layer"""
        self.data_wrapper.create_employee(employee)

    def update_employee(self, kt_employee_to_update, column_to_update, new_info):
        self.data_wrapper.update_employee(kt_employee_to_update, column_to_update, new_info)

    def read_all_employees(self):
        return self.data_wrapper.read_all_employees()
      




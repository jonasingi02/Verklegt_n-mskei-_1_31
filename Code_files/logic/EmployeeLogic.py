from data.EmployeeData import EmployeeData
from model.employee import Employee

class EmployeeLogic:
    def __init__(self, data_connection):
        print("inside Logic")
        self.data_wrapper = data_connection
        

    def create_employee(self, employee):
        """Takes an employee as an object and forwards it to the data layer"""
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
      




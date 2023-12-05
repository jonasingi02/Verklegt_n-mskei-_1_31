from Code_files.data.EmployeeData import EmployeeData
from Code_files.model.employee import Employee

class EmployeeLogic:
    def __init__(self):
        print("inside Logic")
        self.employee_data = EmployeeData()

    def create_employee(self, employee):
        """Takes an employee as an object and forwards it to the data layer"""
        pass

    def get_all_employees(self): 
        return self.employee_data.create_employee()




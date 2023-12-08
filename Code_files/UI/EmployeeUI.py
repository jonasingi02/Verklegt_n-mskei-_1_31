from data.EmployeeData import EmployeeData


class EmployeeUI:
    def __init__(self):
        print("inside UI")
        self.employee_data = EmployeeData()

    def input_prompt(self):
        print("Employee")
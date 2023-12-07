from logic.logic_wrapper import Logic_wrapper
from logic.logic_wrapper import Logic_wrapper
class EmployeeUI:
    def __init__(self):
        print("inside UI")
        self.logic_wrapper = Logic_wrapper()


    def input_prompt(self):
        print("Employee")
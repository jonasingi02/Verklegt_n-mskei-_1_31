from .plane_logic import plane_logic
from .destination_logic import destination_logic
from .EmployeeLogic import EmployeeLogic
from .fmvoyage_logic import FmvoyageLogic
from data.data_wrapper import data_wrapper

class Logic_wrapper:
    def __init__(self):
        self.data_wrapper = data_wrapper()
        self.plane_logic = plane_logic(self.data_wrapper)
        self.destination_logic = destination_logic(self.data_wrapper)
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.fmvoyage_logic = FmvoyageLogic(self.data_wrapper)


    def create_plane(self, plane):
        """Takes in a plane object and forwards it to the data layer"""
        return self.plane_logic.create_plane(plane)

    def get_all_planes(self):
        return self.plane_logic.get_all_planes()
    
    def create_destination(self, destination):
        """Takes in a destination object and forwards it to the data layer"""
        return self.destination_logic.create_destination(destination)
    
    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()
    
    def create_employee(self, employee):
        return self.employee_logic.create_employee(employee)
    
    def update_employee(self,kt_employee_to_update, column_to_update, new_info):
        return self.employee_logic.update_employee(kt_employee_to_update, column_to_update, new_info)

    def read_all_employees(self):
        return self.employee_logic.read_all_employees()
    
    def get_all_pilots(self): 
        return self.employee_logic.get_all_pilots()
    
    def get_all_fmvoyages(self):
        return self.fmvoyage_logic.get_all_fmvoyages()
    
    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_all_flight_attendants(self): 
        return self.employee_logic.get_all_flight_attendantds()
    
from data.EmployeeData import EmployeeData
from data.plane_data import PlaneData
from data.destination_data import destination_data
from data.fmvoyage_data import FmvoyageData


class data_wrapper:
    def __init__(self):
        self.plane_data = PlaneData()
        self.destination_data = destination_data()
        self.employee_data = EmployeeData()
        self.FmvoyageData = FmvoyageData()

    def get_all_planes(self):
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)

    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()

    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def get_certain_employee(self, name):
        return self.employee_data.get_certain_employee(name)
    
    def read_all_employees(self):
        return self.employee_data.read_all_employees()
    
    def create_employee(self, employee): 
        return self.employee_data.create_employee(employee)
    
    def update_employee(self,kt_employee_to_update, column_to_update, new_info):
        return self.employee_data.update_employee(kt_employee_to_update, column_to_update, new_info)

    def create_fmvoyage(self, fmvoyage):
        return self.FmvoyageData.create_fmvoyage(fmvoyage)
    
    def read_all_fmvoyages(self):
        return self.FmvoyageData.read_all_fmvoyages()

    def create_voyagexpilot(self, vxp):
        return self.FmvoyageData.create_voyagexpilot(vxp)
    
    def get_all_voyagexpilots(self):
        return self.FmvoyageData.read_all_voyagexpilots()
    
    def get_all_pilots(self):
        return self.employee_data.read_all_pilots()
    
    def get_all_flight_attendants(self):
        return self.employee_data.read_all_flight_attendants()
        
    def get_all_voyagexattendants(self):
        return self.FmvoyageData.read_all_voyagexattendants()
    
    def create_voyagexattendant(self, vxa):
        return self.FmvoyageData.create_voyagexattendant(vxa)

    def read_all_fmvoyages(self):
        return self.FmvoyageData.read_all_fmvoyages()
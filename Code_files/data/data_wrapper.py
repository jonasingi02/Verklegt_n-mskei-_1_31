from data.EmployeeData import EmployeeData
from data.plane_data import PlaneData
from data.destination_data import destination_data


class data_wrapper:
    def __init__(self):
        self.plane_data = PlaneData()
        self.destination_data = destination_data()
        self.employee_data = EmployeeData()

    def get_all_planes(self):
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)

    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()

    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def get_all_employees(self):
        return self.employee_data.get_all_employees()
    
    def create_employee(self, employee): 
        return self.employee_data.create_empoyee(employee)



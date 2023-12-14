from data.plane_data import PlaneData
from data.destination_data import destination_data


class data_wrapper:
    def __init__(self):
        self.plane_data = PlaneData()
        self.destination_data = destination_data()

    def get_all_plane(self):
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def create_destination(self, destination):
<<<<<<< Updated upstream
        return self.destination_data.create_destination(destination)
=======
        return self.destination_data.create_destination(destination)
    
    def get_certain_employee(self, kt):
        return self.employee_data.get_certain_employee(kt)
    
    def read_all_employees(self):
        return self.employee_data.read_all_employees()
    
    def create_employee(self, employee): 
        return self.employee_data.create_employee(employee)
    
    def update_employee(self,kt_employee_to_update, column_to_update, new_info):
        return self.employee_data.update_employee(kt_employee_to_update, column_to_update, new_info)

    def create_fmvoyage(self, fmvoyage):
        return self.FmvoyageData.create_fmvoyage(fmvoyage)
    
    def get_all_fmvoyages(self):
        return self.FmvoyageData.read_all_fmvoyages()
    
    def get_all_voyagexpilots(self): 
        return self.FmvoyageData.read_all_voyagexpilots()

    def create_voyagexpilots(self, vxp):
        return self.FmvoyageData.create_voyagexpilots(vxp)
    
    def get_all_voyagesxflightattendants(self):
        return self.FmvoyageData.read_all_voyage_voyagexattendant()
    
   

    
>>>>>>> Stashed changes

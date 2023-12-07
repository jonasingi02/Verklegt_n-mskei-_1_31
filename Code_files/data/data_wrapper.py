from data.plane_data import plane_data
from data.destination_data import destination_data


class data_wrapper:
    def __init__(self):
        self.plane_data = plane_data()
        self.destination_data = destination_data()

    def get_all_plane(self):
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
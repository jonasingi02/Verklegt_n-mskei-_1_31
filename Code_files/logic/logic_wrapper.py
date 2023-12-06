from .plane_logic import plane_logic
from data.data_wrapper import data_wrapper

class Logic_wrapper:
    def __init__(self):
        self.data_wrapper = data_wrapper()
        self.plane_logic = plane_logic(self.data_wrapper)

    def create_plane(self, plane):
        """Takes in a customer object and forwards it to the data layer"""
        return self.plane_logic.create_plane(plane)

    def get_all_planes(self):
        return self.plane_logic.get_all_planes()
from model.planes import Planes
from data.plane_data import plane_data


class plane_logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_plane(self, plane):
        """hjalp"""

        self.data_wrapper.create_plane(plane)

    def get_all_customers(self):
        return self.data_wrapper.get_all_planes()

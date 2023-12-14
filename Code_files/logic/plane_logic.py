from model.planes import Planes
from data.plane_data import PlaneData


class PlaneLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_plane(self, plane):
        self.data_wrapper.create_plane(plane)

    def get_all_planes(self):
        return self.data_wrapper.get_all_planes()

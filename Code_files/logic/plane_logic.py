from model.planes import Planes
from data.plane_data import PlaneData


class PlaneLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_plane(self, plane):
        """
        Creates a new plane record in the data source.

        Args:
            plane (Plane): An object representing the plane details to be created in the data source.
        """
        self.data_wrapper.create_plane(plane)

    def get_all_planes(self):
        """
        Retrieves a list of all plane records from the data source.

        Returns:
            List[Plane]: A list of Plane objects representing all planes in the data source.
        """
        return self.data_wrapper.get_all_planes()

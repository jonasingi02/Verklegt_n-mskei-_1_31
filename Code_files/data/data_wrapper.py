from data.plane_data import plane_data


class data_wrapper:
    def __init__(self):
        self.plane_data = plane_data()

    def get_all_plane(self):
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        return self.plane_data.create_plane(plane)
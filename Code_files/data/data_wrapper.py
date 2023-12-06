from data.plane_data import plane_data


class data_wrapper:
    def __init__(self):
        self.plane_data = plane_data()

    def get_all_customers(self):
        return self.plane_data.read_all_planes()

    def create_customer(self, customer):
        return self.plane_data.create_plane(customer)
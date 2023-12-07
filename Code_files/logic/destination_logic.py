from model.destination import destination
from data.destination_data import destination_data

class destination_logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        """hjalp"""

        self.data_wrapper.create_destination(destination)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()
from model.destination import destination
from data.destination_data import destination_data

class destination_logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        """ 
        Delegates the creation of a new destination record to the data wrapper.

        Args:
            destination (Destination): The destination object to be added.
        """
        self.data_wrapper.create_destination(destination)

    def get_all_destinations(self):
        """ 
        Retrieves all destination records via the data wrapper.

        Returns:
           list[Destination]: A list of all destination objects.
        """
        return self.data_wrapper.get_all_destinations()
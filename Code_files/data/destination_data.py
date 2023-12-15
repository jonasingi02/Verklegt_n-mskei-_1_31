import csv
from model.destination import destination

class destination_data:
    def __init__(self):
        self.file_name = "data/files/destinations.csv"
    
    def read_all_destinations(self):
        """ 
        Pares a CSV file and returns a list of destinations as objects

        Returns:
            List[destination]: Object representing destinations with atriubtes like countries, airport and ect.
        """
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile1:
            reader = csv.DictReader(csvfile1)
            for row in reader:
                ret_list.append(destination(row["country"], row["airport"], row["flighttime"], row["distance"], row["name"], row["phone"]))
        return ret_list
    
    
    def create_destination(self, destination):
        """
        Appends a new destination as an object to the csv file.

        Args:
            destination (Destination): The destinations object to be added to the csv file.
        """
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["country", "airport", "flighttime", "distance", "name", "phone"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'country': destination.country, 
                'airport': destination.airport, 
                'flighttime': destination.flighttime, 
                'distance': destination.distance,
                'name': destination.name,
                'phone': destination.phone
                })

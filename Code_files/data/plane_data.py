import os
import csv
from model.planes import Planes

class PlaneData:
    def __init__(self):
        self.file_name = "data/files/planes.csv"
    
    def read_all_planes(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Planes(row["name"], row["type"], row["numseats"], row["manufacturer"]))
        return ret_list
    
    def create_plane(self, plane):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "type", "numseats", "manufacturer"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': plane.name, 'type': plane.type, 'numseats': plane.numseats, 'manufacturer': plane.manufacturer})

import os
import csv
from model.planes import Planes


class PlaneData:
    def __init__(self):
        self.file_name = "data/files/planes.csv"

    def read_all_planes(self):
        """
        Reads plane data from a CSV file and returns a list of planes objects.

        Returns:
            list[Planes]: A list of planes objects with details like name, type, number of seats, and manufacturer.
        """
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile1:
            reader = csv.DictReader(csvfile1)
            for row in reader:
                ret_list.append(
                    Planes(
                        row["name"], row["type"], row["numseats"], row["manufacturer"]
                    )
                )
        return ret_list

    def create_plane(self, plane):
        """
        Appends a new plane's data to a CSV file.

        Args:
            plane (Plane): An object representing a plane. Containing details like name, type, number of seats, and manufacturer.
        """
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile2:
            fieldnames = ["name", "type", "numseats", "manufacturer"]
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)

            writer.writerow(
                {
                    "name": plane.name,
                    "type": plane.type,
                    "numseats": plane.numseats,
                    "manufacturer": plane.manufacturer,
                }
            )

import csv
from model.FMVoyage import FMvoyage
from model.voyagexpilots import voyagexpilots
from model.voyagexattendant import voyagexattendant as vxa
import os


class FmvoyageData:
    def __init__(self):
        self.file_name = "data/files/fmvoyage.csv"
        self.file_name2 = "data/files/voyagexpilots.csv"
        self.file_name3 = "data/files/voyagexattendants.csv"
        self.update_file = "fmvoyage.csv"

    def read_all_fmvoyages(self):
        """
        Reads FMvoyage data from a CSV and returns a list of FMvoyages as objects.

        Returns:
            list[FMvoyage]: A list of FMvoyages as objescts with details like id, date, time ect. 
        """
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    FMvoyage(
                        row["id"], row["date"], row["time"], row["plane"], row["airport"]
                    )
                )
        return ret_list

    def create_fmvoyage(self, fmvoyage):
        """ 
        Adds a new object to FMvoyages data to a CSV file.

        Args:
            fmvoyage (FMvoygae): An object representing a voyage with details like id, date, time, plane, and airport.
        """
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "date", "time", "plane", "airport"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": fmvoyage.id,
                    "date": fmvoyage.date,
                    "time": fmvoyage.time,
                    "plane": fmvoyage.plane,
                    "airport": fmvoyage.airport
                }
            )
    
    def create_voyagexpilot(self, vxp):
        """ 
        Appends a pilot x voyage association to a CSV file.

        Args:
            vxp (VoyagesxPilots): An object representing the association bettween a voyage and a pilot.
            Details like the pilots id, personal ID (kt) and the pilot's status
        """
        with open(self.file_name2, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "kt", "main_pilot"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": vxp.id,
                    "kt": vxp.kt,
                    "main_pilot": vxp.main_pilot
                }
            )

    def read_all_voyagexpilots(self):
        """ 
        Reads voyage x pilts association data from a CSV file and returns voyagesxpilots as objects.

        Returns:
            list[voyagexpilots]: A list of voyagexpilots as objects representing an association bettween a voyage and a pilot.
        """
        ret_list = []
        with open(self.file_name2, newline="", encoding="utf-8") as csvfile2:
            reader = csv.DictReader(csvfile2)
            for row in reader:
                ret_list.append(
                    voyagexpilots(
                        row["id"], row["kt"], row["main_pilot"]
                    )
                )
        return ret_list
    
    def read_all_voyagexattendants(self):
        """
        Reads voyage x flightattendants association data from a CSV file.


        Returns:
            list[vxa]: A list of voyage x flightattendants as objects, each representing an association between a voyage and a flight attendant.
        """
        ret_list = []
        with open(self.file_name3, newline="", encoding="utf-8") as csvfile3:
            reader = csv.DictReader(csvfile3)
            for row in reader:
                ret_list.append(
                    vxa(
                        row["id"], row["kt"], row["main_attendant"]
                    )
                )
        return ret_list
    
    def create_voyagexattendant(self, vxa):
        """ 
        Appends a new voyage x flightattendant association to a CSV file.

        Args:
            vxa (VoyageXAttendant): An object representing the association between a voyage and a flight attendant. 
            Containing details like id, attendant's personal ID (kt), and main attendant status.
        """
        with open(self.file_name3, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "kt", "main_attendant"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": vxa.id,
                    "kt": vxa.kt,
                    "main_attendant": vxa.main_attendant
                }
            )


    def update_flight_info(self, flight_id_to_update, column_to_update, new_info):
        """ 
        Updates specific information for a flight in a CSV file based on the flight ID.

        Args:
            flight_id_to_update (str): The ID of the flight to be updated.
            column_to_update (int): The index of the column where the information needs to be updated.
            new_info (str): The new information to replace the existing data.

        Note:
            The function checks if a certain flight ID exists as well as specified column before updating.
            If the flight ID is found and the column is valid, it updates the data and writes it back to the CSV file.
        """

        file_name = "data/files/" + self.update_file    
        with open(self.file_name, 'r+', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        
        valid = False
        for row in rows:

            if len(row) >= 0 and row[0] == flight_id_to_update:
                valid = True

                if row[column_to_update] in row:
                    row[column_to_update] = new_info
            
        if valid:
            update_employee_path = "data/files/new_" + self.update_file
            with open(update_employee_path, 'w', newline='') as file_name:
                writer = csv.writer(file_name)
                writer.writerows(rows)
            os.replace(update_employee_path, self.file_name)


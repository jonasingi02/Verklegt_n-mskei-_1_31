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
        ret_list = []
        with open(self.file_name2, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    voyagexpilots(
                        row["id"], row["kt"], row["main_pilot"]
                    )
                )
        return ret_list
    
    def read_all_voyagexattendants(self):
        ret_list = []
        with open(self.file_name3, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    vxa(
                        row["id"], row["kt"], row["main_attendant"]
                    )
                )
        return ret_list
    
    def create_voyagexattendant(self, vxa):
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


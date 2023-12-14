import csv
from model.FMVoyage import FMvoyage
from model.voyagexattendant import voyagexattendant
from model.voyagexpilots import voyagexpilots


class FmvoyageData:
    def __init__(self):
        self.file_name = "data/files/fmvoyage.csv"
        self.file_name2 = "data/files/voyagexpilots.csv"
        self.file_name3 =  "data/files/voyagexflightattendants.csv"

    def read_all_fmvoyages(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    FMvoyage(
                        row["id"], row["date"], row["plane"], row["airport"]
                    )
                )
        return ret_list

    def create_fmvoyage(self, fmvoyage):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "date", "plane", "airport"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": fmvoyage.id,
                    "date": fmvoyage.date,
                    "plane": fmvoyage.plane,
                    "airport": fmvoyage.airport
                }
            )
    
    def create_voyagexpilots(self, vxp):
        with open(self.file_name2, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "kt"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": vxp.id,
                    "kt": vxp.kt
                }
            )

    def read_all_voyagexpilots(self):
        ret_list = []
        with open(self.file_name3, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    voyagexpilots(
                        row["id"], row["kt"]
                    )
                )
        return ret_list
    
    def create_voyagexattendant(self, voyagexattendant):

        with open(self.file_name3, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["vid", "attendant"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                "vid": voyagexattendant.vid,
                "attendant": voyagexattendant.attendant
            })

    def read_all_voyage_voyagexattendant(self):
        ret_list = []
        with open(self.file_name3, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                   voyagexattendant(
                        row["id"], row["attendant"]
                    )
                )
        return ret_list
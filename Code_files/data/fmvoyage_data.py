import csv
from model.FMVoyage import FMvoyage


class FmvoyageData:
    def __init__(self):
        self.file_name = "data/files/fmvoyage.csv"

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

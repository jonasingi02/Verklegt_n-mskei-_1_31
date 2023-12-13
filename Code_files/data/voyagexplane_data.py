import csv
from model.voyagexpilots import voyagexpilots


class voyagexplaneData:
    def __init__(self):
        self.file_name = "data/files/voyagexplane.csv"

    def read_all_voyagexplane(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    vo(
                        row["vid"], row["plane"]
                    )
                )
        return ret_list

    def create_voyagexplane(self, voyagexplane):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["vid", "plane"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "vid": voyagexplane.vid,
                    "plane": voyagexplane.plane
                }
            )

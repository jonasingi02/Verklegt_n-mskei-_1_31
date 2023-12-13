import csv
from model.voyagexdest import vxd


class voyagexdestData:
    def __init__(self):
        self.file_name = "data/files/voyagexdest.csv"

    def read_all_voyagexdest(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    vxd(
                        row["vid"], row["airport"]
                    )
                )
        return ret_list

    def create_voyagexdest(self, voyagexdest):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["vid", "airport"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "vid": voyagexdest.vid,
                    "airport": voyagexdest.airport
                }
            )

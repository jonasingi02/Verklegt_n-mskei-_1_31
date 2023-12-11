import csv
from model.employee import Employee


class EmployeeData:
    def __init__(self):
        print("inside data")
        self.file_name = "data/all_staff.csv"

    def read_all_employees(self):
        ret_list = [] 
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Employee(
                        row["name"], row["kt"], row["phone_number"], row["address"] , row["postal_code"], row["occupation"]
                    )
                )
        return ret_list

    def create_employee(self, employee):
        self.pilots_csv_file = "data/pilots.csv"
        self.flight_attendants_csv_file = "data/flight_attendants.csv"

        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "name",
                "kt",
                "phone_number",
                "address",
                "post_code",
                "occupation",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "name": employee.name,
                    "kt": employee.kt,
                    "phone_number": employee.phone_number,
                    "address": employee.address,
                    "post_code": employee.postal_code,
                    "occupation": employee.occupation,
                }
            )

            if employee.occupation == "flugmaður":
                with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
                    fieldnames = [
                        "name",
                        "kt",
                        "phone_number",
                        "address",
                        "post_code",
                        "occupation",
                    ]
                    pilots_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    pilots_writer.writerow(
                        {
                            "name": employee.name,
                            "kt": employee.kt,
                            "phone_number": employee.phone_number,
                            "address": employee.address,
                            "post_code": employee.postal_code,
                            "occupation": employee.occupation,
                        }
                    )

            if employee.occupation == "flugþjónn":
                with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
                    fieldnames = [
                        "name",
                        "kt",
                        "phone_number",
                        "address",
                        "post_code",
                        "occupation",
                    ]
                    flight_attendants_writer = csv.DictWriter(
                        csvfile, fieldnames=fieldnames
                    )

                    flight_attendants_writer.writerow(
                        {
                            "name": employee.name,
                            "kt": employee.kt,
                            "phone_number": employee.phone_number,
                            "address": employee.address,
                            "post_code": employee.postal_code,
                            "occupation": employee.occupation,
                        }
                    )

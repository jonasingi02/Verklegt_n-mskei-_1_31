import csv
from model.employee import Employee
import os
from tempfile import NamedTemporaryFile

class EmployeeData:
    def __init__(self):
        self.file_name = "data/files/all_staff.csv"
        self.pilots_csv_file = "data/files/pilots.csv"
        self.flight_attendants_csv_file = "data/files/flight_attendants.csv"
        self.update_file = "all_staff.csv"

    def read_all_employees(self) -> list:
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
                with open(self.pilots_csv_file, "a", newline="", encoding="utf-8") as csvfile2:
                    fieldnames = [
                        "name",
                        "kt",
                        "phone_number",
                        "address",
                        "post_code",
                        "occupation",
                    ]
                    pilots_writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)

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
                with open(self.flight_attendants_csv_file, "a", newline="", encoding="utf-8") as csvfile3:
                    fieldnames = [
                        "name",
                        "kt",
                        "phone_number",
                        "address",
                        "post_code",
                        "occupation",
                    ]
                    flight_attendants_writer = csv.DictWriter(
                        csvfile3, fieldnames=fieldnames
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
        
    def update_employee(self, kt_employee_to_update, column_to_update, new_info):

        file_name = "data/files/" + self.update_file    
        with open(self.file_name, 'r+', newline='') as csvfile6:
            reader = csv.reader(csvfile6)
            rows = list(reader)
        
        valid = False
        for row in rows:

            if len(row) >= 2 and row[1] == kt_employee_to_update:
                valid = True

                if row[column_to_update] in row:
                    row[column_to_update] = new_info
            
        if valid:
            update_employee_path = "data/files/new_" + self.update_file
            with open(update_employee_path, 'w', newline='') as file_name:
                writer = csv.writer(file_name)
                writer.writerows(rows)
            os.replace(update_employee_path, self.file_name)
                

    # def update_employee(self, kt_employee_to_update, column_to_update, new_info):
    #     tempfile = NamedTemporaryFile(mode="w", delete=False)

    #     fields = ["name", "kt", "phone_number", "home_address", "postal_code", "occupation"]
    #     with open(self.file_name, "r") as csvfile6, tempfile:
    #         reader = csv.DictReader(csvfile6, fieldnames=fields)
    #         writer = csv.DictWriter(tempfile, fieldnames=fields)

    #         for row in reader:
    #             if row["kt"] == kt_employee_to_update:
                    

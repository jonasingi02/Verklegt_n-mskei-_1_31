import csv
from model.employee import Employee
import os

class EmployeeData:
    def __init__(self):
        self.file_name = "data/files/all_staff.csv"
        self.pilots_csv_file = "data/files/pilots.csv"
        self.flight_attendants_csv_file = "data/files/flight_attendants.csv"
        self.update_file = "all_staff.csv"

    def read_all_employees(self) -> list:
        """ 
        Reads employee data from a CSV file and returns a list of employees as object.

        Returns:
            list[Employee]: A list of employees as objects with details like name, kt, phone number ect.
        """
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
    
    def get_certain_employee(self, name:str) -> list:
        """ 
        Retrieves a list of employees matching a certain given name from a CSV file.

        Args:
            name (str): the name to search for as a stirng.

        Returns:
            list: A list of emplyees data if certain criteria matches.
        """
        certain_employee = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile_certain:
            reader = csv.DictReader(csvfile_certain)
        
            for row in reader:
                if name.lower() in row["name"].lower():
                    certain_employee.append([
                    row["name"],
                    row["kt"],
                    row["phone_number"],
                    row["address"],
                    row["postal_code"],
                    row["occupation"]
                ])
        if certain_employee == []:
            return None  
        else: 
            return certain_employee

    def create_employee(self, employee):
        """ 
        Writes and appends an employee's details to the main CSV file. 
        Also writes and appends to a CSV file depending on their occupation if possible 

        Args:
            employee (Employee): An object representing and employee, Both peronal and job related.
        """
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
        """ 
        Uptades a specific in information for an employee in a CSV file.

        Args:
            kt_employee_to_update (str): The personal ID (kt) of the employee to be updated.
            column_to_update (int): The index of the column where the information needs to be updated.
            new_info (str): The new information to replace the existing data.
        """
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
                    
    def read_all_pilots(self): 
        """
        Reads pilot data from a CSV file and returns a list of 'Employee' objects representing pilots.

        Returns:
            list[Employee]: A list of Employee objects with pilot details.

        """
        pilot_list = []
        with open(self.pilots_csv_file , newline="", encoding="utf-8") as csvfile4:
            reader = csv.DictReader(csvfile4)
            for row in reader:
                pilot_list.append(
                    Employee(
                        row["name"], row["kt"], row["phone_number"], row["home_address"] , row["postal_code"], row["occupation"]
                    )
                )
        return pilot_list
    
    def read_all_flight_attendants(self):
        """ 
        Reads flight attendant data from a CSV file and returns a list of 'Employee' objects.

        Returns:
            list[Employee]: A list of employee as objects representing flight attendants.
        """
        flight_attendants_list = []
        with open(self.flight_attendants_csv_file , newline="", encoding="utf-8") as csvfile5:
            reader = csv.DictReader(csvfile5)
            for row in reader:
                flight_attendants_list.append(
                    Employee(
                        row["name"], row["kt"], row["phone_number"], row["home_address"] , row["postal_code"], row["occupation"]
                    )
                )
        return flight_attendants_list
    




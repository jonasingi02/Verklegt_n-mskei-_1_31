import csv
from Code_files.model.employee import Employee

class EmployeeData:
    def __init__(self):
        print("inside data")
        self.file_name = "Code_files/data/all_staff.csv"

    def get_all_employees(self):
        employees = []
        with open(self.file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone_number_str = row.get("phone_number", "")
                post_code = 0

                if len(phone_number_str) != 7:
                    raise ValueError(f"Invalid phone number length: {phone_number_str}")
                try:
                    phone_number = int(phone_number_str)
                except ValueError:
                    raise ValueError(f"Invalid phone number format: {phone_number_str}")
                try:
                    post_code = int(row.get("post_code", 0))
                except ValueError:
                    pass

                employee = Employee(
                    name=row.get("name", ""),
                    kt=row.get("kt", ""),
                    phone_number=phone_number,
                    address=row.get("address", ""),
                    post_code=post_code,
                    occupation=row.get("occupation", "")
                )
                employees.append(employee)
        return employees

    def create_employee(self, employee): 
        pass

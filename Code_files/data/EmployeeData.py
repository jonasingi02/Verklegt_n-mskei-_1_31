import csv
from Code_files.model.employee import Employee

class EmployeeData:
    def __init__(self):
        print("inside data")
        self.file_name = "Code_files/data/all_staff.csv"

    def get_all_employees(self):
        """Input from user gets checked for valid input and if all inputs checks out 
        it gets appended to the all_staff csv file."""
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


    def create_empoyee(self, employee):
        self.pilots_csv_file = "Code_files/data/pilots.csv"
        self.flight_attendants_csv_file = "Code_files/data/flight_attendants.csv"

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "kt", "phone_number", "address", "post_code", "occupation"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({
                'name': employee.name, 
                'kt': employee.kt,
                'phone_number': employee.phone_number,
                'address': employee.address, 
                'post_code': employee.post_code,
                'occupation': employee.occupation
            })

            if employee.occupation == "flugmaður":
                with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                    fieldnames = ["name", "kt", "phone_number", "address", "post_code", "occupation"]
                    pilots_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    pilots_writer.writerow({
                        'name': employee.name, 
                        'kt': employee.kt,
                        'phone_number': employee.phone_number,
                        'address': employee.address, 
                        'post_code': employee.post_code,
                        'occupation': employee.occupation
                    })

            if employee.occupation == "flugþjónn":
                with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                    fieldnames = ["name", "kt", "phone_number", "address", "post_code", "occupation"]
                    flight_attendants_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    flight_attendants_writer.writerow({
                        'name': employee.name, 
                        'kt': employee.kt,
                        'phone_number': employee.phone_number,
                        'address': employee.address, 
                        'post_code': employee.post_code,
                        'occupation': employee.occupation
                    })        
                    

            

               
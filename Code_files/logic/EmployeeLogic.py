from data.EmployeeData import EmployeeData
from model.employee import Employee
from model.staff_and_dest import staff_and_dest as sd
from data.data_wrapper import data_wrapper

class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def create_employee(self, employee):
        """Takes an employee as an object and forwards it to the data layer"""
        self.data_wrapper.create_employee(employee)

    def update_employee(self, kt_employee_to_update, column_to_update, new_info):
        self.data_wrapper.update_employee(kt_employee_to_update, column_to_update, new_info)
    
    def get_certain_employee(self, name):
        return self.data_wrapper.get_certain_employee(name)
    
    def return_certain_employee(self, input=""):
        staff:list = self.get_certain_employee(input)        
        if staff is not None:
            staff_str: str = ""
            count = 0  
            for list_staff in staff:
                if "flugmaður" in list_staff or "flugþjónn" in list_staff:
                    count += 1
                    
                for elem2 in list_staff:
                    if elem2 == "flugmaður" or elem2 == "flugþjónn":
                        staff_str += elem2 + "\n"
                    else:
                        staff_str += elem2 + ", "
                
            return staff_str, count
        else:
            return None        

    def read_all_employees(self):
        return self.data_wrapper.read_all_employees()
    def get_all_flight_attendantds(self):
        return self.data_wrapper.read_all_flight_attendants()
    
    def get_all_pilots(self): 
        return self.data_wrapper.get_all_pilots()
    
    def get_staff_and_dest_by_date(self, date):
        voyage = self.data_wrapper.read_all_fmvoyages()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        vxp = self.data_wrapper.get_all_voyagexpilots()
        staff = self.data_wrapper.read_all_employees()

        staffreturn = []
        staffs = []
        vlist = []

        for elem in voyage:
            if elem.date == date:
                a = sd()
                a.dest = elem.dest
                a.id = elem.id
                vlist.append(a)

        for elem in vxa:
            for i in vlist:
                if elem.id == i.id:
                    a = sd()
                    a.dest = elem.dest
                    a.id = elem.id
                    a.kt = i.kt
                    staffs.append(a)

        for elem in vxp:
            for i in vlist:
                if elem.id == i.id:
                    a = sd()
                    a.dest = elem.dest
                    a.id = elem.id
                    a.kt = i.kt
                    staffs.append(a)
        
        for i in staffs:
            for j in staff:
                if i.kt == j.kt:
                    a = sd()
                    a.dest = i.dest
                    a.id = i.id
                    a.kt = i.kt
                    a.name = j.name
                    staffreturn.append(a)

        return staffreturn


 
    





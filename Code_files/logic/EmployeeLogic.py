from data.EmployeeData import EmployeeData
from model.employee import Employee
from model.staff_and_dest import staff_and_dest as sd
from model.StaffShifts import staffshifts
from data.data_wrapper import data_wrapper
from datetime import datetime as dt
from datetime import timedelta

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
        staff = self.read_all_employees()

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
    
    def change_date_to_datetime(self, date):
        fdate = dt.strptime(date, "%d-%m-%y")
        return fdate
    
    def get_all_voyages_from_kt(self, kt):
        voyage = self.data_wrapper.read_all_fmvoyages()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        vxp = self.data_wrapper.get_all_voyagexpilots()
        staff = self.data_wrapper.read_all_employees()
        voyagelist = []

        person = ""
        for i in staff:
            if staff.kt == kt:
                person = kt
            else:
                voyagelist.append("error")
        
        list = []

        for i in vxa:
            if person == i.kt:
                list.apped(i.id)
        
        for i in vxp:
            if person == i.kt:
                list.apped(i.id)
        

        for i in list:
            for j in voyage:
                if j.id == i.id:
                    ss = staffshifts()
                    ss.date = self.change_date_to_datetime(j.date)
                    ss.time = j.time
                    ss.dest = j.airport
                    voyagelist.append(ss)

        return voyagelist
    
    def get_staff_voyages_today(self, kt, date):

        all_voyages = self.get_all_voyages_from_kt(kt)

        if all_voyages[0] == "error":
            return "Engar vaktir í dag."
        for i in all_voyages: 
            if i.date == self.change_date_to_datetime(date):
                return i
        return "Engar vaktir í dag."
    
    def get_staff_voyages_week(self, kt, date):
        
        all_voyages = self.get_all_voyages_from_kt(kt)

        if all_voyages[0] == "error":
            return "Engar vaktir í vikunni."
        
        voyages = []
        for i in all_voyages: 
            if i.date <= self.change_date_to_datetime(date) and i.date > (self.change_date_to_datetime(date) + timedelta(days = 7)):
                voyages.append(i)
        return voyages
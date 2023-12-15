from data.EmployeeData import EmployeeData
from model.employee import Employee
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
    
    def change_date_to_datetime(self, date):
        fdate = dt.strptime(date, "%d-%m-%y")
        return fdate
    
    def get_all_voyages_from_kt(self, kt):
        voyages = self.data_wrapper.read_all_fmvoyages()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        vxp = self.data_wrapper.get_all_voyagexpilots()
        staff = self.read_all_employees()
        voyagelist = []
        

        for employee in staff:
            if employee.kt == kt:
                person = kt
                break
        else:
            return voyagelist

        flight_ids = []
        for pilot in vxp:
            if person == pilot.kt:
                flight_ids.append(pilot.id)

        for attendant in vxa:
            if person == attendant.kt:
                flight_ids.append(attendant.id)

        for voyage in voyages:
            if voyage.id in flight_ids:
                ss = staffshifts()
                ss.id = voyage.id
                ss.date = self.change_date_to_datetime(voyage.date)
                ss.time = voyage.time
                ss.dest = voyage.airport
                voyagelist.append(ss)

        return voyagelist

    def get_staff_voyages_today(self, kt, date):
        all_voyages = self.get_all_voyages_from_kt(kt)

        if not all_voyages:
            return None

        today_voyages = [i for i in all_voyages if i.date == self.change_date_to_datetime(date)]

        if not today_voyages:
            return None

        return today_voyages


    def get_staff_voyages_week(self, kt, date):
        all_voyages = self.get_all_voyages_from_kt(kt)

        if not all_voyages:
            return None

        week_start = self.change_date_to_datetime(date)
        week_end = week_start + timedelta(days=7)

        week_voyages = [i for i in all_voyages if week_start <= i.date <= week_end]

        return week_voyages

    def get_all_employees_working_on_date(self, date):
        employees = self.data_wrapper.read_all_employees()
        fm_voyages = self.data_wrapper.read_all_fmvoyages()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        vxp = self.data_wrapper.get_all_voyagexpilots()

        voyage_date_staff = []

        for voyage in fm_voyages:
            if voyage.date == date:
                for pilot in vxp:
                    if pilot.id == voyage.id:
                        for employee in employees:
                            if pilot.kt == employee.kt:
                                voyage_date_staff.append([pilot.id, employee.name, employee.kt, employee.occupation, voyage.date, voyage.time, voyage.airport])

                            return voyage_date_staff
                    else: return None
            else: return None
        
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
        #TODO: Erum við að nota þetta fall?
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
        """Check the csv files to see who is working on asked for date."""
        employees = self.data_wrapper.read_all_employees()
        fm_voyages = self.data_wrapper.read_all_fmvoyages()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        vxp = self.data_wrapper.get_all_voyagexpilots()

        voyage_date_staff = []

        for voyage in fm_voyages:
            if voyage.date == date:
                
                for pilot in vxp:
                    # Check pilots
                    if pilot.id == voyage.id:
        
                        for employee in employees:
                            if pilot.kt == employee.kt:
                                if pilot.main_pilot == True:
                                    main = "Yfirflugmaður"
                                    voyage_date_staff.append([.id, employee.name, employee.kt, main, voyage.date, voyage.time, voyage.airport, attendant.main_attendant])
                                else:
                                    voyage_date_staff.append([pilot.id, employee.name, employee.kt, employee.occupation, voyage.date, voyage.time, voyage.airport])
                                   
                            else: 
                                return None
                
                for attendant in vxa:
                    # Check attendants
                    if attendant.id == voyage.id:
                        
                        for employee in employees:
                            if attendant.kt == employee.kt:
                                if attendant.main_attendant == True:
                                    main = "Yfirflugþjónn"
                                    voyage_date_staff.append([attendant.id, employee.name, employee.kt, main, voyage.date, voyage.time, voyage.airport, attendant.main_attendant])
                                else:
                                    voyage_date_staff.append([attendant.id, employee.name, employee.kt, employee.occupation, voyage.date, voyage.time, voyage.airport])
                                    
                                    
                            
                            else:
                                return None 
            else: 
                return None
        
        return voyage_date_staff
        
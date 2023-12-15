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
        """
        Delegates the creation of a new employee record to the data wrapper.

        Args:
            employee (Employee): The employee object to be added.
        """
        self.data_wrapper.create_employee(employee)

    def update_employee(self, kt_employee_to_update, column_to_update, new_info):
        """ 
        Passes employee update details to the data wrapper for processing.

        Args:
            kt_employee_to_update (str): The personal ID (kt) of the employee to be updated.
            column_to_update (int): The index of the column where the information needs to be updated.
            new_info (str): The new information to replace the existing data.

        """
        self.data_wrapper.update_employee(kt_employee_to_update, column_to_update, new_info)
    
    def get_certain_employee(self, name):
        """ 
        Retrieves employee details for a specific name from the data wrapper.

        Args:
            name (str): The name (or part of it) of the employee to be searched for.

        Returns:
            list[Employee] or None: A list of employee objects matching the given name, or None if no match is found.
        """
        return self.data_wrapper.get_certain_employee(name)
    
    def return_certain_employee(self, input=""):
        """ 
        Formats and returns the details of specific employees based on the provided input.

        Args:
            input (str, optional): Search certain criteria, such as part of an employee's name. Defaults to an empty string.

        Returns:
            tuple or None: A tuple containing a formatted string of employee details and a count of relevant employees if found, or None if no matching employees are found.
        """
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
        """
        Retrieves a list of all employees from the data source.

        Returns:
            List[Employee]: A list of Employee objects representing all employees in the data source.
        """
        return self.data_wrapper.read_all_employees()
    
    def get_all_flight_attendantds(self):
        """
        Retrieves a list of all flight attendants from the data source.

        Returns:
            List[FlightAttendant]: A list of FlightAttendant objects representing all flight attendants in the data source.
    
        """
        return self.data_wrapper.read_all_flight_attendants()
    
    def get_all_pilots(self): 
        """ 
        Retrieves a list of all pilots from the data source.

        Returns:
            List[Pilot]: A list of Pilot objects representing all pilots in the data source.

        """
        return self.data_wrapper.get_all_pilots()
    
    def change_date_to_datetime(self, date):
        """
        Converts a date string to a datetime object.

        Args:
            date (str): The date string to convert, formatted as "dd-mm-yy".

        Returns:
            datetime: The converted datetime object.
        """
        fdate = dt.strptime(date, "%d-%m-%y")
        return fdate
    
    def get_all_voyages_from_kt(self, kt):
        """ 
        Retrieves all voyages associated with a specific employee by their identifier (kt).

        Args:
            kt (_type_): The unique identifier of the employee.

        Returns:
            List[VoyageShift]: A list of VoyageShift objects, each representing a voyage associated with the specified employee. 
            Each VoyageShift includes voyage ID, date, time, and destination.
        """
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
        """
        Retrieves the voyages assigned to a staff member identified by their kt on a specific date.

        Args:
            kt (str): Identifies a specific employee by their personal ID (kt).
            date (str or datetime): The date for which to retrieve voyages, either as a string or a datetime object.

        Returns:
            List[VoyageShift] or None: A list of VoyageShift objects representing the voyages on the specified date, or None if there are no voyages.
        """
        all_voyages = self.get_all_voyages_from_kt(kt)

        if not all_voyages:
            return None

        today_voyages = [i for i in all_voyages if i.date == self.change_date_to_datetime(date)]

        if not today_voyages:
            return None

        return today_voyages

    def get_staff_voyages_week(self, kt, date):
        """ 
        Retrieves the voyages assigned to a staff member, identified by their kt, within a week from a specified date.

        Args:
            kt (str): Identifies a certain employee from all the staff by their personal ID (kt).
            date (str or datetime): The starting date of the week for which to retrieve voyages, either as a string or a datetime object.

        Returns:
            List[VoyageShift] or None: A list of VoyageShift objects representing the voyages within the specified week, or 
            Returns None if there are no voyages in that period.
        """
        all_voyages = self.get_all_voyages_from_kt(kt)

        if not all_voyages:
            return None

        week_start = self.change_date_to_datetime(date)
        week_end = week_start + timedelta(days=7)

        week_voyages = [i for i in all_voyages if week_start <= i.date <= week_end]

        return week_voyages

    def get_all_employees_working_on_date(self, date):
        """ 
        Retrieves the voyages assigned to a staff member. Identifies it by their kt, within a week from a specified date.

        Args:
            kt (str): Identifies a certain employee from all the staff by their personal ID (kt).
            date (str or datetime): The starting date of the week for which to retrieve voyages, either as a string or a datetime object.
            
        Returns:
            List[VoyageShift] or None: A list of VoyageShift objects representing the voyages within the specified week.
            Returns None if there are no voyages in that period.

        """
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
                                if pilot.main_pilot == "True":
                                    main = "yfirflugmaður"
                                    voyage_date_staff.append([pilot.id, employee.name, employee.kt, main, voyage.date, voyage.time, voyage.airport])
                                else:
                                    voyage_date_staff.append([pilot.id, employee.name, employee.kt, employee.occupation, voyage.date, voyage.time, voyage.airport])
                
                for attendant in vxa:
                    # Check attendants
                    if attendant.id == voyage.id:
                        
                        for employee in employees:
                            if attendant.kt == employee.kt:
                                if attendant.main_attendant == "True":
                                    main = "Yfirflugþjónn"
                                    voyage_date_staff.append([attendant.id, employee.name, employee.kt, main, voyage.date, voyage.time, voyage.airport])
                                else:
                                    voyage_date_staff.append([attendant.id, employee.name, employee.kt, employee.occupation, voyage.date, voyage.time, voyage.airport])

        if voyage_date_staff != []:
            return voyage_date_staff
        else:
            return None
        
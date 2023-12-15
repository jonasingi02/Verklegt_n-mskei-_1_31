from .plane_logic import PlaneLogic
from .destination_logic import destination_logic
from .EmployeeLogic import EmployeeLogic
from .fmvoyage_logic import FmvoyageLogic
from data.data_wrapper import data_wrapper

class Logic_wrapper:
    def __init__(self):
        self.data_wrapper = data_wrapper()
        self.plane_logic = PlaneLogic(self.data_wrapper)
        self.destination_logic = destination_logic(self.data_wrapper)
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.fmvoyage_logic = FmvoyageLogic(self.data_wrapper)

    def create_plane(self, plane):
        """
        Takes in a plane object and forwards it to the data layer for creation.

        Args:
            plane (Plane): An object representing the plane details.

        Returns:
            Any: The result of the plane creation operation in the data layer.
        """
        return self.plane_logic.create_plane(plane)

    def get_all_planes(self):
        """
        Retrieves all plane records from the data layer.

        Returns:
            List[Plane]: A list of Plane objects representing all planes in the data source.
        """
        return self.plane_logic.get_all_planes()
    
    def create_destination(self, destination):
        """
        Takes in a destination object and forwards it to the data layer for creation.

        Args:
            destination (Destination): An object representing the destination details.

        Returns:
            Any: The result of the destination creation operation in the data layer.    
        """
        return self.destination_logic.create_destination(destination)
    
    def get_all_destinations(self):
        """
        Retrieves all destination records from the data layer.

        Returns:
            List[Destination]: A list of Destination objects representing all destinations in the data source.
        """
        return self.destination_logic.get_all_destinations()
    
    def create_employee(self, employee):
        """
        Creates a new employee record in the data layer.

        Args:
            employee (Employee): An object representing the employee details.

        Returns:
            Any: The result of the employee creation operation in the data layer.
        """
        return self.employee_logic.create_employee(employee)
    
    def update_employee(self,kt_employee_to_update, column_to_update, new_info):
        """
        Updates a specific column of an employee record in the data layer.

        Args:
            kt_employee_to_update (str or int): The identifies the unique employee to update.
            column_to_update (str): The name of the column in the employee record to update.
            new_info (Any): The new information to be updated in the specified column.

        Returns:
            Any: The result of the employee update operation in the data layer.
        """
        return self.employee_logic.update_employee(kt_employee_to_update, column_to_update, new_info)
    
    def update_flight_info(self, flight_id_to_update, column_to_update, new_info): 
        """
        Updates specific information for a flight record.

        Args:
            flight_id_to_update (int): The ID of the flight to update.
            column_to_update (str): The name of the column in the flight record to update.
            new_info (Any): The new information to be updated in the specified column.

        Returns:
            Any: The result of the flight information update operation.
        """
        return self.fmvoyage_logic.update_flight_info(flight_id_to_update, column_to_update, new_info)

    def read_all_employees(self):
        """
        Retrieves a list of all employee records.

        Returns:
            List[Employee]: A list of Employee objects representing all employees.
        """
        return self.employee_logic.read_all_employees()
    
    def get_all_pilots(self): 
        """
        Retrieves a list of all pilots.

        Returns:
            List[Pilot]: A list of Pilot objects representing all pilots.
        """
        return self.employee_logic.get_all_pilots()
    
    def read_all_fmvoyages(self):
        """
        Retrieves a list of all FMvoyages.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing all FMvoyages.
        """
        return self.fmvoyage_logic.read_all_fmvoyages()
    
    def read_all_employees(self):
        """
        Retrieves a list of all employee records from the data layer.

        Returns:
            List[Employee]: A list of Employee objects representing all employees in the data source.
        """
        return self.employee_logic.read_all_employees()
    
    def get_certain_employee(self, name):
        """
        Retrieves a specific employee by name.

        Args:
            name (str): The name of the employee to retrieve.

        Returns:
            Employee: An Employee object representing the employee, or None if not found.
        """
        return self.employee_logic.get_certain_employee(name)

    def return_certain_employee(self, input):
        """
        Retrieves a specific employee based on the provided input.

        Args:
            input (Any): The criteria used to identify the employee.

        Returns:
            Employee: An Employee object representing the employee, or None if not found.
        """
        return self.employee_logic.return_certain_employee(input)

    def get_all_flight_attendants(self): 
        """
        Retrieves a list of all flight attendants.

        Returns:
            List[FlightAttendant]: A list of FlightAttendant objects representing all flight attendants.
        """
        return self.employee_logic.get_all_flight_attendantds()

    def read_all_fmvoyages(self):
        """
        Retrieves a list of all FMvoyage records from the data source.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing all the FMvoyages in the data source.
        """
        return self.fmvoyage_logic.read_all_fmvoyages()
    
    def create_voyagexpilot(self, vxp):
        """
        Creates a new record for a pilot assigned to a voyage in the data source.

        Args:
            vxp (VoyageXPilot): An object representing the pilot's voyage assignment details.

        Returns:
            Any: The result of the operation to create a new voyagexpilot record.
        """
        return self.fmvoyage_logic.create_voyagexpilot(vxp)
    
    def get_all_voyagexpilots(self):
        """
        Retrieves a list of all pilots assigned to voyages from the data source.

        Returns:
            List[VoyageXPilot]: A list of VoyageXPilot objects representing all pilots assigned to voyages.
        """
        return self.fmvoyage_logic.get_all_voyagexpilots()

    def find_voyage_by_id(self, id):
        """
        Retrieves a specific FMvoyage record by its unique ID from the data source.

        Args:
            id (int or str): The unique identifier of the FMvoyage to be found.

        Returns:
           FMVoyage or None: The FMVoyage object corresponding to the given ID. None if no match is found.
        """
        return self.fmvoyage_logic.find_voyage_by_id(id)
    
    def create_fmvoyage(self,voyage):
        """
        Creates a new FMvoyage record in the data source.

        Args:
            voyage (FMVoyage): An object representing the FMvoyage details to be created.
        """
        self.fmvoyage_logic.create_fmvoyage(voyage)
        
    def same_date_voyage(self, date):
        """
        Retrieves a list of voyages occurring on a specified date.

        Args:
            date (str or datetime): The date for which to find voyages, either as a string or a datetime object.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing voyages on the specified date.
        """
        return self.fmvoyage_logic.same_date_voyage(date)
    
    def pilots_not_in_voyage(self, list):
        """
        Retrieves a list of pilots who are not assigned to the voyages specified in the input list.

        Args:
            list (List[int]): A list of voyage IDs to check for pilot exclusion.

        Returns:
            List[Pilot]: A list of Pilot objects representing pilots not assigned to any of the voyages in the input list.
        """
        return self.fmvoyage_logic.pilots_not_in_voyage(list)
    
    def flight_attendants_not_in_voyage(self, list):
        """
        Retrieves a list of flight attendants who are not part of the voyages specified in the input list.

        Args:
            list (List[int]): A list of voyage IDs to check for flight attendant exclusion.

        Returns:
            List[FlightAttendant]: A list of FlightAttendant objects representing flight attendants not assigned to any of the voyages in the input list.
        """
        return self.fmvoyage_logic.flight_attendants_not_in_voyage(list)
    
    def create_voyagexattendant(self, vxa):
        """
        Creates a new voyagexattendant record in the data source.

        Args:
            vxa (VoyageXAttendant): An object representing the voyagexattendant details to be created.

        Returns:
            Any: The result of the voyagexattendant creation operation.
        """
        return self.fmvoyage_logic.create_voyagexattendant(vxa)
    
    def get_unmanned_voyages(self):
        """
        Retrieves a list of voyages that do not have any assigned pilots or attendants.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing voyages without assigned crew members.
        """
        return self.fmvoyage_logic.get_unmanned_voyages()
    
    def change_date_to_datetime(self, date):
        """
        Converts a date string to a datetime object.

        Args:
            date (str): The date string to convert, formatted as "dd-mm-yyyy"

        Returns:
            datetime: The converted datetime object.
        """
        return self.employee_logic.change_date_to_datetime(date)
    
    def get_staff_voyages_today(self, kt, date):
        """
        Retrieves a list of voyages for a specific staff member on a given date.

        Args:
            kt (str or int): The unique identifier of the staff member.
            date (str or datetime): The specific date for which to retrieve voyages.

        Returns:
            List[Voyage]: A list of Voyage objects representing the voyages for the staff member on the specified date.
        """
        return self.employee_logic.get_staff_voyages_today(kt, date)
        
    def get_staff_voyages_week(self, kt, date):
        """
        Retrieves a list of voyages for a specific staff member within a week from a specified date.

        Args:
            kt (str or int): The unique identifier of the staff member.
            date (str or datetime): The starting date of the week for which to retrieve voyages.

        Returns:
            List[Voyage]: A list of Voyage objects representing the voyages for the staff member within the specified week.
        """
        return self.employee_logic.get_staff_voyages_week(kt, date)
    
    def read_all_fm_voyages(self):
        """
        Retrieves a list of all FMvoyages from the data source.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing all the FMvoyages in the data source.
        """
        return self.fmvoyage_logic.read_all_fmvoyages()
    
    def get_staff_by_date(self, date):
        """
        Retrieves a list of staff members working on a specific date.

        Args:
            date (str or datetime): The date for which to retrieve the staff members.

        Returns:
           List[Employee]: A list of Employee objects representing the staff members working on the specified date.
        """
        return self.employee_logic.get_all_employees_working_on_date(date)
    
    def get_all_attendants_on_date(self,date_input):
        """
        Retrieves a list of staff members working on a specific date.

        Args:
            date (str or datetime): The date for which to retrieve the staff members.

        Returns:
        List[Employee]: A list of Employee objects representing the staff members working on the specified date.
        """
        return self.employee_logic.get_all_attendants_on_date(date_input)
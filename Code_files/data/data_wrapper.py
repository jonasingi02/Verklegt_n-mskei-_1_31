from data.EmployeeData import EmployeeData
from data.plane_data import PlaneData
from data.destination_data import destination_data
from data.fmvoyage_data import FmvoyageData


class data_wrapper:
    def __init__(self):
        self.plane_data = PlaneData()
        self.destination_data = destination_data()
        self.employee_data = EmployeeData()
        self.FmvoyageData = FmvoyageData()

    def get_all_planes(self):
        """
        Retrieves a list of all plane records from the data source.

        Returns:
            List[Plane]: A list of Plane objects representing all planes in the data source.
        """
        return self.plane_data.read_all_planes()

    def create_plane(self, plane):
        """
        Creates a new plane record in the data source.

        Args:
            plane (Plane): An object representing the plane details to be created.

        Returns:
             Any: The result of the plane creation operation in the data source.
        """
        return self.plane_data.create_plane(plane)

    def get_all_destinations(self):
        """ 
        Retrieves a list of all destination records from the data source.

        Returns:
            List[Destination]: A list of Destination objects representing all destinations in the data source.
        """
        return self.destination_data.read_all_destinations()

    def create_destination(self, destination):
        """
        Creates a new destination record in the data source.

        Args:
            destination (Destination): An object representing the destination details to be created.

        Returns:
           Any: The result of the destination creation operation in the data source.
        """
        return self.destination_data.create_destination(destination)
    
    def get_certain_employee(self, name):
        """
        Retrieves a specific employee by name from the data source.

        Args:
            name (str): The name of the employee to retrieve.

        Returns:
            Employee or None: An Employee object representing the employee if found.
            Returns None if no such employee exists.
        """
        return self.employee_data.get_certain_employee(name)
    
    def read_all_employees(self):
        """
        Retrieves a list of all employee records from the data source.

        Returns:
            List[Employee]: A list of Employee objects representing all employees in the data source.
        """
        return self.employee_data.read_all_employees()
    
    def create_employee(self, employee):
        """
        Creates a new employee record in the data source.

        Args:
            employee (Employee): An object representing the employee details to be created.

        Returns:
            Any: The result of the employee creation operation in the data source.
        """
        return self.employee_data.create_employee(employee)
    
    def update_employee(self,kt_employee_to_update, column_to_update, new_info):
        """
        Updates a specific column of an employee record in the data source.

        Args:
            kt_employee_to_update (str or int): The unique identifier of the employee to update.
            column_to_update (str): The name of the column in the employee record to update.
            new_info (Any): The new information to be updated in the specified column.

        Returns:
            Any: The result of the employee update operation in the data source.
        """
        return self.employee_data.update_employee(kt_employee_to_update, column_to_update, new_info)

    def create_fmvoyage(self, fmvoyage):
        """
        Creates a new FMvoyage record in the data source.

        Args:
            fmvoyage (FMVoyage): An object representing the FMvoyage details to be created.

        Returns:
            Any: The result of the FMvoyage creation operation in the data source.
        """
        return self.FmvoyageData.create_fmvoyage(fmvoyage)
    
    def read_all_fmvoyages(self):
        """
        Retrieves a list of all FMvoyage records from the data source.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing all FMvoyages in the data source.
        """
        return self.FmvoyageData.read_all_fmvoyages()

    def create_voyagexpilot(self, vxp):
        """
        Creates a new voyagexpilot record in the data source.

        Args:
            vxp (VoyageXPilot): An object representing the pilot's voyage assignment details.

        Returns:
            Any: The result of the operation to create a new voyagexpilot record.
        """
        return self.FmvoyageData.create_voyagexpilot(vxp)
    
    def get_all_voyagexpilots(self):
        """
        Retrieves a list of all pilots assigned to voyages from the data source.

        Returns:
            List[VoyageXPilot]: A list of VoyageXPilot objects representing all pilots assigned to voyages.
        """
        return self.FmvoyageData.read_all_voyagexpilots()
    
    def get_all_pilots(self):
        """
        Retrieves a list of all pilots from the data source.

        Returns:
            List[Pilot]: A list of Pilot objects representing all pilots.
        """
        return self.employee_data.read_all_pilots()
    
    def get_all_flight_attendants(self):
        """
        Retrieves a list of all flight attendants from the data source.

        Returns:
            List[FlightAttendant]: A list of FlightAttendant objects representing all flight attendants.
        """
        return self.employee_data.read_all_flight_attendants()
        
    def get_all_voyagexattendants(self):
        """
        Retrieves a list of all attendants assigned to voyages from the data source.

        Returns:
           List[VoyageXAttendant]: A list of VoyageXAttendant objects representing all attendants assigned to voyages.
        """
        return self.FmvoyageData.read_all_voyagexattendants()
    
    def create_voyagexattendant(self, vxa):
        """
        Creates a new voyagexattendant record in the data source.

        Args:
            vxa (VoyageXAttendant): An object representing the attendant's voyage assignment details.

        Returns:
            Any: The result of the operation to create a new voyagexattendant record.
        """
        return self.FmvoyageData.create_voyagexattendant(vxa)

    def read_all_fmvoyages(self):
        """
        Retrieves a list of all FMvoyages from the data source.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing all the FMvoyages.
        """
        return self.FmvoyageData.read_all_fmvoyages()
    
    def update_flight_info(self, id, column, data):
        return self.FmvoyageData.update_flight_info(id, column, data)

    
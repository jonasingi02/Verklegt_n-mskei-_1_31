from model.FMVoyage import FMvoyage

from data.plane_data import PlaneData
from model.voyagexpilots import voyagexpilots

class FmvoyageLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_fmvoyage(self, FMvoyage):
        """ 
        Creates a new FMvoyages record in the data source.

        Args:
            FMvoyage (FMvoyage): An object of the FMVoyage class representing the voyage details to be created.
        """
        self.data_wrapper.create_fmvoyage(FMvoyage)

    def read_all_fmvoyages(self):
        """ 
        Retrieves a list of all FMvoyage records from the data source.

        Returns:
            List[FMVoyage]: A list of all FMVoyage objects in the data source.
        """
        return self.data_wrapper.read_all_fmvoyages()
    
    def create_voyagexpilot(self, vxp):
        """ 
        Creates a new voyagexpilot record in the data source.

        Args:
            vxp (VoyageXPilot): An object representing the pilot's voyage details to be created.

        Returns:
            Any: The result of the data source operation to create a voyagexpilot.
        """
        return self.data_wrapper.create_voyagexpilot(vxp)
    
    def get_all_voyagexpilots(self):
        """ 
        Retrieves a list of all voyagexpilot records from the data source.

        Returns:
            List[VoyageXPilot]: A list of all VoyageXPilot objects in the data source.
        """
        return self.data_wrapper.get_all_voyagexpilots()
    
    def update_flight_info(self, flight_id_to_update, column_to_update, new_info):
        """ 
        Updates specific information for a flight record in the data source.

        Args:
            flight_id_to_update (int): The ID of the flight to update.
            column_to_update (str): The name of the column in the flight record to update.
            new_info (Any): The new information to be updated in the specified column.

        Returns:
            Any: The result of the data source operation to update the flight information.
        """
        return self.data_wrapper.update_flight_info(flight_id_to_update, column_to_update, new_info)
    
    def create_voyagexattendant(self, vxa):
        """ 
        Creates a new voyagexattendant record in the data source.

        Args:
            vxa (VoyageXAttendant): An object representing the attendant's voyage details to be created.

        Returns:
            Any: The result of the data source operation to create a voyagexattendant.
        """
        return self.data_wrapper.create_voyagexattendant(vxa)
    
    def find_voyage_by_id(self, id):
        """ 
        Finds and returns a specific FMvoyage record by its identifier.

        Args:
            id (int or str): The unique identifier of the FMvoyage to be found.

        Returns:
            FMvoyage: The FMVoyage object corresponding to the given ID.
            Returns an empty FMVoyage object if no match is found.
        """
        result = self.data_wrapper.read_all_fmvoyages()
        for i in result:
            if i.id == id:
                return i
        return FMvoyage()
    
    def same_date_voyage(self, date):
        """ 
        Retrieves a list of voyage IDs for voyages occurring on the specified date.

        Args:
            date (str or datetime): The date to find certain voyages, either a string or datetime object.

        Returns:
            list[int]: A list of IDs for voyages occurring on the specified date.
        """
        voyage = self.data_wrapper.read_all_fmvoyages()
        voyage_list = []
        for elem in voyage:
            if elem.date == date:
                voyage_list.append(elem.id)
        return voyage_list

    def pilots_not_in_voyage(self, list):
        """
        Retrieves a list of pilots who are not part of the voyages specified in the input list.

        Args:
            list (list[int]): A list of voyage IDs for pilot assignments

        Returns:
            list[Pilot]: A list Pilot object representing those who are not assigned for any voyages in the input list. 
        """
        vxp = self.data_wrapper.get_all_voyagexpilots()
        pilots_list = []
        for elem in vxp:
            for j in list:
                if elem.id == j:
                    pilots_list.append(elem.kt)

        input_validator_list = []
        pilots = self.data_wrapper.get_all_pilots()
        for i in pilots:
            bool = True
            for j in pilots_list:
                if i.kt == j:
                    bool = False
            if bool == True:
                input_validator_list.append(i)
        return input_validator_list
    
    def flight_attendants_not_in_voyage(self, list):
        """
        Compiles a list of the flight attendants that are assigned for voyages in the input list.

        Args:
            list (list[int]): A list of the voyages ID to cheack for flight attendants assignment.

        Returns:
            list[str]: Identifies the kt for flight attendants that are assigned for voyages in input list.
        """
        vxa = self.data_wrapper.get_all_voyagexattendants()
        attendants_list = []
        for elem in vxa:
            for j in list:
                if elem.id == j:
                    attendants_list.append(elem.kt)

        input_validator_list = []
        attendants = self.data_wrapper.get_all_flight_attendants()
        for i in attendants:
            bool = True
            for j in attendants_list:
                if i.kt == j:
                    bool = False
            if bool == True:
                input_validator_list.append(i)
        return input_validator_list
    
    def get_unmanned_voyages(self):
        """
        Retrieves a list of FMvoyage records that currently do not have any assigned pilots or attendants.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing voyages that are not assigned to any crew members.
        """
        fmvoyages = self.data_wrapper.read_all_fmvoyages()
        vxp = self.data_wrapper.get_all_voyagexpilots()
        vxa = self.data_wrapper.get_all_voyagexattendants()
        result = []

        for i in fmvoyages:
            bool = True
            for j in vxp:
                if i.id == j.id:
                    bool = False
            for j in vxa:
                if i.id == j.id:
                    bool = False
            if bool == True:
                result.append(i)
        return result
    
    def find_voyage_by_date(self, date):
        """
        Retrieves a list of voyages occurring on a specified date.

        Args:
            date (str or datetime): The date for which to find voyages, formatted as a string or represented as a datetime object.

        Returns:
            List[FMVoyage]: A list of FMVoyage objects representing voyages that occur on the specified date.
        """
        result = self.data_wrapper.read_all_fmvoyages()
        voyages = []
        for i in result:
            if i.date == date:
                voyages.append(i)
            
        return voyages
    
    

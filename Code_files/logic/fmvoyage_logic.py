from model.FMVoyage import FMvoyage

from data.plane_data import PlaneData
from model.voyagexpilots import voyagexpilots

class FmvoyageLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_fmvoyage(self, FMvoyage):
        """"""
        self.data_wrapper.create_fmvoyage(FMvoyage)

    def read_all_fmvoyages(self):
        return self.data_wrapper.read_all_fmvoyages()
    
    def create_voyagexpilot(self, vxp):
        return self.data_wrapper.create_voyagexpilot(vxp)
    
    def get_all_voyagexpilots(self):
        return self.data_wrapper.get_all_voyagexpilots()
    
    def create_voyagexattendant(self, vxa):
        return self.data_wrapper.create_voyagexattendant(vxa)
    
    def find_voyage_by_id(self, id):
        result = self.data_wrapper.read_all_fmvoyages()
        for i in result:
            if i.id == id:
                return i
        return FMvoyage()
    
    def same_date_voyage(self, date):
        voyage = self.data_wrapper.read_all_fmvoyages()
        voyage_list = []
        for elem in voyage:
            if elem.date == date:
                voyage_list.append(elem.id)
        return voyage_list

    def pilots_not_in_voyage(self, list):
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
        result = self.data_wrapper.read_all_fmvoyages()
        voyages = []
        for i in result:
            if i.date == date:
                voyages.append(i)
            
        return voyages
        

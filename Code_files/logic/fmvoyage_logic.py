from model.FMVoyage import FMvoyage

from data.plane_data import PlaneData
from model.voyagexpilots import voyagexpilots
from data.fmvoyage_data import FmvoyageData

class FmvoyageLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        

    def create_fmvoyage(self, FMvoyage):
        """"""
        self.data_wrapper.create_fmvoyage(FMvoyage)

    def get_all_fmvoyages(self):
        return self.data_wrapper.get_all_fmvoyages()
    
    def create_voyagexpilots(self, voyagexpilots):
        return self.data_wrapper.create_voyagexpilots()
    
    def get_all_voyagexpilots(self):
        return self.data_wrapper.get_all_voyagexpilots()
    
    def get_all_voyagexflightattendants(self):
        return self.data_wrapper.get_all_voyagexflightattendants()
    
    def create_voyagexflightattendats(self, voyagexflightattendant):
        return self.data_wrapper.create_voyagexflightattendats()
    
    def get_voyage_distribution(self):
        voyages = self.data_wrapper.get_all_fmvoyages()
        pilots_assignments = self.data_wrapper.get_all_voyagexpilots()
        attendants_assignments = self.data_wrapper.get_all_voyagexattendants()

        voyage_personnel = []
        for voyage in voyages:
            assigned_pilots = [pa.pilot for pa in pilots_assignments if pa.vid == voyage.id]
            assigned_attendants = [aa.attendant for aa in attendants_assignments if aa.vid == voyage.id]

            voyage_personnel.append({
                'voyage': voyage,
                'pilots': assigned_pilots,
                'attendants': assigned_attendants
            })

        return voyage_personnel

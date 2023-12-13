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
    
    def find_voyage_by_id(self, id):
        result = self.data_wrapper.read_all_fmvoyages()
        for i in result:
            print(f"result:{i}, id:{id}")
            if i.id == id:
                return i
        return FMvoyage()

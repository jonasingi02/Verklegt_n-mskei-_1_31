from model.FMVoyage import FMvoyage
#from model.voyagexdest import voyagexdest
#from model.voyagexplane import voyagexplane
from data.plane_data import PlaneData

class FmvoyageLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_fmvoyage(self, FMvoyage):
        """"""
        self.data_wrapper.create_fmvoyage(FMvoyage)

    def get_all_fmvoyages(self):
        return self.data_wrapper.get_all_fmvoyages()
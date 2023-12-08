from datetime import datetime

class FMvoyage:
    def __init__(self, date = "", plane = "", destination = "", id = 0):
        id += 1
        self.date = date
        self.id = id
        self.plane = plane
        self.destination = destination

    def __str__(self):
        return f"id: {self.id}, date: {self.date}, plane: {self.plane}, destination: {self.destination}"
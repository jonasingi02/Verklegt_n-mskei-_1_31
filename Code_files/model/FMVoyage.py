from datetime import datetime

class FMvoyage:
    def __init__(self, id="", date = "",time="", plane = "", airport = ""):
        self.id = id
        self.date = date
        self.time = time
        self.plane = plane
        self.airport = airport

    def __str__(self):
        return f"id: {self.id}, date: {self.date}, plane: {self.plane}, airport: {self.airport}"
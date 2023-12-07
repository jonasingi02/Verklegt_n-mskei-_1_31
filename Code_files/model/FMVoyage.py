from datetime import datetime

class destination:
    def __init__(self, country = "", airport = "", flighttime = 0, distance = 0, name = "", phone = 0):
        self.country = country
        self.airport = airport
        self.flighttime = flighttime
        self.distance = distance
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"country: {self.country}, airport: {self.airport}, flighttime: {self.flighttime}, distance: {self.distance}, name: {self.name}, phone: {self.phone}"
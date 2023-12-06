class Planes:
    def __init__(self, name = "", type = "", numseats = 0, manufacturer = ""):
        self.name = name
        self.type = type
        self.numseats = numseats
        self.manufacturer = manufacturer

    def __str__(self):
        return f"name: {self.name}, type: {self.type}, number of seats: {self.numseats}, manufacturer: {self.manufacturer}"
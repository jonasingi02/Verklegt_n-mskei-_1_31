class staff_and_dest:
    def __init__(self, name = "", kt = "", destination = "", date = ""):
        self.name = name
        self.kt = kt
        self.destination = destination
        self.date = date

    def __str__(self):
        return f"name: {self.name}, kt: {self.kt}, destination: {self.destination}, date: {self.date}"
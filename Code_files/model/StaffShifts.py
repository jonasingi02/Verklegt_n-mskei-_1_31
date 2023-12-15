from datetime import datetime

class staffshifts:
    def __init__(self, id="", date = None, dest = "", time = ""):
        self.id = id
        self.date = date
        self.dest = dest
        self.time = time

    def __str__(self):
        return f"date: {self.date}, time: {self.time}, destination: {self.dest}"
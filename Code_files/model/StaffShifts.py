from datetime import datetime

class staffshifts:
    def __init__(self, date = datetime(0, 0, 0), dest = "", time = ""):
        self.date = date
        self.dest = dest
        self.time = time

    def __str__(self):
        return f"date: {self.date}, time: {self.time}, destination: {self.dest}"
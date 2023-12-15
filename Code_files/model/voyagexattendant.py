class voyagexattendant:
    def __init__(self, id = "", kt = "", main_attendant = False):
        self.id = id
        self.kt = kt
        self.main_attendant = main_attendant

    def __str__(self):
        return f"voyage id: {self.vid}, attendant: {self.attendant}"
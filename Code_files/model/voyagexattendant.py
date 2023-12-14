class voyagexattendant:
    def __init__(self, vid = "", attendant = ""):
        self.vid = vid
        self.attendant = attendant

    def __str__(self):
        return f"voyage id: {self.vid}, attendant: {self.attendant}"
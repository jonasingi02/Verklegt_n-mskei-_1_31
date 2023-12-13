class voyagexpilots:
    def __init__(self, vid = "", pilot = ""):
        self.vid = vid
        self.pilot = pilot

    def __str__(self):
        return f"voyage id: {self.vid}, kt: {self.kt}"
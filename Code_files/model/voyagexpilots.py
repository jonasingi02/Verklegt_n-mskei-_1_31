class voyagexpilots:
    def __init__(self, id = "", kt = "", main_pilot = False):
        self.id = id
        self.kt = kt
        self.main_pilot = main_pilot

    def __str__(self):
        return f"voyage id: {self.id}, kt: {self.kt}"
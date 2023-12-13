class voyagexpilots:
    def __init__(self, id = "", kt = ""):
        self.id = id
        self.kt = kt

    def __str__(self):
        return f"voyage id: {self.id}, kt: {self.kt}"
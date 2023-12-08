class Employee:
    def __init__(self, name="", kt="", phone_number = 0, address="", post_code = 0, occupation=""):
        self.name = name
        self.kt = kt
        self.phone_number = phone_number
        self.address = address
        self.postal_code = post_code
        self.occupation = occupation

    def __repr__(self):
        return f"Employee(name='{self.name}', kt='{self.kt}', phone_number='{self.phone_number}', address='{self.address}', postal_code='{self.postal_code}', occupation='{self.occupation}')"

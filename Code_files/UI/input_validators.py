# Input Validators


class NameLengthException(Exception):
    print("Þessi strengur er lengri en 50 stafir.")


# Validating staff information
class ValidatingStaffInput:
    def __init__(self) -> None:
        pass

    def validate_name(self):
        """Check length of name"""
        if len(self) >= 50:
            raise NameLengthException()

    def validate_kt(self):
        """Check if kennitala is 10 digits and all numeric characters.
        If not prints out error message, try again."""
        valid = self.isnumeric()

        if len(self) != 10:
            print("Þessi kennitala virðist ekki vera rétt. Reyndu aftur.")
            return False
        elif valid != True:
            print(
                "Þessi kennitala virðist ekki vera rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
            return None
        else:
            return self

    def validate_phone_number(self):
        """Check validity of phone number by checking if it's only numerical numbers"""
        valid = self.isnumeric()

        if valid != True:
            print(
                "Þetta símanúmer virðist ekki vera rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
            return None
        else:
            return self

    def validate_address(self, address, postal_code, place):
        pass

    def validate_occupation(self):
        lower_occupation = self.lower()
        pass


# Validate plane information
class ValidatePlaneInfo:
    def __init__(self) -> None:
        pass

    def validate_num_seats(self):
        """Check if number of seats input is only integers"""
        valid: bool = self.isnumeric()

        if valid:
            return self
        else:
            print(
                "Þetta virðist hafa farið úrskeiðis. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
            return 0

    def validate_plane_string(self):
        """Check length of input"""
        if len(self) >= 50:
            raise NameLengthException()
        else:
            return ""


# Validate Voyage information
class ValidateVoyageInput:
    def __init__(self) -> None:
        pass

    def validate_voyage_string(self):
        """Check length of input"""
        if len(self) >= 50:
            raise NameLengthException()
        else:
            return self

    def validate_length_km(self):
        """Check if user input for kilometers is a float."""
        try:
            self = float(self)
            return self
        except ValueError:
            return None


# Validate Destination inputs
class ValidateDestinationInputs:
    def __init__(self) -> None:
        pass

    def validate_destination_string(self):
        """Check length of input"""
        if len(self) >= 50:
            raise NameLengthException()
        else:
            return self

    def validate_contact_phone_number(self):
        valid = self.isnumeric()

        if valid:
            return self
        else:
            print(
                "Hmm.. Þetta virðist ekki rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
            return None


# d.country = input("nafn áfangastaðs (string):")
# d.airport = input("nafn flugvallar (string):")
# d.flighttime = input("flugtími (datetime hours):")
# d.distance = input("vegalengd í km (int):")
# d.name = input("nafn tengiliðs (string):")
# d.phone = input("símanúmer tengiliðs (int):")
# self.logic_wrapper.create_destination(d)

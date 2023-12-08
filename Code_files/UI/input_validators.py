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
            print("Úps, þessi kennitala virðist ekki vera rétt. Reyndu aftur.")
            return False
        elif valid != True:
            print("Úps, þessi kennitala virðist ekki vera rétt. Reyndu aftur.")
            return None
        else:
            return self

    def validate_phone_number(self):
        """Check validity of phone number by checking if it's only numerical numbers"""
        valid = self.isnumeric()

        if valid != True:
            print("Úps, þetta símanúmer virðist ekki vera rétt. Reyndu aftur.")
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
                "Hmm.. Þetta virðist hafa farið úrskeiðis. Reyndu aftur. (Einungis tölustafir)"
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
        pass

    def validate_contact_phone_number(self):
        valid = self.isnumeric()

        if valid:
            return self
        else:
            return None
        
class ValidateFMVoyageInfo:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def validate_voyage_dest(self, dest):
        result = self.logic_wrapper.get_all_destinations()
        for elem in result:
            if elem.airport == dest:
                return dest
        print("engin áfangastaður í kerfinu með þennan flugvöll.")
        return ""

    def validate_voyage_plane(self, plane):
        result = self.logic_wrapper.get_all_planes()
        for elem in result:
            if elem.airport == plane:
                return plane
        print("engin flugvél í kerfinu með þetta nafn.")
        return ""

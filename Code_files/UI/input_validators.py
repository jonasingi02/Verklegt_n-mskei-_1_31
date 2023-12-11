# Input Validators


class NameLengthException(Exception):
    print("Þessi strengur er lengri en 50 stafir.")


# Validating staff information
class ValidatingStaffInput:
    def __init__(self) -> None:
        pass

    def validate_name_and_string(self, name):
        """Check length of name"""

        if len(name) >= 50:
            return None
        elif len(name) <= 0:
            return None
        else:
            return name

    def get_validated_name(self):
        valid = True
        while valid:
            user_input = input("Nafn starfsmanns: ")
            validated_name = self.validate_name_and_string(user_input)

            if validated_name != None:
                valid = False
                return validated_name
            else:
                print("Vinsamlegast sláðu inn nafn starfsmanns.")

    def validate_kt(self, kt):
        """Check if kennitala is 10 digits and all numeric characters.
        If not prints out error message, try again."""
        valid = kt.isnumeric()

        if len(kt) != 10:
            print("Þessi kennitala var ekki 10 tölustafir.")
            return None
        elif valid != True:
            return None
        else:
            return kt
        
    def get_validated_kennitala(self):
        valid = True
        while valid:
            user_input = input("Kennitala starfsmanns: ")
            validated_kt = self.validate_kt(user_input)

            if validated_kt != None:
                valid = False
                return validated_kt
            else:
                print("Vinsamlegast sláðu inn kennitölu starfsmanns.")

    def validate_phone_number(self, pn):
        """Check validity of phone number by checking if it's only numerical numbers"""
        valid = pn.isnumeric()

        if valid != True:
            print("Vinsamlegast sláið einungis inn tölustafi. Dæmi: 5812345")
            return None
        elif len(pn) != 7:
            print("Þetta símanúmer er ekki 7 stafir.")
            return None
        else:
            return pn
        
    def get_validated_phone_number(self):
        valid = True
        while valid:
            user_input = input("Símanúmer starfsmanns: ")
            validated_pn = self.validate_phone_number(user_input)

            if validated_pn != None:
                valid = False
                return validated_pn



    def get_validated_address(self):
        valid = True
        while valid:
            user_input = input("Heimilisfang: ")
            validated_address = self.validate_name_and_string(user_input)

            if validated_address != None:
                valid = False
                return validated_address
            else:
                print("Vinsamlegast sláðu inn heimilisfang starfsmanns.")


    def validate_postal_code(self, pc):
        if len(pc) == 3:
            try:
                self = int(pc)
                return pc
            except ValueError:
                print("Ekki gilt, reyndu aftur. ")
                return None
        else:
            print("Ekki gilt, reyndu aftur. ")
            return None
        
    def get_validated_pc(self):
        valid = True
        while valid:
            user_input = input("Póstnúmer starfsmanns: ")
            validated_pc = self.validate_postal_code(user_input)

            if validated_pc != None:
                valid = False
                return validated_pc
            else:
                print("Vinsamlegast sláðu inn póstnúmer starfsmanns.")

    def validate_occupation(self, occupation):
        lower_occupation = occupation.lower()

        if lower_occupation == "flugmaður" or lower_occupation == "flugþjónn":
            return occupation
        else:
            print("Vinsamlegast skrifaðu eingöngu flugmaður eða flugþjónn.")
            return None
        
    
    def get_validated_occupation(self):
        print("Skrifaðu inn annað hvort flugmaður eða flugþjónn.")
        valid = True

        while valid:
            user_input = input("Starfsheiti: ")
            validated_occupation = self.validate_occupation(user_input)
            if validated_occupation != None:
                valid = False
                return validated_occupation


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
        """Validate that the contact phone number is only numerical characters."""
        valid = self.isnumeric()

        if valid:
            return self
        else:
            print(
                "Hmm.. Þetta virðist ekki rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
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


# d.country = input("nafn áfangastaðs (string):")
# d.airport = input("nafn flugvallar (string):")
# d.flighttime = input("flugtími (datetime hours):")
# d.distance = input("vegalengd í km (int):")
# d.name = input("nafn tengiliðs (string):")
# d.phone = input("símanúmer tengiliðs (int):")
# self.logic_wrapper.create_destination(d)

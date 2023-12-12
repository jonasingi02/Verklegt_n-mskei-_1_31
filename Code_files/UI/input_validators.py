# Input Validators



# Validating staff information
class ValidatingStaffInput:
    def __init__(self) -> None:
        pass

    def validate_name_and_string(self, name):
        """Check length of name and strings."""
        if len(name) >= 50:
            return None
        elif len(name) <= 0:
            return None
        else:
            return name

    def get_validated_name(self):
        """Validate that a name was put in."""
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
        """Get user input for kennitala and validate it."""
        valid = True
        while valid:
            user_input = input("Kennitala: ")
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
        """Ask the user for input and check if it's a valid phone number."""
        valid = True
        while valid:
            user_input = input("Símanúmer: ")
            validated_pn = self.validate_phone_number(user_input)

            if validated_pn != None:
                valid = False
                return validated_pn

    def get_validated_address(self):
        """Ask the user for input until a valid address is put in."""
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
        """Validate postal codes by icelandic standards. Three number and only numerical."""
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
        """Ask the user for input and check if it is valid. Return only a valid postal code"""
        valid = True
        while valid:
            user_input = input("Póstnúmer: ")
            validated_pc = self.validate_postal_code(user_input)

            if validated_pc != None:
                valid = False
                return validated_pc
            else:
                print("Vinsamlegast sláðu inn póstnúmer starfsmanns.")

    def validate_occupation(self, occupation):
        """Validate occupation title by checking if it is either a pilot or a flight attendant."""
        lower_occupation = occupation.lower()

        if lower_occupation == "flugmaður" or lower_occupation == "flugþjónn":
            return lower_occupation
        else:
            print("Vinsamlegast skrifaðu eingöngu flugmaður eða flugþjónn.")
            return None
        
    def get_validated_occupation(self):
        """Get the validated occupation, as of this update 
        there are only 2 options to add as occupations"""
        print("\nSkrifaðu inn annað hvort flugmaður eða flugþjónn.")
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

    def validate_string(self, name):
        """Check length of name and strings."""
        if len(name) >= 50:
            return None
        elif len(name) <= 0:
            return None
        else:
            return name
        
    def get_validated_string(self, what_input:str):
        """Validate that a string was put in."""
        valid = True
        while valid:
            user_input = input(what_input)
            validated_name = self.validate_string(user_input)

            if validated_name != None:
                valid = False
                return validated_name
            else:
                lower_what_input = what_input.rstrip(what_input[-1]).lower()
                print(f"Vinsamlegast sláðu inn {lower_what_input}.")    
        
    def validate_num_seats(self):
        """Check if number of seats input is only integers"""
        check = True
        while check:
            user_input = input("Fjöldi sæta: ")
            valid: bool = user_input.isnumeric()
            if valid:
                check = False
                return user_input
            else:
                print("Þetta virðist hafa farið úrskeiðis. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi.")
                


# Validate Voyage information
class ValidateVoyageInput:
    def __init__(self) -> None:
        pass

    def validate_voyage_string(self):
        """Check length of input"""
        if len(self) >= 50:
            print("Þessi strengur er lengri en 50 stafir.")
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
            print("Þessi strengur er lengri en 50 stafir.")
        else:
            return self

    def validate_contact_phone_number(self):
        """Validate that the contact phone number is only numerical characters."""
        valid = self.isnumeric()

        if valid:
            return self
        else:
            print(
                "Þetta virðist ekki rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
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
        print("\nengin áfangastaður í kerfinu með þennan flugvöll.")
        return ""

    def validate_voyage_plane(self, plane):
        result = self.logic_wrapper.get_all_planes()
        for elem in result:
            if elem.name == plane:
                return plane
        print("\nengin flugvél í kerfinu með þetta nafn.")
        return ""


# d.country = input("nafn áfangastaðs (string):")
# d.airport = input("nafn flugvallar (string):")
# d.flighttime = input("flugtími (datetime hours):")
# d.distance = input("vegalengd í km (int):")
# d.name = input("nafn tengiliðs (string):")
# d.phone = input("símanúmer tengiliðs (int):")
# self.logic_wrapper.create_destination(d)

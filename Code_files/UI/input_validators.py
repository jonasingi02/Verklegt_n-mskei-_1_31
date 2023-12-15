# Input Validators
from model.FMVoyage import FMvoyage
from logic.logic_wrapper import Logic_wrapper


# Validating staff information
class ValidatingStaffInput:
    def __init__(self) -> None:
        self.logic_wrapper = Logic_wrapper

    def validate_name_and_string(self, name) -> str or None:
        """Check length of name and strings."""
        if len(name) >= 50:
            return None
        elif len(name) <= 0:
            return None
        else:
            return name

    def get_validated_name(self) -> str or None:
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

    def validate_kt(self, kt) -> str or None:
        """Check if kennitala is 10 digits, is all numeric characters and if this kt is not already in the 
           system. If not prints out error message, try again."""
        valid = kt.isnumeric()
        logic_instance = self.logic_wrapper()
        ktlist = logic_instance.read_all_employees()

        for i in ktlist:
            if i.kt == kt:
                print("Þessi kennitala er nú þegar í kerfinu.")
                return None

        if len(kt) != 10:
            print("Þessi kennitala var ekki 10 tölustafir.")
            return None
        elif valid != True:
            return None
        else:
            return kt
        
    def get_validated_kennitala(self) -> str:
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

    def validate_phone_number(self, pn) -> str or None:
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
        
    def get_validated_phone_number(self) -> str:
        """Ask the user for input and check if it's a valid phone number."""
        valid = True
        while valid:
            user_input = input("Símanúmer: ")
            validated_pn = self.validate_phone_number(user_input)

            if validated_pn != None:
                valid = False
                return validated_pn

    def get_validated_address(self) -> str:
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

    def validate_postal_code(self, pc) -> str or None:
        """Validate postal codes by icelandic standards. Three numbers and only numerical."""
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
        
    def get_validated_pc(self) -> str:
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

    def validate_occupation(self, occupation) -> str or None:
        """Validate occupation title by checking if it is either a pilot or a flight attendant."""
        lower_occupation = occupation.lower()

        if lower_occupation == "flugmaður" or lower_occupation == "flugþjónn":
            return lower_occupation
        else:
            print("Vinsamlegast skrifaðu eingöngu flugmaður eða flugþjónn.")
            return None
        
    def get_validated_occupation(self) -> str:
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
        self.logic_wrapper = Logic_wrapper

    def validate_string(self, name) -> str or None:
        """Check length of name and strings."""
        if len(name) >= 50:
            return None
        elif len(name) <= 0:
            return None
        else:
            return name
        
    def get_validated_string(self, what_input:str) -> str:
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

    def get_validated_plane_name(self, what_input):
        """Validate that a string was put in."""

        s = self.logic_wrapper()
        list = s.get_all_planes()

        valid = True


        while valid:
            user_input = input(what_input)

            validated_name = self.validate_string(user_input)

            for i in list:
                if i.name == user_input:
                    print("Það er önnur vél með þetta nafn")
                    validated_name = None

            if validated_name != None:
                valid = False
                return validated_name
            else:
                lower_what_input = what_input.rstrip(what_input[-1]).lower()
                print(f"Vinsamlegast sláðu inn {lower_what_input}.")   

        
    def validate_num_seats(self) -> str:
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

    def validate_voyage_string(self) -> str:
        """Check length of input"""
        if len(self) >= 50:
            print("Þessi strengur er lengri en 50 stafir.")
        else:
            return self

    def validate_length_km(self) -> float or None:
        """Check if user input for kilometers is a float."""
        try:
            self = float(self)
            return self
        except ValueError:
            return None


# Validate Destination inputs
class ValidateDestinationInputs:
    def __init__(self) -> None:
        self.logic_wrapper = Logic_wrapper

    def validate_destination_string(self, input) -> str:
        """Check length of input"""
        if len(input) >= 50:
            print("Þessi strengur er lengri en 50 stafir.")
            return ""
        else:
            return input
        
    def validate_dest_airport(self, input):

        s = self.logic_wrapper()
        list = s.get_all_destinations()
        bool = True
        for i in list:
            if i.airport == input:
                bool = False
            
        if len(input) >= 50:
            print("Þessi strengur er lengri en 50 stafir.")
        elif(bool == True):
            return input
        print("þessi flugvöllur er nú þegar í kerfinu veldu ")
        return ""

    def validate_contact_phone_number(self, phone) -> str:
        """Validate that the contact phone number is only numerical characters."""
        valid = phone.isnumeric()

        if valid:
            return phone
        else:
            print(
                "Þetta virðist ekki rétt. Reyndu aftur. Vinsamlegast sláðu bara inn tölustafi."
            )
            return ""

class ValidateFMVoyageInfo:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def validate_voyage_dest(self, dest) -> str:
        """Validate that there is an airport in the system with that name"""
        result = self.logic_wrapper.get_all_destinations()
        for elem in result:
            if elem.airport == dest:
                return dest
        print("\nEnginn áfangastaður í kerfinu með þennan flugvöll.")
        return ""

    def validate_voyage_plane(self, plane) -> str:
        """Validate that there is a plane in the system with that name"""
        result = self.logic_wrapper.get_all_planes()
        for elem in result:
            if elem.name == plane:
                return plane
        print("\nEngin flugvél í kerfinu með þetta nafn.")
        return ""
    
    def validate_time_of_takeoff(self, date, time) -> str or None:
        """Check if there is a scheduled takeoff at the same time"""
        validate_time = self.logic_wrapper.read_all_fmvoyages()
        time_list = []

        for elem in validate_time:
            if elem.time == time and elem.date == date:
                time_list.append(elem)

        if time_list:
            return time_list
        else:
            return None

    def validate_voyage(self, voyage, list) -> str:
        """Validate chosen voyage ID"""
        if voyage == "b" or voyage == "B":
            return "b"
        
        for elem in list:
            if elem.id == voyage:
                return elem.id
        print("\nEngin vinnuferð í kerfinu með þetta ID")
        return ""

    def validate_voyage_staff(self, pilot, list) -> str:
        "Validate the staff on the voyage"
        if pilot == "b" or pilot == "B":
            return "b"
            
        for i in list:
            if pilot == i.kt:
                return pilot
        return ""
    
    def validate_number_of_staff_on_voyage(self, occupation) -> int:
        """Validate the minimum staff on shift"""
        user_input = int(input(f"Veldu magn {occupation} (til baka: b): "))
        valid = True
        
        
        if type(user_input) != int :
            print("Það þarf að vera tala")
            valid = False
        
        while valid:
            if occupation == "flugþjóna":
                if user_input < 1:
                    print("Það þarf að vera a.m.k einn fljugþjónn í hverri ferð.")
                    user_input = int(input(f"Veldu magn {occupation}: "))
                else:
                    valid = False
                    return user_input
            
            elif occupation == "flugmanna":
                if user_input < 2:
                    print("Það þarf að vera a.m.k tveir flugmenn í hverri ferð.")
                    user_input = int(input(f"Veldu magn {occupation}: "))
                else:
                    valid = False
                    return user_input

    def validate_voyage_id(self, voyage_list) -> str:
        """Validate if the voyage id is in the system"""
        while True:
            id_input = input("Sláðu inn ID flugsins til að finna flugið sem þú ætlar að breyta upplýsingum um.\n")
            
            for voyage in voyage_list:
                if id_input == voyage.id:
                    return id_input
            print("Engin vinnuferð í kerfinu með þetta ID. Reyndu aftur.")

    def get_validated_date(self) -> str: 
        """Check if the input for date is correctly formatted"""
        while True: 
            new_date_input = input("Skráðu inn uppfærða dagsetningu: (DD-MM-ÁÁ) ")
            date_splits = new_date_input.split("-")

            if len(date_splits) == 3 and all(len(date_split) == 2 for date_split in date_splits):
                return "-".join(date_splits)
            else: 
                print("Úps!, Passaðu að slá inn dagsetningu á eftirfarandi hátt: (DD-MM-ÁÁ) ")

    def get_validated_time(self) -> str:
        """Check if the input for time is correctly formatted""" 
        while True:
            new_time_input = input("Skráðu inn nýja tímasetningu: (00:00) ")
            time_split = new_time_input.split(":")
            
            if len(time_split) == 2 and len(time_split[0]) == 2 and len(time_split[1]) == 2:
                return ":".join(time_split)
            else:
                print("Úps!, Passaðu að slá inn tímasetninguna á eftirfarandi hátt: (00:00) ")
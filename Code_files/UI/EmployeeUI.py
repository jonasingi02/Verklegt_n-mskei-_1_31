from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt


class EmployeeUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        # AsciiArt.airplane_1_ascii()
        # print("Velkomin/n vaktstjóri")
        print("Hvað má bjóða þér að gera:\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                result = self.logic_wrapper.get_all_employees()
                for elem in result:
                   print(f"Nafn {elem.name}, Kennitala: {elem.kt}") 
            elif command == "2":
                e = Employee()
                
                validating_input = ValidatingStaffInput()
                e.name = validating_input.get_validated_name()
                e.kt = validating_input.get_validated_kennitala()
                e.phone_number = validating_input.get_validated_phone_number()
                e.address = validating_input.get_validated_address()
                e.postal_code = validating_input.get_validated_pc()
                e.occupation = validating_input.get_validated_occupation()

                self.logic_wrapper.create_employee(e)
                print(f"\nÞú hefur bætt við starfsmanninum: {e.name}, {e.occupation}.")

            elif command == "3":
                validating_input = ValidatingStaffInput()

                print("Þú hefur valið að uppfæra upplýsingar um starfsmann.\nSláðu inn kennitölu starfsmanns til að finna þann sem þú ætlar að breyta upplýsingum um.")
                kt = validating_input.get_validated_kennitala()
                print("Hvað má bjóða þér að uppfæra hjá starfsmanni?\n")
                print("1. Símanúmer \n2. Heimilisfang \n3. Póstnúmer \n4. Starfsheiti")
                user_input = int(input("\nInnsláttarreitur: "))
                if user_input == 1:
                    info = "símanúmer"    
                    column_to_update = 2
                    new_info = validating_input.get_validated_phone_number()
                elif user_input == 2:
                    info = "heimilisfang"
                    column_to_update = 3
                    new_info = validating_input.get_validated_address()
                elif user_input == 3:
                    info = "póstnúmer"
                    column_to_update = 4
                    new_info = validating_input.get_validated_pc()
                elif user_input == 4:
                    info = "starfsheiti"
                    column_to_update = 5
                    new_info = validating_input.get_validated_occupation()

                print(f"\nÞú hefur uppfært {info} starfsmanns með kennitöluna {kt}.")
                self.logic_wrapper.update_employee(kt, column_to_update, new_info)
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Invalid input, try again.")

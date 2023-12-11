from logic.logic_wrapper import Logic_wrapper
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt


class EmployeeUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        AsciiArt.airplane_1_ascii()
        print("Velkomin/n vaktstjóri")
        print("Hvað má bjóða þér að gera:\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            if command == "1":
                pass
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
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Invalid input, try again.")

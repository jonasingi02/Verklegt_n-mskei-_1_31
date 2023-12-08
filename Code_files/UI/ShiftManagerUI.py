from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt


class ShiftManagerUI:
    def __init__(self, logic_connection):
        self.data_wrapper = logic_connection

    def menu_output(self):
        AsciiArt.airplane_1_ascii()
        print("Velkomin/n vaktstjóri")
        print(
            "Hvað má bjóða þér að gera:\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\nQ: Hætta\nB: Til baka\n"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            if command == "1":
                pass
            elif command == "2":
                e = Employee()

                e.name = ValidatingStaffInput.validate_name(
                    input("Skráðu nafn starfsmanns: ")
                )

                e.kt = ValidatingStaffInput.validate_kt(
                    input("Skráðu kennitölu starfsmanns: ")
                )
                while e.kt == None:
                    e.kt = ValidatingStaffInput.validate_kt(
                        input("Skráðu kennitölu starfsmanns: ")
                    )

                e.phone_number = ValidatingStaffInput.validate_phone_number(
                    input("Skráðu símanúmer starfsmanns: ")
                )
                while e.phone_number == None:
                    e.phone_number = ValidatingStaffInput.validate_phone_number(
                        input("Skráðu símanúmer starfsmanns: ")
                    )

                e.address = ValidatingStaffInput.validate_name(
                    input("Skráðu heimilisfang starfsmanns: ")
                )
                e.postal_code = int(input("Skráðu póstfang starfsmanns: "))
                e.occupation = ValidatingStaffInput.validate_name(
                    "Skráðu starfsgrein starfsmanns (Flugmaður/Flugþjónn): "
                )
                self.data_wrapper.create_employee(e)
                print(f"\nÞú hefur bætt við starfsmanninum: {e.name}.")

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Invalid input, try again.")

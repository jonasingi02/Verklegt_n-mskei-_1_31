from model.employee import Employee
from UI.staff_input_validators import ValidatingStaffInput


class ShiftManagerUI:
    def __init__(self):
        pass

    def menu_output(self):
        print("Velkomin/n vaktstjóri")
        print(
            "Hvað má bjóða þér að gera:\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\nQ: Hætta\nB: Til baka"
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
                e.phone_number = int(input("Skráður símanúmer starfsmanns: "))
                e.address = ValidatingStaffInput.validate_name(
                    input("Skráðu heimilisfang starfsmanns: ")
                )
                e.postal_code = int(input("Skráðu póstfang starfsmanns: "))
                e.occupation = ValidatingStaffInput.validate_name(
                    "Skráðu starfsgrein starfsmanns: "
                )

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Invalid input, try again.")

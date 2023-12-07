from model.planes import Planes
from .staff_input_validators import ValidatingStaffInput, ValidatePlaneInfo
from logic.logic_wrapper import Logic_wrapper


class planesUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera:\n\n1: birta allar flugvélar\n2: bæta við flugvél\n3: uppfæra flugvél\nQ: Hætta\nB: til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()

            if command == "1":
                pass

            elif command == "2":
                p = Planes()

                input_field = True
                while input_field:
                    p.name = ValidatePlaneInfo.validate_plane_string(
                        input("Nafn vélar: ")
                    )
                    while p.name == None:
                        p.name = ValidatePlaneInfo.validate_plane_string(
                            input("Nafn vélar: ")
                        )

                    p.type = ValidatePlaneInfo.validate_plane_string(
                        input("Tegund vélar: ")
                    )
                    while p.type == None:
                        p.type = ValidatePlaneInfo.validate_plane_string(
                            input("Tegund vélar: ")
                        )

                    p.numseats = ValidatePlaneInfo.validate_num_seats(
                        input("Fjöldi sæta: ")
                    )
                    while p.numseats == None:
                        p.numseats = p.type = ValidatePlaneInfo.validate_num_seats(
                            input("Fjöldi sæta: ")
                        )

                    self.logic_wrapper.create_plane(p)
                    print(
                        f"\nÞú hefur bætt við flugvélinni: {p.name}, {p.type}, fjöldi sæta {p.numseats}\n\n."
                    )
                    input_field = False

            elif command == "3":
                pass

            elif command == "q":
                return "q"

            elif command == "b":
                return "b"

            else:
                print("Virkaði ekki, reyndu aftur.")
